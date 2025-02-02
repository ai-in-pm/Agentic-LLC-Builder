"""
Module for validating business information and requirements.
"""

from typing import Dict, Any, List, Optional
from core.utils import (
    validate_business_name,
    validate_ein,
    validate_phone,
    validate_email,
    validate_date
)

class BusinessValidator:
    """Class for validating business information and requirements."""
    
    @staticmethod
    def validate_business_details(details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate all business details.
        
        Args:
            details: Dictionary containing business information
            
        Returns:
            Dictionary containing validation results
        """
        results = {
            "valid": True,
            "issues": []
        }
        
        # Validate required fields
        required_fields = [
            "business_name",
            "state",
            "organization_type",
            "management_type",
            "registered_agent",
            "principal_office_address"
        ]
        
        for field in required_fields:
            if field not in details or not details[field]:
                results["valid"] = False
                results["issues"].append(f"Missing required field: {field}")
        
        if not results["valid"]:
            return results
        
        # Validate business name
        name_validation = validate_business_name(
            details["business_name"],
            details["state"]
        )
        if not name_validation["valid"]:
            results["valid"] = False
            results["issues"].extend(name_validation["issues"])
        
        # Validate EIN if provided
        if "ein" in details and details["ein"]:
            if not validate_ein(details["ein"]):
                results["valid"] = False
                results["issues"].append("Invalid EIN format")
        
        # Validate contact information
        results.update(BusinessValidator.validate_contact_info(details))
        
        # Validate members and management
        results.update(BusinessValidator.validate_management_structure(details))
        
        # Validate addresses
        results.update(BusinessValidator.validate_addresses(details))
        
        # Validate organization-specific requirements
        if details["organization_type"] == "non-profit":
            results.update(BusinessValidator.validate_nonprofit_requirements(details))
        
        return results
    
    @staticmethod
    def validate_contact_info(details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate contact information.
        
        Args:
            details: Dictionary containing business information
            
        Returns:
            Dictionary containing validation results
        """
        results = {
            "valid": True,
            "issues": []
        }
        
        # Validate phone numbers
        if "phone" in details and details["phone"]:
            if not validate_phone(details["phone"]):
                results["valid"] = False
                results["issues"].append("Invalid phone number format")
        
        # Validate email addresses
        if "email" in details and details["email"]:
            if not validate_email(details["email"]):
                results["valid"] = False
                results["issues"].append("Invalid email format")
        
        # Validate registered agent contact info
        agent = details.get("registered_agent", {})
        if agent:
            if "phone" in agent and agent["phone"]:
                if not validate_phone(agent["phone"]):
                    results["valid"] = False
                    results["issues"].append("Invalid registered agent phone number")
            
            if "email" in agent and agent["email"]:
                if not validate_email(agent["email"]):
                    results["valid"] = False
                    results["issues"].append("Invalid registered agent email")
        
        return results
    
    @staticmethod
    def validate_management_structure(details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate management structure and members.
        
        Args:
            details: Dictionary containing business information
            
        Returns:
            Dictionary containing validation results
        """
        results = {
            "valid": True,
            "issues": []
        }
        
        # Validate management type
        valid_types = ["member", "manager"]
        if details["management_type"] not in valid_types:
            results["valid"] = False
            results["issues"].append(f"Invalid management type. Must be one of: {', '.join(valid_types)}")
        
        # Validate members
        members = details.get("members", [])
        if not members:
            results["valid"] = False
            results["issues"].append("At least one member is required")
        else:
            ownership_total = sum(member.get("ownership_percentage", 0) for member in members)
            if abs(ownership_total - 100) > 0.01:  # Allow for small floating-point differences
                results["valid"] = False
                results["issues"].append("Total ownership percentage must equal 100%")
            
            # Validate member details
            for i, member in enumerate(members):
                if "name" not in member or not member["name"]:
                    results["valid"] = False
                    results["issues"].append(f"Member {i+1} missing name")
                
                if "ownership_percentage" not in member:
                    results["valid"] = False
                    results["issues"].append(f"Member {i+1} missing ownership percentage")
        
        # Validate managers if manager-managed
        if details["management_type"] == "manager":
            managers = details.get("managers", [])
            if not managers:
                results["valid"] = False
                results["issues"].append("At least one manager is required for manager-managed LLC")
        
        return results
    
    @staticmethod
    def validate_addresses(details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate business addresses.
        
        Args:
            details: Dictionary containing business information
            
        Returns:
            Dictionary containing validation results
        """
        results = {
            "valid": True,
            "issues": []
        }
        
        # Validate principal office address
        office = details.get("principal_office_address", {})
        required_address_fields = ["street1", "city", "state", "zip"]
        
        for field in required_address_fields:
            if field not in office or not office[field]:
                results["valid"] = False
                results["issues"].append(f"Principal office address missing {field}")
        
        # Validate registered agent address
        agent = details.get("registered_agent", {})
        agent_address = agent.get("address", {})
        
        for field in required_address_fields:
            if field not in agent_address or not agent_address[field]:
                results["valid"] = False
                results["issues"].append(f"Registered agent address missing {field}")
        
        # Validate mailing address if different
        if details.get("mailing_address_different"):
            mailing = details.get("mailing_address", {})
            for field in required_address_fields:
                if field not in mailing or not mailing[field]:
                    results["valid"] = False
                    results["issues"].append(f"Mailing address missing {field}")
        
        return results
    
    @staticmethod
    def validate_nonprofit_requirements(details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate non-profit specific requirements.
        
        Args:
            details: Dictionary containing business information
            
        Returns:
            Dictionary containing validation results
        """
        results = {
            "valid": True,
            "issues": []
        }
        
        # Validate tax exemption category
        valid_categories = ["501(c)(3)", "501(c)(4)", "501(c)(6)", "501(c)(7)"]
        category = details.get("tax_exemption_category")
        
        if not category:
            results["valid"] = False
            results["issues"].append("Tax exemption category is required for non-profits")
        elif category not in valid_categories:
            results["valid"] = False
            results["issues"].append(f"Invalid tax exemption category. Must be one of: {', '.join(valid_categories)}")
        
        # Validate board of directors
        board = details.get("board_of_directors", [])
        if not board:
            results["valid"] = False
            results["issues"].append("Board of directors is required for non-profits")
        elif len(board) < 3:
            results["valid"] = False
            results["issues"].append("At least three board members are required")
        
        # Validate purpose statement
        purpose = details.get("purpose_statement")
        if not purpose:
            results["valid"] = False
            results["issues"].append("Purpose statement is required for non-profits")
        
        return results
