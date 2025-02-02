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
    
    def get_formation_requirements(self) -> Dict[str, Any]:
        return {
            "filing_agency": "California Secretary of State",
            "forms_required": [
                "Articles of Organization (Form LLC-1)",
                "Statement of Information (Form LLC-12)",
                "Operating Agreement"
            ],
            "signature_requirements": {
                "authorized_signer": True,
                "notary_required": False
            },
            "minimum_members": 1,
            "requires_operating_agreement": True,
            "allows_series_llc": False,
            "allows_professional_llc": True,
            "foreign_qualification": {
                "required": True,
                "forms": ["Application to Register (Form LLC-5)"]
            }
        }
    
    def get_filing_fees(self) -> Dict[str, float]:
        return {
            "formation": 70.00,
            "name_reservation": 10.00,
            "statement_of_information": 20.00,
            "expedited": 350.00,
            "preclearance": 500.00,
            "certified_copy": 15.00,
            "certificate_of_good_standing": 5.00,
            "foreign_qualification": 70.00
        }
    
    def get_processing_times(self) -> Dict[str, Any]:
        return {
            "standard": 10,  # business days
            "expedited": 24,  # hours
            "preclearance": 5,  # business days
            "counter_drop_off": 1  # business day
        }
    
    def get_required_filings(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "Articles of Organization",
                "form_number": "LLC-1",
                "frequency": "One-time",
                "fee": 70.00,
                "required": True
            },
            {
                "name": "Statement of Information",
                "form_number": "LLC-12",
                "frequency": "Initial + Biennial",
                "fee": 20.00,
                "required": True,
                "due_date": "90 days after formation, then every 2 years"
            },
            {
                "name": "Operating Agreement",
                "form_number": None,
                "frequency": "One-time",
                "fee": 0.00,
                "required": True
            }
        ]
    
    def get_name_requirements(self) -> Dict[str, Any]:
        return {
            "required_terms": ["Limited Liability Company", "LLC", "L.L.C."],
            "prohibited_terms": [
                "Bank", "Insurance", "Trust", "Corporation",
                "Corp.", "Inc.", "Incorporated"
            ],
            "restricted_terms": {
                "Engineer": "Board of Professional Engineers",
                "Architect": "Board of Architects",
                "Medical": "Medical Board"
            },
            "reservation_available": True,
            "reservation_duration": 60,  # days
            "reservation_fee": 10.00,
            "reservation_renewable": True,
            "distinguishable": True
        }
    
    def get_registered_agent_requirements(self) -> Dict[str, Any]:
        return {
            "required": True,
            "state_residency_required": True,
            "business_hours": "Normal business hours",
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
                "change_of_agent": 0.00,  # Included in Statement of Information
                "change_of_address": 0.00  # Included in Statement of Information
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
                "minimum_amount": 800.00,
                "due_date": "15th day of 4th month",
                "filing_requirements": {
                    "form": "Form 568",
                    "online_filing": True
                }
            },
            "sales_tax": {
                "required": True,
                "base_rate": 0.0725,
                "local_rates": True,
                "registration": "CDTFA",
                "exemptions_available": True
            },
            "employer_taxes": {
                "unemployment": {
                    "required": "If employees",
                    "registration": "EDD"
                },
                "withholding": {
                    "required": "If employees",
                    "registration": "EDD"
                }
            }
        }
    
    def get_annual_requirements(self) -> Dict[str, Any]:
        return {
            "statement_of_information": {
                "required": True,
                "frequency": "Biennial",
                "fee": 20.00,
                "filing_method": "Online or mail",
                "late_penalties": {
                    "amount": 250.00
                }
            },
            "franchise_tax": {
                "required": True,
                "minimum_amount": 800.00,
                "due_date": "15th day of 4th month",
                "first_year_exemption": False
            },
            "initial_report": {
                "required": True,
                "due_date": "90 days after formation",
                "fee": 20.00
            }
        }
    
    def get_publication_requirements(self) -> Optional[Dict[str, Any]]:
        return None  # California has no publication requirements
    
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
                "required": "Varies by locality",
                "issuing_agency": "City/County",
                "fee": "Varies",
                "renewal": "Annual"
            },
            "seller's_permit": {
                "required": "If selling tangible goods",
                "issuing_agency": "CDTFA",
                "fee": 0.00
            }
        }
