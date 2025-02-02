"""
Module containing state-specific tax requirements for LLCs.
"""

from typing import Dict, Any, List

STATE_TAX_REQUIREMENTS = {
    "AL": {
        "name": "Alabama",
        "tax_structure": {
            "business_privilege_tax": {
                "required": True,
                "based_on": "Net worth",
                "minimum": 100.00,
                "maximum": 15000.00,
                "due_date": "March 15"
            },
            "income_tax": {
                "required": False,
                "note": "Pass-through to members"
            },
            "sales_tax": {
                "required": "If selling tangible goods",
                "base_rate": 0.04,
                "local_rates": "Vary by locality"
            }
        },
        "filing_requirements": {
            "annual_report": False,
            "tax_returns": ["Business Privilege Tax Return"],
            "due_dates": {
                "business_privilege_tax": "March 15",
                "sales_tax": "20th of following month"
            }
        }
    },
    "AK": {
        "name": "Alaska",
        "tax_structure": {
            "income_tax": {
                "required": False,
                "note": "Pass-through to members"
            },
            "sales_tax": {
                "required": False,
                "note": "No state sales tax, local taxes may apply"
            }
        },
        "filing_requirements": {
            "annual_report": {
                "required": True,
                "due_date": "January 2",
                "fee": 100.00
            }
        }
    },
    # Add all other states...
    "WY": {
        "name": "Wyoming",
        "tax_structure": {
            "income_tax": {
                "required": False,
                "note": "No state income tax"
            },
            "sales_tax": {
                "required": "If selling tangible goods",
                "base_rate": 0.04,
                "local_rates": "Vary by locality"
            },
            "annual_report": {
                "required": True,
                "fee": "Based on assets in Wyoming",
                "minimum": 50.00,
                "due_date": "First day of anniversary month"
            }
        },
        "filing_requirements": {
            "annual_report": True,
            "license_renewal": "Annual"
        }
    }
}

def get_state_tax_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get tax requirements for a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing state tax requirements
    """
    if state_code not in STATE_TAX_REQUIREMENTS:
        raise KeyError(f"Invalid state code: {state_code}")
    return STATE_TAX_REQUIREMENTS[state_code]

def get_filing_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get filing requirements for a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing filing requirements
    """
    return get_state_tax_requirements(state_code)["filing_requirements"]

def get_tax_structure(state_code: str) -> Dict[str, Any]:
    """
    Get tax structure for a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing tax structure
    """
    return get_state_tax_requirements(state_code)["tax_structure"]

def get_annual_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get annual requirements for maintaining LLC in a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing annual requirements
    """
    requirements = {}
    state_reqs = get_state_tax_requirements(state_code)
    
    # Check annual report requirements
    if "annual_report" in state_reqs["filing_requirements"]:
        requirements["annual_report"] = state_reqs["filing_requirements"]["annual_report"]
    
    # Check tax filing requirements
    if "tax_returns" in state_reqs["filing_requirements"]:
        requirements["tax_returns"] = state_reqs["filing_requirements"]["tax_returns"]
    
    # Check due dates
    if "due_dates" in state_reqs["filing_requirements"]:
        requirements["due_dates"] = state_reqs["filing_requirements"]["due_dates"]
    
    return requirements

def get_sales_tax_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get sales tax requirements for a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing sales tax requirements
    """
    tax_structure = get_tax_structure(state_code)
    if "sales_tax" in tax_structure:
        return tax_structure["sales_tax"]
    return {"required": False, "note": "No sales tax requirements"}

def get_income_tax_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get income tax requirements for a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing income tax requirements
    """
    tax_structure = get_tax_structure(state_code)
    if "income_tax" in tax_structure:
        return tax_structure["income_tax"]
    return {"required": False, "note": "No specific income tax requirements"}
