"""
Module for generating legal and business documents.
"""

import os
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
from core.utils import generate_document_from_template, generate_file_name, save_document

class DocumentGenerator:
    """Class for generating various business and legal documents."""
    
    def __init__(self, output_dir: str):
        """
        Initialize the DocumentGenerator.
        
        Args:
            output_dir: Directory to save generated documents
        """
        self.output_dir = output_dir
        self.template_dir = Path(__file__).parent.parent / "templates"
    
    def generate_formation_documents(self, business_details: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate all necessary formation documents.
        
        Args:
            business_details: Dictionary containing business information
            
        Returns:
            Dictionary mapping document types to file paths
        """
        documents = {}
        
        # Generate Articles of Organization
        articles = self.generate_articles_of_organization(business_details)
        documents["articles_of_organization"] = articles
        
        # Generate Operating Agreement
        agreement = self.generate_operating_agreement(business_details)
        documents["operating_agreement"] = agreement
        
        # Generate additional documents based on business type
        if business_details.get("organization_type") == "non-profit":
            if business_details.get("tax_exemption_category") == "501(c)(6)":
                documents.update(self.generate_501c6_documents(business_details))
            elif business_details.get("tax_exemption_category") == "501(c)(3)":
                documents.update(self.generate_501c3_documents(business_details))
        
        return documents
    
    def generate_articles_of_organization(self, business_details: Dict[str, Any]) -> str:
        """
        Generate Articles of Organization.
        
        Args:
            business_details: Dictionary containing business information
            
        Returns:
            Path to generated document
        """
        state_code = business_details["state"]
        template_path = self.template_dir / "legal" / "state_specific" / "articles_of_organization.md"
        
        # Add state-specific context
        context = {
            **business_details,
            "state_code_is_ny": state_code == "NY",
            "state_code_is_ca": state_code == "CA",
            "state_code_is_de": state_code == "DE",
            "state_code_is_fl": state_code == "FL",
            "state_code_is_tx": state_code == "TX",
            "state_code_is_az": state_code == "AZ",
            "execution_date": datetime.now().strftime("%B %d, %Y")
        }
        
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("articles_of_organization_{business_name}_{state}", context)
        
        return save_document(content, self.output_dir, f"{filename}.md")
    
    def generate_operating_agreement(self, business_details: Dict[str, Any]) -> str:
        """
        Generate Operating Agreement.
        
        Args:
            business_details: Dictionary containing business information
            
        Returns:
            Path to generated document
        """
        template_path = self.template_dir / "legal" / "state_specific" / "operating_agreement.md"
        
        # Add agreement-specific context
        context = {
            **business_details,
            "effective_date": datetime.now().strftime("%B %d, %Y"),
            "single_member": len(business_details.get("members", [])) == 1,
            "member_managed": business_details.get("management_type") == "member"
        }
        
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("operating_agreement_{business_name}_{state}", context)
        
        return save_document(content, self.output_dir, f"{filename}.md")
    
    def generate_501c6_documents(self, business_details: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate documents specific to 501(c)(6) organizations.
        
        Args:
            business_details: Dictionary containing business information
            
        Returns:
            Dictionary mapping document types to file paths
        """
        documents = {}
        
        # Generate Form 1024
        template_path = self.template_dir / "legal" / "non-profit" / "form_1024.md"
        context = {**business_details}
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("form_1024_{business_name}", context)
        documents["form_1024"] = save_document(content, self.output_dir, f"{filename}.md")
        
        # Generate Membership Agreement
        template_path = self.template_dir / "legal" / "non-profit" / "membership_agreement.md"
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("membership_agreement_{business_name}", context)
        documents["membership_agreement"] = save_document(content, self.output_dir, f"{filename}.md")
        
        # Generate Industry Advancement Plan
        template_path = self.template_dir / "legal" / "non-profit" / "industry_advancement_plan.md"
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("industry_advancement_plan_{business_name}", context)
        documents["industry_advancement_plan"] = save_document(content, self.output_dir, f"{filename}.md")
        
        return documents
    
    def generate_501c3_documents(self, business_details: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate documents specific to 501(c)(3) organizations.
        
        Args:
            business_details: Dictionary containing business information
            
        Returns:
            Dictionary mapping document types to file paths
        """
        documents = {}
        
        # Generate Form 1023
        template_path = self.template_dir / "legal" / "non-profit" / "form_1023.md"
        context = {**business_details}
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("form_1023_{business_name}", context)
        documents["form_1023"] = save_document(content, self.output_dir, f"{filename}.md")
        
        # Generate Conflict of Interest Policy
        template_path = self.template_dir / "legal" / "non-profit" / "conflict_of_interest_policy.md"
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("conflict_of_interest_policy_{business_name}", context)
        documents["conflict_of_interest_policy"] = save_document(content, self.output_dir, f"{filename}.md")
        
        return documents
    
    def generate_hr_documents(self, business_details: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate HR-related documents.
        
        Args:
            business_details: Dictionary containing business information
            
        Returns:
            Dictionary mapping document types to file paths
        """
        documents = {}
        org_type = business_details.get("organization_type", "profit")
        
        # Generate Employee Handbook
        template_path = self.template_dir / "hr" / org_type / "employee_handbook.md"
        context = {**business_details}
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("employee_handbook_{business_name}", context)
        documents["employee_handbook"] = save_document(content, self.output_dir, f"{filename}.md")
        
        # Generate Employment Agreement
        template_path = self.template_dir / "hr" / org_type / "employment_agreement.md"
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("employment_agreement_{business_name}", context)
        documents["employment_agreement"] = save_document(content, self.output_dir, f"{filename}.md")
        
        # Generate additional documents for non-profits
        if org_type == "non-profit":
            # Generate Volunteer Agreement
            template_path = self.template_dir / "hr" / "non-profit" / "volunteer_agreement.md"
            content = generate_document_from_template(str(template_path), context)
            filename = generate_file_name("volunteer_agreement_{business_name}", context)
            documents["volunteer_agreement"] = save_document(content, self.output_dir, f"{filename}.md")
            
            # Generate Board Member Agreement
            template_path = self.template_dir / "hr" / "non-profit" / "board_member_agreement.md"
            content = generate_document_from_template(str(template_path), context)
            filename = generate_file_name("board_member_agreement_{business_name}", context)
            documents["board_member_agreement"] = save_document(content, self.output_dir, f"{filename}.md")
        
        return documents
    
    def generate_financial_documents(self, business_details: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate financial documents.
        
        Args:
            business_details: Dictionary containing business information
            
        Returns:
            Dictionary mapping document types to file paths
        """
        documents = {}
        org_type = business_details.get("organization_type", "profit")
        
        # Generate Financial Projections
        template_path = self.template_dir / "financial" / org_type / "financial_projections.md"
        context = {**business_details}
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("financial_projections_{business_name}", context)
        documents["financial_projections"] = save_document(content, self.output_dir, f"{filename}.md")
        
        # Generate Tax Structure Document
        template_path = self.template_dir / "financial" / org_type / "tax_structure.md"
        content = generate_document_from_template(str(template_path), context)
        filename = generate_file_name("tax_structure_{business_name}", context)
        documents["tax_structure"] = save_document(content, self.output_dir, f"{filename}.md")
        
        # Generate additional documents for non-profits
        if org_type == "non-profit":
            # Generate Grant Management Document
            template_path = self.template_dir / "financial" / "non-profit" / "grant_management.md"
            content = generate_document_from_template(str(template_path), context)
            filename = generate_file_name("grant_management_{business_name}", context)
            documents["grant_management"] = save_document(content, self.output_dir, f"{filename}.md")
        
        return documents
