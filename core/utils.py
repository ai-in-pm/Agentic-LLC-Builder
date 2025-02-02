"""
Utility functions for the LLC Builder application.
"""

import os
import re
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

def validate_business_name(name: str, state_code: str) -> Dict[str, Any]:
    """
    Validate a business name against state-specific requirements.
    
    Args:
        name: Proposed business name
        state_code: Two-letter state code
        
    Returns:
        Dictionary containing validation results
    """
    from core.state_requirements import get_state_requirements
    
    requirements = get_state_requirements(state_code)
    name_reqs = requirements["formation_requirements"]["name_requirements"]
    
    results = {
        "valid": True,
        "issues": []
    }
    
    # Check required terms
    has_required = any(term.lower() in name.lower() for term in name_reqs["required_terms"])
    if not has_required:
        results["valid"] = False
        results["issues"].append(f"Name must contain one of: {', '.join(name_reqs['required_terms'])}")
    
    # Check prohibited terms
    has_prohibited = any(term.lower() in name.lower() for term in name_reqs["prohibited_terms"])
    if has_prohibited:
        results["valid"] = False
        results["issues"].append(f"Name contains prohibited term from: {', '.join(name_reqs['prohibited_terms'])}")
    
    return results

def generate_document_from_template(template_path: str, context: Dict[str, Any]) -> str:
    """
    Generate a document from a template using the provided context.
    
    Args:
        template_path: Path to template file
        context: Dictionary containing template variables
        
    Returns:
        Generated document content
    """
    import chevron
    
    with open(template_path, 'r') as f:
        template = f.read()
    
    return chevron.render(template, context)

def calculate_fees(state_code: str, services: List[str]) -> Dict[str, float]:
    """
    Calculate fees for LLC formation services.
    
    Args:
        state_code: Two-letter state code
        services: List of requested services
        
    Returns:
        Dictionary containing fee breakdown
    """
    from core.state_requirements import get_state_requirements
    
    requirements = get_state_requirements(state_code)
    fees = requirements["formation_requirements"]["fees"]
    
    total_fees = {
        "formation": fees["formation"],
        "expedited": fees.get("expedited", 0.0) if "expedited" in services else 0.0,
        "registered_agent": 0.0,  # Add if using service
        "additional_services": 0.0
    }
    
    total_fees["total"] = sum(total_fees.values())
    return total_fees

def generate_filing_checklist(state_code: str, business_type: str) -> List[Dict[str, Any]]:
    """
    Generate a checklist of required filings.
    
    Args:
        state_code: Two-letter state code
        business_type: Type of business (e.g., 'profit', 'non-profit')
        
    Returns:
        List of required filings and their details
    """
    from core.state_requirements import get_state_requirements
    from core.state_compliance import get_initial_requirements
    
    requirements = get_state_requirements(state_code)
    compliance = get_initial_requirements(state_code)
    
    checklist = []
    
    # Add formation documents
    if requirements["formation_requirements"]["articles_of_organization"]:
        checklist.append({
            "item": "Articles of Organization",
            "required": True,
            "deadline": "Before operations",
            "notes": "Must be filed with Secretary of State"
        })
    
    # Add compliance requirements
    for req_type, details in compliance.items():
        if details["required"] is True or (isinstance(details["required"], str) and details["required"] != "Varies"):
            checklist.append({
                "item": req_type.replace("_", " ").title(),
                "required": True,
                "deadline": "Before operations",
                "notes": f"File with {details.get('agency', 'appropriate agency')}"
            })
    
    return checklist

def format_address(address: Dict[str, str]) -> str:
    """
    Format an address dictionary into a string.
    
    Args:
        address: Dictionary containing address components
        
    Returns:
        Formatted address string
    """
    components = [
        address.get("street1", ""),
        address.get("street2", ""),
        f"{address.get('city', '')}, {address.get('state', '')} {address.get('zip', '')}"
    ]
    return "\n".join(filter(None, components))

def validate_ein(ein: str) -> bool:
    """
    Validate an Employer Identification Number format.
    
    Args:
        ein: EIN to validate
        
    Returns:
        Boolean indicating if EIN is valid
    """
    # Remove any hyphens and spaces
    ein = re.sub(r'[\s-]', '', ein)
    
    # Check if EIN is 9 digits
    if not ein.isdigit() or len(ein) != 9:
        return False
    
    # Check if first two digits are valid
    valid_prefixes = {'10', '12', '60', '67', '50', '53'} | set(f"{i:02d}" for i in range(1, 95))
    if ein[:2] not in valid_prefixes:
        return False
    
    return True

def generate_file_name(template: str, context: Dict[str, Any]) -> str:
    """
    Generate a file name for a document.
    
    Args:
        template: Template for file name
        context: Dictionary containing variables
        
    Returns:
        Generated file name
    """
    # Replace spaces with underscores and remove special characters
    name = template.format(**context)
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '_', name)
    
    return name.lower()

def save_document(content: str, directory: str, filename: str) -> str:
    """
    Save a generated document to file.
    
    Args:
        content: Document content
        directory: Directory to save in
        filename: Name of file
        
    Returns:
        Path to saved file
    """
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    return filepath

def load_template(template_name: str, business_type: str = "profit") -> str:
    """
    Load a template file.
    
    Args:
        template_name: Name of template
        business_type: Type of business
        
    Returns:
        Template content
    """
    template_dir = Path(__file__).parent.parent / "templates"
    template_path = template_dir / business_type / f"{template_name}.md"
    
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    
    with open(template_path, 'r') as f:
        return f.read()

def validate_date(date_str: str, format: str = "%Y-%m-%d") -> bool:
    """
    Validate a date string.
    
    Args:
        date_str: Date string to validate
        format: Expected date format
        
    Returns:
        Boolean indicating if date is valid
    """
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False

def format_currency(amount: float) -> str:
    """
    Format a currency amount.
    
    Args:
        amount: Amount to format
        
    Returns:
        Formatted currency string
    """
    return "${:,.2f}".format(amount)

def validate_phone(phone: str) -> bool:
    """
    Validate a phone number.
    
    Args:
        phone: Phone number to validate
        
    Returns:
        Boolean indicating if phone number is valid
    """
    # Remove any non-digit characters
    phone = re.sub(r'\D', '', phone)
    
    # Check if phone is 10 digits
    return len(phone) == 10 and phone.isdigit()

def validate_email(email: str) -> bool:
    """
    Validate an email address.
    
    Args:
        email: Email address to validate
        
    Returns:
        Boolean indicating if email is valid
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def load_state_data() -> Dict[str, Dict[str, Any]]:
    """
    Load state-specific data from all modules.
    
    Returns:
        Combined dictionary of state data
    """
    from core.state_requirements import STATE_REQUIREMENTS
    from core.state_tax_requirements import STATE_TAX_REQUIREMENTS
    from core.state_compliance import STATE_COMPLIANCE_REQUIREMENTS
    
    state_data = {}
    
    for state_code in STATE_REQUIREMENTS:
        state_data[state_code] = {
            "requirements": STATE_REQUIREMENTS[state_code],
            "tax": STATE_TAX_REQUIREMENTS[state_code],
            "compliance": STATE_COMPLIANCE_REQUIREMENTS[state_code]
        }
    
    return state_data
