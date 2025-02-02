"""
Delaware state-specific requirements implementation.
"""

from typing import Dict, Any, List, Optional
from states.base_state import BaseState

class Delaware(BaseState):
    """Delaware state requirements implementation."""
    
    def _get_state_code(self) -> str:
        return "DE"
    
    def _get_state_name(self) -> str:
        return "Delaware"
    
    def get_formation_requirements(self) -> Dict[str, Any]:
        return {
            "filing_agency": "Delaware Division of Corporations",
            "forms_required": ["Certificate of Formation"],
            "signature_requirements": {
                "authorized_signer": True,
                "notary_required": False
            },
            "minimum_members": 1,
            "requires_operating_agreement": False,
            "allows_series_llc": True,
            "allows_professional_llc": True,
            "foreign_qualification": {
                "required": True,
                "forms": ["Certificate of Registration"]
            }
        }
    
    def get_filing_fees(self) -> Dict[str, float]:
        return {
            "formation": 90.00,
            "name_reservation": 75.00,
            "expedited": 50.00,
            "same_day": 100.00,
            "two_hour": 500.00,
            "one_hour": 1000.00,
            "certified_copy": 50.00,
            "certificate_of_good_standing": 50.00,
            "foreign_qualification": 200.00
        }
    
    def get_processing_times(self) -> Dict[str, Any]:
        return {
            "standard": 10,  # business days
            "expedited": 24,  # hours
            "same_day": 1,   # business day
            "two_hour": 2,   # hours
            "one_hour": 1    # hour
        }
    
    def get_required_filings(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "Certificate of Formation",
                "form_number": None,
                "frequency": "One-time",
                "fee": 90.00,
                "required": True
            },
            {
                "name": "Annual Report",
                "form_number": None,
                "frequency": "Annual",
                "fee": 300.00,
                "required": True,
                "due_date": "June 1"
            }
        ]
    
    def get_name_requirements(self) -> Dict[str, Any]:
        return {
            "required_terms": ["Limited Liability Company", "LLC", "L.L.C."],
            "prohibited_terms": [
                "Bank", "Insurance", "Trust", "University",
                "College", "Educational Institution"
            ],
            "restricted_terms": {
                "Engineer": "Board of Professional Engineers",
                "Architect": "Board of Architects"
            },
            "reservation_available": True,
            "reservation_duration": 120,  # days
            "reservation_fee": 75.00,
            "reservation_renewable": True,
            "distinguishable": True
        }
    
    def get_registered_agent_requirements(self) -> Dict[str, Any]:
        return {
            "required": True,
            "state_residency_required": True,
            "business_hours": "9am-5pm",
            "commercial_allowed": True,
            "entity_as_agent": True,
            "office_requirements": {
                "physical_address": True,
                "po_box_allowed": False,
                "business_hours": True
            },
            "filing_required": {
                "change_of_agent": True,
                "change_of_address": True
            },
            "fees": {
                "change_of_agent": 50.00,
                "change_of_address": 50.00
            }
        }
    
    def get_tax_requirements(self) -> Dict[str, Any]:
        return {
            "income_tax": {
                "required": False,
                "type": "Pass-through",
                "exceptions": None
            },
            "franchise_tax": {
                "required": True,
                "amount": 300.00,
                "due_date": "June 1",
                "filing_requirements": {
                    "form": "Annual Report",
                    "online_filing": True
                }
            },
            "sales_tax": {
                "required": True,
                "rate": 0.00,  # Delaware has no sales tax
                "exemptions_available": True
            },
            "employer_taxes": {
                "unemployment": {
                    "required": "If employees",
                    "registration": "Department of Labor"
                },
                "withholding": {
                    "required": "If employees",
                    "registration": "Division of Revenue"
                }
            }
        }
    
    def get_annual_requirements(self) -> Dict[str, Any]:
        return {
            "annual_report": {
                "required": True,
                "due_date": "June 1",
                "fee": 300.00,
                "filing_method": "Online",
                "late_penalties": {
                    "amount": 200.00,
                    "additional_fees": True
                }
            },
            "franchise_tax": {
                "required": True,
                "amount": 300.00,
                "due_date": "June 1",
                "calculation_method": "Flat fee"
            },
            "initial_report": {
                "required": False
            }
        }
    
    def get_publication_requirements(self) -> Optional[Dict[str, Any]]:
        return None  # Delaware has no publication requirements
    
    def get_professional_license_requirements(self) -> Dict[str, Any]:
        return {
            "professional_llc": {
                "allowed": True,
                "regulated_professions": [
                    "Accountants",
                    "Architects",
                    "Engineers",
                    "Healthcare Providers",
                    "Attorneys"
                ],
                "ownership_restrictions": {
                    "professional_requirements": True,
                    "licensing_requirements": True
                },
                "name_requirements": {
                    "professional_designation": True,
                    "licensing_board_approval": True
                }
            },
            "general_business_license": {
                "required": True,
                "issuing_agency": "Division of Revenue",
                "fee": 75.00,
                "renewal": "Annual"
            }
        }
