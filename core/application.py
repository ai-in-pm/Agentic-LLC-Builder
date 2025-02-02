"""
Main application module for the LLC Builder.
"""

import os
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

from core.document_generator import DocumentGenerator
from core.business_validator import BusinessValidator
from core.utils import (
    calculate_fees,
    generate_filing_checklist,
    load_state_data
)

class LLCBuilder:
    """Main application class for building LLCs."""
    
    def __init__(self, output_dir: str):
        """
        Initialize the LLC Builder.
        
        Args:
            output_dir: Directory for output files
        """
        self.output_dir = output_dir
        self.document_generator = DocumentGenerator(output_dir)
        self.state_data = load_state_data()
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def create_llc(self, business_details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new LLC with the provided details.
        
        Args:
            business_details: Dictionary containing business information
            
        Returns:
            Dictionary containing results and generated files
        """
        results = {
            "success": False,
            "validation_results": None,
            "documents": {},
            "checklist": [],
            "fees": {},
            "issues": []
        }
        
        # Validate business details
        validation = BusinessValidator.validate_business_details(business_details)
        results["validation_results"] = validation
        
        if not validation["valid"]:
            results["issues"].extend(validation["issues"])
            return results
        
        try:
            # Generate formation documents
            results["documents"] = self.document_generator.generate_formation_documents(business_details)
            
            # Generate HR documents if requested
            if business_details.get("generate_hr_documents", False):
                hr_docs = self.document_generator.generate_hr_documents(business_details)
                results["documents"].update(hr_docs)
            
            # Generate financial documents if requested
            if business_details.get("generate_financial_documents", False):
                financial_docs = self.document_generator.generate_financial_documents(business_details)
                results["documents"].update(financial_docs)
            
            # Calculate fees
            results["fees"] = calculate_fees(
                business_details["state"],
                business_details.get("requested_services", [])
            )
            
            # Generate filing checklist
            results["checklist"] = generate_filing_checklist(
                business_details["state"],
                business_details["organization_type"]
            )
            
            results["success"] = True
            
        except Exception as e:
            results["success"] = False
            results["issues"].append(str(e))
        
        return results
    
    def get_state_requirements(self, state_code: str) -> Dict[str, Any]:
        """
        Get requirements for a specific state.
        
        Args:
            state_code: Two-letter state code
            
        Returns:
            Dictionary containing state requirements
        """
        if state_code not in self.state_data:
            raise KeyError(f"Invalid state code: {state_code}")
        return self.state_data[state_code]
    
    def estimate_costs(self, state_code: str, services: List[str]) -> Dict[str, float]:
        """
        Estimate costs for LLC formation.
        
        Args:
            state_code: Two-letter state code
            services: List of requested services
            
        Returns:
            Dictionary containing cost breakdown
        """
        return calculate_fees(state_code, services)
    
    def get_formation_checklist(self, state_code: str, business_type: str) -> List[Dict[str, Any]]:
        """
        Get formation checklist for a specific state and business type.
        
        Args:
            state_code: Two-letter state code
            business_type: Type of business
            
        Returns:
            List of checklist items
        """
        return generate_filing_checklist(state_code, business_type)
    
    def validate_business_info(self, business_details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate business information.
        
        Args:
            business_details: Dictionary containing business information
            
        Returns:
            Dictionary containing validation results
        """
        return BusinessValidator.validate_business_details(business_details)
    
    def generate_documents(self, business_details: Dict[str, Any], document_types: List[str]) -> Dict[str, str]:
        """
        Generate specific documents.
        
        Args:
            business_details: Dictionary containing business information
            document_types: List of document types to generate
            
        Returns:
            Dictionary mapping document types to file paths
        """
        documents = {}
        
        for doc_type in document_types:
            if doc_type == "formation":
                docs = self.document_generator.generate_formation_documents(business_details)
                documents.update(docs)
            elif doc_type == "hr":
                docs = self.document_generator.generate_hr_documents(business_details)
                documents.update(docs)
            elif doc_type == "financial":
                docs = self.document_generator.generate_financial_documents(business_details)
                documents.update(docs)
        
        return documents
