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
            "filing_agency": "Delaware Department of State",
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
                "forms": ["Certificate of Authority"]
            }
        }
    
    def get_filing_fees(self) -> Dict[str, float]:
        return {
            "formation": 90.00,
            "name_reservation": 0.00,
            "expedited": 50.00,
            "certified_copy": 0.00,
            "certificate_of_good_standing": 0.00,
            "foreign_qualification": 0.00
        }
    
    def get_processing_times(self) -> Dict[str, Any]:
        return {
            "standard": 10,
            "expedited": 1
        }
    
    def get_required_filings(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "Annual Report",
                "deadline": "March 1",
                "fee": 300.00,
                "description": "Annual report and franchise tax payment"
            }
        ]
    
    def get_name_requirements(self) -> Dict[str, Any]:
        return {
            "required_terms": ["LLC", "L.L.C.", "Limited Liability Company"],
            "prohibited_terms": [],
            "restricted_terms": {},
            "reservation_available": True,
            "reservation_duration": 120,
            "reservation_fee": 0.00,
            "reservation_renewable": True,
            "distinguishable": True
        }
    
    def get_registered_agent_requirements(self) -> Dict[str, Any]:
        return {
            "required": True,
            "state_residency_required": False,
            "business_hours": "Normal business hours",
            "commercial_allowed": True,
            "entity_as_agent": True,
            "office_requirements": {
                "physical_address": True,
                "po_box_allowed": False,
                "business_hours": True
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
                "due_date": "March 1",
                "filing_requirements": {}
            },
            "sales_tax": {
                "required": False,
                "rate": 0.00,
                "exemptions_available": True
            }
        }
    
    def get_annual_requirements(self) -> Dict[str, Any]:
        return {
            "annual_report": {
                "required": True,
                "due_date": "March 1",
                "fee": 300.00,
                "filing_method": "",
                "late_penalties": {}
            },
            "franchise_tax": {
                "required": True,
                "amount": 300.00,
                "due_date": "March 1",
                "calculation_method": ""
            },
            "initial_report": {
                "required": False
            }
        }
    
    def get_publication_requirements(self) -> Optional[Dict[str, Any]]:
        return None
    
    def get_professional_license_requirements(self) -> Dict[str, Any]:
        return {
            "professional_llc": {
                "allowed": True,
                "regulated_professions": [],
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
                "required": False,
                "issuing_agency": "",
                "fee": 0.00,
                "renewal": ""
            }
        }
