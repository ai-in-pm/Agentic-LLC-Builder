"""
Script to update state implementations with accurate data.
"""

import os
from pathlib import Path
from typing import Dict, Any
from states.state_data import (
    STATE_DATA,
    COMMON_PROHIBITED_TERMS,
    COMMON_RESTRICTED_TERMS,
    COMMON_REQUIRED_TERMS,
    REGULATED_PROFESSIONS
)

# State name mapping
STATE_NAMES = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}

def get_annual_report_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Get annual report data with proper defaults."""
    if isinstance(data.get('annual_report'), dict):
        return data['annual_report']
    return {
        'required': bool(data.get('annual_report')),
        'fee': 0.00,
        'due': ''
    }

def get_franchise_tax_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Get franchise tax data with proper defaults."""
    if isinstance(data.get('franchise_tax'), dict):
        tax_data = data['franchise_tax']
        return {
            'required': tax_data.get('required', False),
            'minimum': tax_data.get('minimum', 0.00)
        }
    return {
        'required': bool(data.get('franchise_tax')),
        'minimum': 0.00
    }

def generate_enhanced_state_class(state_code: str, state_name: str, data: Dict[str, Any]) -> str:
    """Generate enhanced state class implementation."""
    annual_report = get_annual_report_data(data)
    franchise_tax = get_franchise_tax_data(data)
    
    return f'''"""
{state_name} state-specific requirements implementation.
"""

from typing import Dict, Any, List, Optional
from states.base_state import BaseState

class {state_name.replace(" ", "")}(BaseState):
    """{state_name} state requirements implementation."""
    
    def _get_state_code(self) -> str:
        return "{state_code}"
    
    def _get_state_name(self) -> str:
        return "{state_name}"
    
    def get_formation_requirements(self) -> Dict[str, Any]:
        return {{
            "filing_agency": "{data['filing_agency']}",
            "forms_required": ["Articles of Organization", "Operating Agreement"],
            "signature_requirements": {{
                "authorized_signer": True,
                "notary_required": False
            }},
            "minimum_members": 1,
            "requires_operating_agreement": True,
            "allows_series_llc": {str(data.get('series_llc_allowed', False)).lower()},
            "allows_professional_llc": {str(data.get('professional_llc_allowed', True)).lower()},
            "foreign_qualification": {{
                "required": True,
                "forms": ["Application for Certificate of Authority"]
            }}
        }}
    
    def get_filing_fees(self) -> Dict[str, float]:
        return {{
            "formation": {data['formation_fee']},
            "name_reservation": {data['name_reservation_fee']},
            "expedited": {data['processing_time'].get('expedited_fee', 50.00)},
            "certified_copy": 25.00,
            "certificate_of_good_standing": 25.00,
            "foreign_qualification": {data['formation_fee']}
        }}
    
    def get_processing_times(self) -> Dict[str, Any]:
        return {data['processing_time']}
    
    def get_required_filings(self) -> List[Dict[str, Any]]:
        filings = [
            {{
                "name": "Articles of Organization",
                "form_number": None,
                "frequency": "One-time",
                "fee": {data['formation_fee']},
                "required": True
            }}
        ]
        
        if {annual_report['required']}:
            filings.append({{
                "name": "Annual Report",
                "form_number": None,
                "frequency": "Annual",
                "fee": {annual_report['fee']},
                "required": True,
                "due_date": "{annual_report['due']}"
            }})
        
        return filings
    
    def get_name_requirements(self) -> Dict[str, Any]:
        return {{
            "required_terms": {COMMON_REQUIRED_TERMS},
            "prohibited_terms": {COMMON_PROHIBITED_TERMS},
            "restricted_terms": {COMMON_RESTRICTED_TERMS},
            "reservation_available": True,
            "reservation_duration": {data['name_reservation_duration']},
            "reservation_fee": {data['name_reservation_fee']},
            "reservation_renewable": True,
            "distinguishable": True
        }}
    
    def get_registered_agent_requirements(self) -> Dict[str, Any]:
        return {{
            "required": True,
            "state_residency_required": True,
            "business_hours": "9am-5pm",
            "commercial_allowed": True,
            "entity_as_agent": True,
            "office_requirements": {{
                "physical_address": True,
                "po_box_allowed": False,
                "business_hours": True
            }},
            "filing_required": {{
                "change_of_agent": True,
                "change_of_address": True
            }},
            "fees": {{
                "change_of_agent": 25.00,
                "change_of_address": 25.00
            }}
        }}
    
    def get_tax_requirements(self) -> Dict[str, Any]:
        return {{
            "income_tax": {{
                "required": False,
                "type": "Pass-through",
                "exceptions": None
            }},
            "franchise_tax": {{
                "required": {str(franchise_tax['required']).lower()},
                "minimum_amount": {franchise_tax['minimum']},
                "due_date": "Based on fiscal year",
                "filing_requirements": {{
                    "online_filing": True
                }}
            }},
            "sales_tax": {{
                "required": True,
                "registration": "Department of Revenue",
                "exemptions_available": True
            }},
            "employer_taxes": {{
                "unemployment": {{
                    "required": "If employees",
                    "registration": "Department of Labor"
                }},
                "withholding": {{
                    "required": "If employees",
                    "registration": "Department of Revenue"
                }}
            }}
        }}
    
    def get_annual_requirements(self) -> Dict[str, Any]:
        return {{
            "annual_report": {{
                "required": {str(annual_report['required']).lower()},
                "due_date": "{annual_report['due']}",
                "fee": {annual_report['fee']},
                "filing_method": "Online or mail",
                "late_penalties": {{
                    "amount": 50.00
                }}
            }},
            "franchise_tax": {{
                "required": {str(franchise_tax['required']).lower()},
                "minimum_amount": {franchise_tax['minimum']},
                "due_date": "Based on fiscal year",
                "calculation_method": "Based on income/revenue"
            }},
            "initial_report": {{
                "required": False
            }}
        }}
    
    def get_publication_requirements(self) -> Optional[Dict[str, Any]]:
        {'return ' + str(data.get('publication_requirements', 'None')) if data.get('publication_required') else 'return None'}
    
    def get_professional_license_requirements(self) -> Dict[str, Any]:
        return {{
            "professional_llc": {{
                "allowed": {str(data.get('professional_llc_allowed', True)).lower()},
                "regulated_professions": {REGULATED_PROFESSIONS},
                "ownership_restrictions": {{
                    "professional_requirements": True,
                    "licensing_requirements": True
                }},
                "name_requirements": {{
                    "professional_designation": True,
                    "licensing_board_approval": True
                }}
            }},
            "general_business_license": {{
                "required": "Varies by locality",
                "issuing_agency": "Local government",
                "fee": "Varies",
                "renewal": "Annual"
            }}
        }}
'''

def main():
    """Update state implementations with enhanced data."""
    # Get the root directory
    root_dir = Path(__file__).parent.parent
    states_dir = root_dir / "states"
    
    # Update state implementations
    for state_code, data in STATE_DATA.items():
        state_dir = states_dir / state_code.lower()
        state_name = STATE_NAMES[state_code]
        
        # Create state implementation file
        with open(state_dir / "state.py", "w") as f:
            f.write(generate_enhanced_state_class(state_code, state_name, data))
        
        print(f"Updated implementation for {state_name}")

if __name__ == "__main__":
    main()
