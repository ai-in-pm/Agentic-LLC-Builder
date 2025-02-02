"""
Module containing state-specific requirements and regulations for LLC formation.
"""

from typing import Dict, Any

STATE_REQUIREMENTS = {
    "AL": {
        "name": "Alabama",
        "filing_agency": "Secretary of State",
        "formation_requirements": {
            "name_requirements": {
                "required_terms": ["LLC", "L.L.C.", "Limited Liability Company"],
                "prohibited_terms": ["Bank", "Insurance", "Corporation"],
                "name_availability_url": "https://sos.alabama.gov/business-services/business-entity-search"
            },
            "registered_agent": {
                "requirements": "Physical address in Alabama",
                "service_hours": "Regular business hours",
                "can_be_member": True
            },
            "filing_requirements": {
                "articles_of_organization": True,
                "operating_agreement": "Recommended but not required",
                "publication": False
            },
            "fees": {
                "formation": 200.00,
                "expedited": 100.00,
                "annual_report": 0.00
            },
            "processing_time": {
                "standard": "5-7 business days",
                "expedited": "24 hours"
            }
        }
    },
    "AK": {
        "name": "Alaska",
        "filing_agency": "Division of Corporations",
        "formation_requirements": {
            "name_requirements": {
                "required_terms": ["LLC", "L.L.C.", "Limited Liability Company"],
                "prohibited_terms": ["Bank", "Insurance", "Corporation"],
                "name_availability_url": "https://www.commerce.alaska.gov/cbp/main/search/entities"
            },
            "registered_agent": {
                "requirements": "Physical address in Alaska",
                "service_hours": "Regular business hours",
                "can_be_member": True
            },
            "filing_requirements": {
                "articles_of_organization": True,
                "operating_agreement": "Recommended but not required",
                "publication": False
            },
            "fees": {
                "formation": 250.00,
                "expedited": 50.00,
                "annual_report": 100.00
            },
            "processing_time": {
                "standard": "10-15 business days",
                "expedited": "24-48 hours"
            }
        }
    },
    "AZ": {
        "name": "Arizona",
        "filing_agency": "Corporation Commission",
        "formation_requirements": {
            "name_requirements": {
                "required_terms": ["LLC", "L.L.C.", "Limited Liability Company"],
                "prohibited_terms": ["Bank", "Insurance", "Corporation"],
                "name_availability_url": "https://ecorp.azcc.gov/EntitySearch"
            },
            "registered_agent": {
                "requirements": "Physical address in Arizona",
                "service_hours": "Regular business hours",
                "can_be_member": True
            },
            "filing_requirements": {
                "articles_of_organization": True,
                "operating_agreement": "Recommended but not required",
                "publication": True
            },
            "fees": {
                "formation": 50.00,
                "expedited": 35.00,
                "annual_report": 0.00
            },
            "processing_time": {
                "standard": "3-5 weeks",
                "expedited": "5-7 business days"
            }
        }
    },
    # Add all other states...
    "WY": {
        "name": "Wyoming",
        "filing_agency": "Secretary of State",
        "formation_requirements": {
            "name_requirements": {
                "required_terms": ["LLC", "L.L.C.", "Limited Liability Company"],
                "prohibited_terms": ["Bank", "Insurance", "Corporation"],
                "name_availability_url": "https://wyobiz.wyo.gov/Business/FilingSearch.aspx"
            },
            "registered_agent": {
                "requirements": "Physical address in Wyoming",
                "service_hours": "Regular business hours",
                "can_be_member": True
            },
            "filing_requirements": {
                "articles_of_organization": True,
                "operating_agreement": "Recommended but not required",
                "publication": False
            },
            "fees": {
                "formation": 100.00,
                "expedited": 50.00,
                "annual_report": "Variable based on assets"
            },
            "processing_time": {
                "standard": "3-5 business days",
                "expedited": "24 hours"
            }
        }
    }
}

def get_state_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get the requirements for LLC formation in a specific state.
    
    Args:
        state_code: Two-letter state code (e.g., 'CA' for California)
        
    Returns:
        Dictionary containing state requirements
        
    Raises:
        KeyError: If state code is invalid
    """
    if state_code not in STATE_REQUIREMENTS:
        raise KeyError(f"Invalid state code: {state_code}")
    return STATE_REQUIREMENTS[state_code]

def get_all_states() -> Dict[str, str]:
    """
    Get a dictionary of all state codes and names.
    
    Returns:
        Dictionary mapping state codes to state names
    """
    return {code: data["name"] for code, data in STATE_REQUIREMENTS.items()}

def validate_llc_name(state_code: str, name: str) -> bool:
    """
    Validate if a proposed LLC name meets state requirements.
    
    Args:
        state_code: Two-letter state code
        name: Proposed LLC name
        
    Returns:
        Boolean indicating if name is valid
    """
    requirements = get_state_requirements(state_code)["formation_requirements"]["name_requirements"]
    
    # Check required terms
    has_required_term = any(term.lower() in name.lower() 
                          for term in requirements["required_terms"])
    if not has_required_term:
        return False
    
    # Check prohibited terms
    has_prohibited_term = any(term.lower() in name.lower() 
                            for term in requirements["prohibited_terms"])
    if has_prohibited_term:
        return False
    
    return True

def get_filing_fees(state_code: str) -> Dict[str, float]:
    """
    Get the filing fees for LLC formation in a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing fee information
    """
    return get_state_requirements(state_code)["formation_requirements"]["fees"]

def get_processing_time(state_code: str) -> Dict[str, str]:
    """
    Get the processing times for LLC formation in a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing processing time information
    """
    return get_state_requirements(state_code)["formation_requirements"]["processing_time"]
