"""
Base class for state-specific requirements.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
import re

class BaseState(ABC):
    """Base class defining interface for state-specific requirements."""
    
    def __init__(
        self,
        professional_requirements: Dict[str, Any],
        foreign_requirements: Dict[str, Any],
        tax_requirements: Dict[str, Any],
        regulated_professions: Dict[str, Any]
    ):
        """Initialize state requirements."""
        self._professional_requirements = professional_requirements
        self._foreign_requirements = foreign_requirements
        self._tax_requirements = tax_requirements
        self._regulated_professions = regulated_professions
    
    @abstractmethod
    def _get_state_code(self) -> str:
        """Get state code."""
        pass
    
    @abstractmethod
    def _get_state_name(self) -> str:
        """Get state name."""
        pass
    
    def get_formation_requirements(self) -> Dict[str, Any]:
        """Get formation requirements."""
        return {
            "state_code": self._get_state_code(),
            "state_name": self._get_state_name(),
            "publication_required": self._is_publication_required(),
            "publication_period": self._get_publication_period(),
            "professional_requirements": self._professional_requirements,
            "foreign_requirements": self._foreign_requirements
        }
    
    def get_filing_fees(self) -> float:
        """Get filing fees."""
        base_fee = self._get_base_filing_fee()
        expedited_fee = self._get_expedited_fee() if self._is_expedited() else 0
        publication_fee = self._get_publication_fee() if self._is_publication_required() else 0
        return base_fee + expedited_fee + publication_fee
    
    def get_registered_agent_fees(self) -> float:
        """Get registered agent fees."""
        return self._get_registered_agent_fee()
    
    def get_annual_fees(self) -> float:
        """Get annual fees."""
        return self._get_annual_report_fee()
    
    def get_processing_time(self) -> int:
        """Get processing time in days."""
        return self._get_standard_processing_time()
    
    def get_income_tax_rate(self) -> float:
        """Get income tax rate."""
        return self._tax_requirements.get("income_tax_rate", 0.0)
    
    def get_sales_tax_rate(self) -> float:
        """Get sales tax rate."""
        return self._tax_requirements.get("sales_tax_rate", 0.0)
    
    def get_tax_incentives(self) -> List[Dict[str, Any]]:
        """Get tax incentives."""
        return self._tax_requirements.get("incentives", [])
    
    def get_regulatory_burden(self) -> str:
        """Get regulatory burden level."""
        return self._get_regulatory_burden_level()
    
    def get_business_support_programs(self) -> List[Dict[str, Any]]:
        """Get business support programs."""
        return self._get_support_programs()
    
    def get_insurance_requirements(self) -> Dict[str, Any]:
        """Get insurance requirements."""
        return self._get_insurance_requirements()
    
    def get_annual_requirements(self) -> List[Dict[str, Any]]:
        """Get annual requirements."""
        return self._get_annual_requirements()
    
    def get_record_keeping_requirements(self) -> Dict[str, Any]:
        """Get record keeping requirements."""
        return self._get_record_keeping_requirements()
    
    def get_reporting_requirements(self) -> List[Dict[str, Any]]:
        """Get reporting requirements."""
        return self._get_reporting_requirements()
    
    def get_professional_governance_requirements(self) -> Dict[str, Any]:
        """Get professional governance requirements."""
        return self._professional_requirements.get("governance", {})
    
    def get_legal_risks(self) -> List[Dict[str, Any]]:
        """Get legal risks."""
        return self._get_legal_risks()
    
    def get_formation_risks(self) -> List[Dict[str, Any]]:
        """Get formation risks."""
        return self._get_formation_risks()
    
    def get_formation_recommendations(self) -> List[Dict[str, Any]]:
        """Get formation recommendations."""
        return self._get_formation_recommendations()
    
    def get_compliance_requirements(self) -> List[Dict[str, Any]]:
        """Get compliance requirements."""
        return self._get_compliance_requirements()
    
    def get_governance_warnings(self) -> List[str]:
        """Get governance warnings."""
        return self._get_governance_warnings()
    
    def _get_base_filing_fee(self) -> float:
        """Get base filing fee."""
        return 100.0  # Default base fee
    
    def _get_expedited_fee(self) -> float:
        """Get expedited processing fee."""
        return 50.0  # Default expedited fee
    
    def _get_publication_fee(self) -> float:
        """Get publication fee if required."""
        return 200.0  # Default publication fee
    
    def _get_registered_agent_fee(self) -> float:
        """Get registered agent fee."""
        return 120.0  # Default annual registered agent fee
    
    def _get_annual_report_fee(self) -> float:
        """Get annual report fee."""
        return 50.0  # Default annual report fee
    
    def _get_standard_processing_time(self) -> int:
        """Get standard processing time in days."""
        return 5  # Default processing time
    
    def _is_expedited(self) -> bool:
        """Check if expedited processing is requested."""
        return False  # Default to standard processing
    
    def _is_publication_required(self) -> bool:
        """Check if publication is required."""
        return False  # Default to no publication requirement
    
    def _get_publication_period(self) -> int:
        """Get publication period in days if required."""
        return 0  # Default no publication period
    
    def _get_regulatory_burden_level(self) -> str:
        """Get regulatory burden level."""
        return "Medium"  # Default regulatory burden
    
    def _get_support_programs(self) -> List[Dict[str, Any]]:
        """Get business support programs."""
        return []  # Default no support programs
    
    def _get_insurance_requirements(self) -> Dict[str, Any]:
        """Get insurance requirements."""
        return {
            "general_liability": {
                "required": True,
                "minimum_coverage": 1000000
            }
        }
    
    def _get_annual_requirements(self) -> List[Dict[str, Any]]:
        """Get annual requirements."""
        return [
            {
                "name": "Annual Report",
                "deadline": "Anniversary of formation",
                "fee": self._get_annual_report_fee()
            }
        ]
    
    def _get_record_keeping_requirements(self) -> Dict[str, Any]:
        """Get record keeping requirements."""
        return {
            "financial_records": {
                "retention_period": "7 years",
                "type": "Required"
            },
            "meeting_minutes": {
                "retention_period": "Permanent",
                "type": "Required"
            },
            "tax_records": {
                "retention_period": "7 years",
                "type": "Required"
            }
        }
    
    def _get_reporting_requirements(self) -> List[Dict[str, Any]]:
        """Get reporting requirements."""
        return [
            {
                "name": "Annual Report",
                "frequency": "Annual",
                "description": "Basic information update"
            }
        ]
    
    def _get_legal_risks(self) -> List[Dict[str, Any]]:
        """Get legal risks."""
        return [
            {
                "category": "Compliance",
                "description": "Failure to maintain required records",
                "severity": "Medium"
            },
            {
                "category": "Legal",
                "description": "Inadequate operating agreement",
                "severity": "High"
            }
        ]
    
    def _get_formation_risks(self) -> List[Dict[str, Any]]:
        """Get formation risks."""
        return [
            {
                "category": "Administrative",
                "description": "Processing delays",
                "severity": "Low"
            },
            {
                "category": "Documentation",
                "description": "Incomplete filings",
                "severity": "Medium"
            }
        ]
    
    def _get_formation_recommendations(self) -> List[Dict[str, Any]]:
        """Get formation recommendations."""
        return [
            {
                "category": "Documentation",
                "suggestion": "Maintain thorough records",
                "priority": "High"
            },
            {
                "category": "Compliance",
                "suggestion": "Set up compliance calendar",
                "priority": "Medium"
            }
        ]
    
    def _get_compliance_requirements(self) -> List[Dict[str, Any]]:
        """Get compliance requirements."""
        return [
            {
                "category": "Records",
                "requirements": [
                    "Maintain financial records",
                    "Keep meeting minutes",
                    "Document major decisions"
                ]
            },
            {
                "category": "Filings",
                "requirements": [
                    "File annual report",
                    "Update registered agent",
                    "Maintain licenses"
                ]
            }
        ]
    
    def _get_governance_warnings(self) -> List[str]:
        """Get governance warnings."""
        return [
            "Maintain clear separation between personal and business activities",
            "Document all major business decisions",
            "Keep accurate and complete records"
        ]
