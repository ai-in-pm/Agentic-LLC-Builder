"""
New York state-specific requirements implementation.
"""

from typing import Dict, Any, List, Optional
from states.base_state import BaseState

class NewYork(BaseState):
    """New York state requirements implementation."""
    
    def _get_state_code(self) -> str:
        return "NY"
    
    def _get_state_name(self) -> str:
        return "New York"
    
    def get_formation_requirements(self) -> Dict[str, Any]:
        return {
            "filing_agency": "New York Department of State",
            "forms_required": ["Articles of Organization", "Operating Agreement"],
            "signature_requirements": {
                "authorized_signer": True,
                "notary_required": False
            },
            "minimum_members": 1,
            "requires_operating_agreement": True,
            "allows_series_llc": false,
            "allows_professional_llc": true,
            "foreign_qualification": {
                "required": True,
                "forms": ["Application for Certificate of Authority"]
            }
        }
    
    def get_filing_fees(self) -> Dict[str, float]:
        return {
            "formation": 200.0,
            "name_reservation": 20.0,
            "expedited": 50.0,
            "certified_copy": 25.00,
            "certificate_of_good_standing": 25.00,
            "foreign_qualification": 200.0
        }
    
    def get_processing_times(self) -> Dict[str, Any]:
        return {'standard': 7, 'expedited': 24, 'same_day': 1}
    
    def get_required_filings(self) -> List[Dict[str, Any]]:
        filings = [
            {
                "name": "Articles of Organization",
                "form_number": None,
                "frequency": "One-time",
                "fee": 200.0,
                "required": True
            }
        ]
        
        if True:
            filings.append({
                "name": "Annual Report",
                "form_number": None,
                "frequency": "Annual",
                "fee": 9.0,
                "required": True,
                "due_date": "Biennial anniversary month"
            })
        
        return filings
    
    def get_name_requirements(self) -> Dict[str, Any]:
        return {
            "required_terms": ['Limited Liability Company', 'LLC', 'L.L.C.', 'Ltd. Liability Co.', 'Ltd. Liability Company'],
            "prohibited_terms": ['Bank', 'Banking', 'Cooperative', 'Federal', 'National', 'Reserve', 'Trust', 'United States', 'Insurance', 'Insurer', 'Corporation', 'Corp.', 'Inc.', 'Incorporated'],
            "restricted_terms": {'Engineer': 'Board of Professional Engineers', 'Engineering': 'Board of Professional Engineers', 'Architect': 'Board of Architecture', 'Attorney': 'State Bar Association', 'Doctor': 'Medical Board', 'Hospital': 'Department of Health', 'Pharmacy': 'Board of Pharmacy', 'Real Estate': 'Real Estate Commission', 'Bank': 'Department of Financial Institutions', 'Trust': 'Department of Financial Institutions', 'University': 'Department of Education', 'College': 'Department of Education'},
            "reservation_available": True,
            "reservation_duration": 60,
            "reservation_fee": 20.0,
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
                "change_of_agent": 25.00,
                "change_of_address": 25.00
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
                "required": true,
                "minimum_amount": 25.0,
                "due_date": "Based on fiscal year",
                "filing_requirements": {
                    "online_filing": True
                }
            },
            "sales_tax": {
                "required": True,
                "registration": "Department of Revenue",
                "exemptions_available": True
            },
            "employer_taxes": {
                "unemployment": {
                    "required": "If employees",
                    "registration": "Department of Labor"
                },
                "withholding": {
                    "required": "If employees",
                    "registration": "Department of Revenue"
                }
            }
        }
    
    def get_annual_requirements(self) -> Dict[str, Any]:
        return {
            "annual_report": {
                "required": true,
                "due_date": "Biennial anniversary month",
                "fee": 9.0,
                "filing_method": "Online or mail",
                "late_penalties": {
                    "amount": 50.00
                }
            },
            "franchise_tax": {
                "required": true,
                "minimum_amount": 25.0,
                "due_date": "Based on fiscal year",
                "calculation_method": "Based on income/revenue"
            },
            "initial_report": {
                "required": False
            }
        }
    
    def get_publication_requirements(self) -> Optional[Dict[str, Any]]:
        return {'deadline': '120 days', 'duration': '6 weeks', 'estimated_cost': '1000.00'}
    
    def get_professional_license_requirements(self) -> Dict[str, Any]:
        return {
            "professional_llc": {
                "allowed": true,
                "regulated_professions": ['Accountant', 'Architect', 'Attorney', 'Chiropractor', 'Dentist', 'Engineer', 'Insurance Agent', 'Investment Advisor', 'Medical Doctor', 'Nurse', 'Optometrist', 'Pharmacist', 'Physical Therapist', 'Physician', 'Psychologist', 'Real Estate Agent', 'Veterinarian'],
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
                "issuing_agency": "Local government",
                "fee": "Varies",
                "renewal": "Annual"
            }
        }
