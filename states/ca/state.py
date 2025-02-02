"""
California state-specific requirements implementation.
"""

from typing import Dict, Any, List, Optional
from states.base_state import BaseState

class California(BaseState):
    """California state requirements implementation."""
    
    def _get_state_code(self) -> str:
        return "CA"
    
    def _get_state_name(self) -> str:
        return "California"
    
    def _get_base_filing_fee(self) -> float:
        """Get base filing fee."""
        return 70.0  # California LLC formation fee
    
    def _get_expedited_fee(self) -> float:
        """Get expedited processing fee."""
        return 350.0  # California expedited fee (24-hour)
    
    def _get_registered_agent_fee(self) -> float:
        """Get registered agent fee."""
        return 50.0  # California registered agent fee
    
    def _get_annual_report_fee(self) -> float:
        """Get annual report fee."""
        return 800.0  # California annual franchise tax minimum
    
    def _get_standard_processing_time(self) -> int:
        """Get standard processing time in days."""
        return 15  # California standard processing time
    
    def _is_publication_required(self) -> bool:
        """Check if publication is required."""
        return False  # California does not require publication
    
    def _get_regulatory_burden_level(self) -> str:
        """Get regulatory burden level."""
        return "High"  # California has significant regulatory requirements
    
    def _get_support_programs(self) -> List[Dict[str, Any]]:
        """Get business support programs."""
        return [
            {
                "name": "California Small Business Development Center",
                "description": "Free consulting and training for small businesses",
                "website": "https://www.californiasbdc.org/"
            },
            {
                "name": "California GO-Biz",
                "description": "State's economic development department",
                "website": "https://business.ca.gov/"
            }
        ]
    
    def _get_insurance_requirements(self) -> Dict[str, Any]:
        """Get insurance requirements."""
        return {
            "workers_compensation": {
                "required": True,
                "description": "Required for businesses with employees"
            },
            "general_liability": {
                "required": False,
                "recommended": True,
                "minimum_coverage": 1000000
            },
            "professional_liability": {
                "required": False,
                "recommended": True,
                "description": "Recommended for professional services"
            }
        }
    
    def _get_annual_requirements(self) -> List[Dict[str, Any]]:
        """Get annual requirements."""
        return [
            {
                "name": "Statement of Information",
                "deadline": "Every two years",
                "fee": 20.00,
                "description": "Biennial information statement"
            },
            {
                "name": "Annual Franchise Tax",
                "deadline": "April 15",
                "fee": self._get_annual_report_fee(),
                "description": "Annual minimum franchise tax"
            }
        ]
    
    def _get_record_keeping_requirements(self) -> Dict[str, Any]:
        """Get record keeping requirements."""
        return {
            "financial_records": {
                "retention_period": "7 years",
                "type": "Required",
                "description": "Balance sheets, income statements, tax returns"
            },
            "formation_documents": {
                "retention_period": "Permanent",
                "type": "Required",
                "description": "Articles of Organization, Operating Agreement"
            },
            "meeting_minutes": {
                "retention_period": "Permanent",
                "type": "Required",
                "description": "Records of major decisions and meetings"
            },
            "tax_records": {
                "retention_period": "7 years",
                "type": "Required",
                "description": "State and federal tax returns, supporting documents"
            }
        }
    
    def _get_reporting_requirements(self) -> List[Dict[str, Any]]:
        """Get reporting requirements."""
        return [
            {
                "name": "Statement of Information",
                "frequency": "Biennial",
                "deadline": "Every two years",
                "description": "Update business information"
            },
            {
                "name": "Franchise Tax Return",
                "frequency": "Annual",
                "deadline": "April 15",
                "description": "Annual tax return and payment"
            }
        ]
    
    def _get_legal_risks(self) -> List[Dict[str, Any]]:
        """Get legal risks."""
        return [
            {
                "category": "Compliance",
                "description": "Failure to maintain Statement of Information",
                "severity": "High"
            },
            {
                "category": "Financial",
                "description": "Late franchise tax payments",
                "severity": "High"
            },
            {
                "category": "Employment",
                "description": "Non-compliance with labor laws",
                "severity": "High"
            }
        ]
    
    def _get_formation_risks(self) -> List[Dict[str, Any]]:
        """Get formation risks."""
        return [
            {
                "category": "Documentation",
                "description": "Incomplete formation documents",
                "severity": "High"
            },
            {
                "category": "Compliance",
                "description": "Missing required licenses or permits",
                "severity": "High"
            },
            {
                "category": "Tax",
                "description": "Failure to register for required taxes",
                "severity": "High"
            }
        ]
    
    def _get_formation_recommendations(self) -> List[Dict[str, Any]]:
        """Get formation recommendations."""
        return [
            {
                "category": "Documentation",
                "suggestion": "Create detailed operating agreement",
                "priority": "High"
            },
            {
                "category": "Compliance",
                "suggestion": "Register for all required taxes",
                "priority": "High"
            },
            {
                "category": "Legal",
                "suggestion": "Consult with California business attorney",
                "priority": "High"
            }
        ]
    
    def _get_compliance_requirements(self) -> List[Dict[str, Any]]:
        """Get compliance requirements."""
        return [
            {
                "category": "Filings",
                "requirements": [
                    "File Statement of Information biennially",
                    "Pay annual franchise tax",
                    "Maintain current agent for service of process"
                ]
            },
            {
                "category": "Taxes",
                "requirements": [
                    "Register for required taxes",
                    "File annual tax returns",
                    "Pay estimated taxes quarterly"
                ]
            },
            {
                "category": "Employment",
                "requirements": [
                    "Comply with wage and hour laws",
                    "Maintain workers' compensation insurance",
                    "Follow workplace safety regulations"
                ]
            }
        ]
    
    def _get_governance_warnings(self) -> List[str]:
        """Get governance warnings."""
        return [
            "Maintain strict compliance with California labor laws",
            "Keep detailed records of all business transactions",
            "File Statement of Information on time",
            "Pay franchise tax by deadline",
            "Maintain required licenses and permits",
            "Follow California environmental regulations"
        ]
