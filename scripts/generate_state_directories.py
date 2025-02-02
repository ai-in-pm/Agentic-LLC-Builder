"""
Script to generate directory structure for all 50 states.
"""

import os
from pathlib import Path

# Define all 50 states with their codes and names
STATES = {
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

def generate_state_class(state_code: str, state_name: str) -> str:
    """Generate state class implementation."""
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
            "filing_agency": "",  # TODO: Add filing agency
            "forms_required": [],  # TODO: Add required forms
            "signature_requirements": {{
                "authorized_signer": True,
                "notary_required": False  # TODO: Update notary requirements
            }},
            "minimum_members": 1,
            "requires_operating_agreement": False,  # TODO: Update requirement
            "allows_series_llc": False,  # TODO: Update allowance
            "allows_professional_llc": True,  # TODO: Update allowance
            "foreign_qualification": {{
                "required": True,
                "forms": []  # TODO: Add required forms
            }}
        }}
    
    def get_filing_fees(self) -> Dict[str, float]:
        return {{
            "formation": 0.00,  # TODO: Add formation fee
            "name_reservation": 0.00,  # TODO: Add reservation fee
            "expedited": 0.00,  # TODO: Add expedited fee
            "certified_copy": 0.00,  # TODO: Add certified copy fee
            "certificate_of_good_standing": 0.00,  # TODO: Add good standing fee
            "foreign_qualification": 0.00  # TODO: Add foreign qualification fee
        }}
    
    def get_processing_times(self) -> Dict[str, Any]:
        return {{
            "standard": 0,  # TODO: Add standard processing time
            "expedited": 0  # TODO: Add expedited processing time
        }}
    
    def get_required_filings(self) -> List[Dict[str, Any]]:
        return []  # TODO: Add required filings
    
    def get_name_requirements(self) -> Dict[str, Any]:
        return {{
            "required_terms": [],  # TODO: Add required terms
            "prohibited_terms": [],  # TODO: Add prohibited terms
            "restricted_terms": {{}},  # TODO: Add restricted terms
            "reservation_available": True,  # TODO: Update availability
            "reservation_duration": 0,  # TODO: Add duration
            "reservation_fee": 0.00,  # TODO: Add fee
            "reservation_renewable": True,  # TODO: Update renewable status
            "distinguishable": True  # TODO: Update distinguishable requirement
        }}
    
    def get_registered_agent_requirements(self) -> Dict[str, Any]:
        return {{
            "required": True,
            "state_residency_required": True,  # TODO: Update requirement
            "business_hours": "Normal business hours",
            "commercial_allowed": True,  # TODO: Update allowance
            "entity_as_agent": True,  # TODO: Update allowance
            "office_requirements": {{
                "physical_address": True,
                "po_box_allowed": False,
                "business_hours": True
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
                "required": False,  # TODO: Update requirement
                "amount": 0.00,  # TODO: Add amount
                "due_date": "",  # TODO: Add due date
                "filing_requirements": {{}}  # TODO: Add filing requirements
            }},
            "sales_tax": {{
                "required": True,  # TODO: Update requirement
                "rate": 0.00,  # TODO: Add rate
                "exemptions_available": True
            }}
        }}
    
    def get_annual_requirements(self) -> Dict[str, Any]:
        return {{
            "annual_report": {{
                "required": False,  # TODO: Update requirement
                "due_date": "",  # TODO: Add due date
                "fee": 0.00,  # TODO: Add fee
                "filing_method": "",  # TODO: Add filing method
                "late_penalties": {{}}  # TODO: Add penalties
            }},
            "franchise_tax": {{
                "required": False,  # TODO: Update requirement
                "amount": 0.00,  # TODO: Add amount
                "due_date": "",  # TODO: Add due date
                "calculation_method": ""  # TODO: Add calculation method
            }},
            "initial_report": {{
                "required": False  # TODO: Update requirement
            }}
        }}
    
    def get_publication_requirements(self) -> Optional[Dict[str, Any]]:
        return None  # TODO: Update if publication is required
    
    def get_professional_license_requirements(self) -> Dict[str, Any]:
        return {{
            "professional_llc": {{
                "allowed": True,  # TODO: Update allowance
                "regulated_professions": [],  # TODO: Add regulated professions
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
                "required": False,  # TODO: Update requirement
                "issuing_agency": "",  # TODO: Add agency
                "fee": 0.00,  # TODO: Add fee
                "renewal": ""  # TODO: Add renewal period
            }}
        }}
'''

def generate_init_file() -> str:
    """Generate __init__.py content."""
    return '"""State module initialization."""\n'

def main():
    """Generate state directory structure."""
    # Get the root directory
    root_dir = Path(__file__).parent.parent
    states_dir = root_dir / "states"
    
    # Create states directory if it doesn't exist
    states_dir.mkdir(exist_ok=True)
    
    # Create base __init__.py
    with open(states_dir / "__init__.py", "w") as f:
        f.write(generate_init_file())
    
    # Create directories and files for each state
    for state_code, state_name in STATES.items():
        # Create state directory
        state_dir = states_dir / state_code.lower()
        state_dir.mkdir(exist_ok=True)
        
        # Create state __init__.py
        with open(state_dir / "__init__.py", "w") as f:
            f.write(generate_init_file())
        
        # Create state implementation file
        with open(state_dir / "state.py", "w") as f:
            f.write(generate_state_class(state_code, state_name))
        
        print(f"Generated files for {state_name}")

if __name__ == "__main__":
    main()
