"""
Module containing state-specific compliance requirements for LLCs.
"""

from typing import Dict, Any, List
from datetime import datetime

STATE_COMPLIANCE_REQUIREMENTS = {
    "AL": {
        "name": "Alabama",
        "initial_requirements": {
            "business_license": {
                "required": True,
                "issuing_agency": "County Probate Office",
                "renewal": "Annual"
            },
            "professional_license": {
                "required": "Varies by industry",
                "agency": "Professional Licensing Board"
            },
            "tax_registration": {
                "required": True,
                "agency": "Department of Revenue"
            }
        },
        "ongoing_requirements": {
            "annual_report": {
                "required": False
            },
            "business_privilege_tax": {
                "required": True,
                "due_date": "March 15",
                "minimum_fee": 100.00
            },
            "license_renewal": {
                "frequency": "Annual",
                "due_date": "Based on issue date"
            }
        },
        "employment_requirements": {
            "workers_comp": {
                "required": "If 5+ employees",
                "agency": "Department of Labor"
            },
            "unemployment_insurance": {
                "required": "If employees",
                "agency": "Department of Labor"
            }
        }
    },
    "AK": {
        "name": "Alaska",
        "initial_requirements": {
            "business_license": {
                "required": True,
                "issuing_agency": "Department of Commerce",
                "renewal": "Biennial"
            },
            "professional_license": {
                "required": "Varies by industry",
                "agency": "Professional Licensing Division"
            }
        },
        "ongoing_requirements": {
            "annual_report": {
                "required": True,
                "due_date": "January 2",
                "fee": 100.00
            },
            "biennial_license": {
                "required": True,
                "fee": 50.00
            }
        },
        "employment_requirements": {
            "workers_comp": {
                "required": "All employers",
                "exemptions": ["Sole proprietors", "Partners"]
            }
        }
    },
    # Add all other states...
    "WY": {
        "name": "Wyoming",
        "initial_requirements": {
            "business_license": {
                "required": "Varies by locality",
                "issuing_agency": "Local government"
            },
            "sales_tax_license": {
                "required": "If selling tangible goods",
                "agency": "Department of Revenue"
            }
        },
        "ongoing_requirements": {
            "annual_report": {
                "required": True,
                "due_date": "First day of anniversary month",
                "fee": "Based on assets"
            }
        },
        "employment_requirements": {
            "workers_comp": {
                "required": "All employers",
                "agency": "Department of Workforce Services"
            },
            "unemployment_insurance": {
                "required": "If employees",
                "agency": "Department of Workforce Services"
            }
        }
    }
}

def get_state_compliance_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get compliance requirements for a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing state compliance requirements
    """
    if state_code not in STATE_COMPLIANCE_REQUIREMENTS:
        raise KeyError(f"Invalid state code: {state_code}")
    return STATE_COMPLIANCE_REQUIREMENTS[state_code]

def get_initial_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get initial compliance requirements for a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing initial requirements
    """
    return get_state_compliance_requirements(state_code)["initial_requirements"]

def get_ongoing_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get ongoing compliance requirements for a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing ongoing requirements
    """
    return get_state_compliance_requirements(state_code)["ongoing_requirements"]

def get_employment_requirements(state_code: str) -> Dict[str, Any]:
    """
    Get employment-related compliance requirements for a specific state.
    
    Args:
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing employment requirements
    """
    return get_state_compliance_requirements(state_code)["employment_requirements"]

def get_upcoming_deadlines(state_code: str, formation_date: datetime) -> List[Dict[str, Any]]:
    """
    Get upcoming compliance deadlines for an LLC.
    
    Args:
        state_code: Two-letter state code
        formation_date: Date LLC was formed
        
    Returns:
        List of upcoming deadlines and requirements
    """
    requirements = get_ongoing_requirements(state_code)
    deadlines = []
    
    # Check annual report deadline
    if "annual_report" in requirements and requirements["annual_report"]["required"]:
        deadlines.append({
            "type": "Annual Report",
            "due_date": requirements["annual_report"]["due_date"],
            "fee": requirements["annual_report"].get("fee", "Varies")
        })
    
    # Check license renewal deadlines
    if "license_renewal" in requirements:
        deadlines.append({
            "type": "License Renewal",
            "frequency": requirements["license_renewal"]["frequency"],
            "due_date": requirements["license_renewal"].get("due_date", "Varies")
        })
    
    return deadlines

def validate_compliance(state_code: str, business_details: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate if a business meets compliance requirements.
    
    Args:
        state_code: Two-letter state code
        business_details: Dictionary containing business information
        
    Returns:
        Dictionary containing compliance status and any issues
    """
    requirements = get_state_compliance_requirements(state_code)
    issues = []
    
    # Check initial requirements
    for req_type, req_details in requirements["initial_requirements"].items():
        if req_details["required"] is True and req_type not in business_details.get("completed_requirements", []):
            issues.append(f"Missing {req_type}")
    
    # Check ongoing requirements
    for req_type, req_details in requirements["ongoing_requirements"].items():
        if req_details["required"] is True and req_type not in business_details.get("maintained_requirements", []):
            issues.append(f"Non-compliant with {req_type}")
    
    # Check employment requirements if applicable
    if business_details.get("has_employees", False):
        for req_type, req_details in requirements["employment_requirements"].items():
            if req_details["required"] == "All employers" and req_type not in business_details.get("employment_compliance", []):
                issues.append(f"Missing {req_type}")
    
    return {
        "compliant": len(issues) == 0,
        "issues": issues
    }
