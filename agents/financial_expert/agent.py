"""
Financial Expert Agent for LLC formation.
"""

from typing import Dict, Any, List
from ..job_descriptions import JobDescriptionGenerator
from states.state_factory import StateFactory

class FinancialExpertAgent:
    """Agent responsible for financial aspects of LLC formation."""
    
    def __init__(self):
        """Initialize the Financial Expert Agent."""
        self.job_generator = JobDescriptionGenerator()
    
    def setup_financial_structure(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Setup financial structure for the LLC."""
        try:
            # Process financial requirements
            banking_reqs = self._determine_banking_requirements(context)
            tax_reqs = self._determine_tax_requirements(context)
            accounting_reqs = self._determine_accounting_requirements(context)
            
            # Get required job roles
            job_roles = self.get_required_job_roles()
            
            state = StateFactory.get_state(context["request"].state_code)
            
            # Determine tax structure
            tax_structure = self._determine_tax_structure(context)
            
            # Generate banking requirements
            banking = self._generate_banking_requirements(context)
            
            # Create financial policies
            policies = self._create_financial_policies(context)
            
            # Generate compliance requirements
            compliance = self._generate_compliance_requirements(context)
            
            return {
                "status": "ready",
                "banking_requirements": banking_reqs,
                "tax_requirements": tax_reqs,
                "accounting_requirements": accounting_reqs,
                "job_roles": job_roles,
                "tax_structure": tax_structure,
                "banking_requirements": banking,
                "financial_policies": policies,
                "compliance_requirements": compliance,
                "next_steps": self._generate_next_steps(context),
                "warnings": self._generate_warnings(context)
            }
            
        except Exception as e:
            context["errors"].append(f"Financial setup error: {str(e)}")
            return self._generate_error_response(context)
    
    def get_required_job_roles(self) -> List[Dict[str, Any]]:
        """Get required job roles for financial operations."""
        return self.job_generator.create_financial_expert_jobs()
    
    def _determine_banking_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Determine banking requirements."""
        return {
            "business_account": True,
            "required_documents": [
                "EIN Documentation",
                "LLC Formation Documents",
                "Operating Agreement"
            ],
            "recommended_banks": [
                "Major National Banks",
                "Local Business Banks",
                "Online Business Banks"
            ]
        }
    
    def _determine_tax_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Determine tax requirements."""
        return {
            "federal_tax_id": True,
            "state_tax_registration": True,
            "sales_tax_permit": "If applicable",
            "tax_deadlines": {
                "annual_filing": "March 15",
                "estimated_taxes": "Quarterly"
            }
        }
    
    def _determine_accounting_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Determine accounting requirements."""
        return {
            "accounting_method": "Accrual",
            "bookkeeping_system": "Required",
            "financial_statements": [
                "Balance Sheet",
                "Income Statement",
                "Cash Flow Statement"
            ],
            "recommended_software": [
                "QuickBooks",
                "Xero",
                "FreshBooks"
            ]
        }
    
    def _determine_tax_structure(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Determine tax structure."""
        state = StateFactory.get_state(context["request"].state_code)
        
        tax_structure = {
            "federal_classification": self._get_federal_classification(context),
            "state_classification": state.get_tax_classification(),
            "filing_requirements": {
                "federal": [
                    "Annual tax return",
                    "Quarterly estimated taxes",
                    "Employment taxes (if applicable)"
                ],
                "state": state.get_tax_filing_requirements()
            },
            "tax_deadlines": {
                "federal": {
                    "annual_return": "March 15 (partnerships) or April 15 (single-member)",
                    "estimated_taxes": ["April 15", "June 15", "September 15", "January 15"]
                },
                "state": state.get_tax_deadlines()
            }
        }
        
        # Add professional LLC specific requirements
        if context["request"].llc_type == "professional":
            tax_structure["professional_requirements"] = state.get_professional_tax_requirements()
        
        return tax_structure
    
    def _get_federal_classification(self, context: Dict[str, Any]) -> str:
        """Get federal tax classification."""
        if context["request"].llc_type == "single-member":
            return "Disregarded Entity"
        else:
            return "Partnership"
    
    def _generate_banking_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate banking requirements."""
        return {
            "required_accounts": [
                {
                    "type": "Business Checking",
                    "purpose": "Primary operating account",
                    "requirements": [
                        "EIN",
                        "Articles of Organization",
                        "Operating Agreement",
                        "Owner ID"
                    ]
                },
                {
                    "type": "Business Savings",
                    "purpose": "Reserve funds",
                    "requirements": [
                        "Business Checking Account",
                        "Initial deposit"
                    ]
                }
            ],
            "recommended_features": [
                "Online banking",
                "Mobile deposit",
                "ACH/wire transfers",
                "Business debit cards",
                "Merchant services"
            ],
            "documentation_needed": [
                "EIN confirmation letter",
                "Articles of Organization",
                "Operating Agreement",
                "Owner identification",
                "Initial deposit"
            ]
        }
    
    def _create_financial_policies(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Create financial policies."""
        return {
            "accounting_policies": [
                "Cash vs. accrual method",
                "Chart of accounts structure",
                "Revenue recognition",
                "Expense categorization"
            ],
            "internal_controls": [
                "Bank account management",
                "Payment authorization",
                "Expense reimbursement",
                "Financial reporting"
            ],
            "record_keeping": [
                "Transaction documentation",
                "Receipt management",
                "Financial statements",
                "Tax records"
            ],
            "review_frequency": "Quarterly"
        }
    
    def _generate_compliance_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate compliance requirements."""
        state = StateFactory.get_state(context["request"].state_code)
        
        return {
            "federal_requirements": [
                "Annual tax returns",
                "Quarterly estimated taxes",
                "Employment tax deposits",
                "Information returns"
            ],
            "state_requirements": state.get_financial_compliance_requirements(),
            "reporting_deadlines": {
                "federal": {
                    "tax_returns": "March 15 or April 15",
                    "estimated_taxes": "Quarterly",
                    "w2_1099": "January 31"
                },
                "state": state.get_reporting_deadlines()
            },
            "record_retention": {
                "tax_records": "7 years",
                "financial_statements": "Permanent",
                "bank_statements": "7 years",
                "contracts": "7 years after expiration"
            }
        }
    
    def _generate_next_steps(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate next steps for financial setup."""
        return [
            {
                "step": "Open Business Bank Account",
                "priority": "High",
                "timeline": "1-2 weeks"
            },
            {
                "step": "Set Up Accounting System",
                "priority": "High",
                "timeline": "1-2 weeks"
            },
            {
                "step": "Register for Tax Accounts",
                "priority": "High",
                "timeline": "2-3 weeks"
            }
        ]
    
    def _generate_warnings(self, context: Dict[str, Any]) -> List[str]:
        """Generate warnings for financial setup."""
        return [
            "Ensure separation of personal and business finances",
            "Keep detailed financial records from day one",
            "Consider consulting with a tax professional"
        ]
    
    def _generate_error_response(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "status": "failed",
            "errors": context.get("errors", []),
            "warnings": self._generate_warnings(context)
        }
