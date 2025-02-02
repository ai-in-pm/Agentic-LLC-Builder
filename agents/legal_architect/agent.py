"""
Legal Architect Agent for LLC formation.
"""

from typing import Dict, Any, List, Tuple
from states.state_factory import StateFactory
from ..job_descriptions import JobDescriptionGenerator

class LegalArchitectAgent:
    """
    AI agent responsible for legal aspects of LLC formation.
    Handles document preparation, compliance checks, and legal requirements.
    """
    
    def __init__(self):
        """Initialize the Legal Architect Agent."""
        self.job_generator = JobDescriptionGenerator()
    
    def process_formation(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process LLC formation request.
        
        Args:
            context: Formation context including request and state requirements
            
        Returns:
            Legal requirements and next steps
        """
        try:
            # Get state requirements
            state = StateFactory.get_state(context["request"].state_code)
            
            # Validate business name
            name_valid, name_messages = state.validate_llc_name(
                context["request"].business_name
            )
            if not name_valid:
                context["errors"].extend(name_messages)
                return self._generate_error_response(context)
            
            # Check professional eligibility if applicable
            if context["request"].llc_type == "professional":
                eligible, messages = state.check_professional_eligibility(
                    context["request"].industry,
                    context["request"].owner_info
                )
                if not eligible:
                    context["errors"].extend(messages)
                    return self._generate_error_response(context)
            
            # Get required documents
            documents = state.get_required_documents(
                is_foreign=context["request"].is_foreign,
                is_professional=context["request"].llc_type == "professional"
            )
            
            # Generate formation plan
            formation_plan = self._create_formation_plan(context, documents)
            
            results = {
                "status": "ready",
                "name_validation": {
                    "valid": name_valid,
                    "messages": name_messages
                },
                "documents_required": documents,
                "formation_plan": formation_plan,
                "next_steps": self._generate_next_steps(context),
                "warnings": self._generate_warnings(context),
                "job_roles": self.get_required_job_roles()
            }
            
            return results
            
        except Exception as e:
            context["errors"].append(f"Legal processing error: {str(e)}")
            return self._generate_error_response(context)
    
    def _create_formation_plan(
        self,
        context: Dict[str, Any],
        documents: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Create detailed formation plan."""
        state = StateFactory.get_state(context["request"].state_code)
        timeline = state.calculate_formation_timeline(
            "expedited" if context["request"].expedited else "standard",
            context["request"].is_foreign
        )
        
        return {
            "steps": [
                {
                    "step": 1,
                    "action": "File Articles of Organization",
                    "timeline": timeline["key_dates"]["filing_date"],
                    "requirements": [
                        "Completed Articles of Organization form",
                        "Filing fee payment",
                        "Owner information"
                    ]
                },
                {
                    "step": 2,
                    "action": "Establish Registered Agent",
                    "timeline": timeline["key_dates"]["filing_date"],
                    "requirements": [
                        "Registered agent information",
                        "Signed acceptance form"
                    ]
                },
                {
                    "step": 3,
                    "action": "Create Operating Agreement",
                    "timeline": timeline["key_dates"]["filing_date"],
                    "requirements": [
                        "Member information",
                        "Management structure",
                        "Capital contributions",
                        "Profit/loss allocation"
                    ]
                }
            ],
            "timeline": timeline,
            "estimated_completion": timeline["estimated_approval"]
        }
    
    def get_required_job_roles(self) -> List[Dict[str, Any]]:
        """Get required job roles for legal operations."""
        return self.job_generator.create_legal_architect_jobs()
    
    def _generate_next_steps(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate next steps for formation process."""
        steps = [
            {
                "action": "Review and sign Articles of Organization",
                "priority": 1,
                "deadline": "Immediate",
                "assigned_to": "Business Owner"
            },
            {
                "action": "Pay formation fees",
                "priority": 1,
                "deadline": "Immediate",
                "assigned_to": "Business Owner"
            }
        ]
        
        # Add publication requirement if needed
        state = StateFactory.get_state(context["request"].state_code)
        if state.get_publication_requirements():
            steps.append({
                "action": "Complete publication requirements",
                "priority": 2,
                "deadline": "Within 120 days",
                "assigned_to": "Business Owner"
            })
        
        return steps
    
    def _generate_warnings(self, context: Dict[str, Any]) -> List[str]:
        """Generate any legal warnings."""
        warnings = []
        state = StateFactory.get_state(context["request"].state_code)
        
        # Check for name restrictions
        name_valid, messages = state.validate_llc_name(
            context["request"].business_name
        )
        if messages:
            warnings.extend(messages)
        
        # Check professional requirements
        if context["request"].llc_type == "professional":
            prof_reqs = state.get_professional_requirements(
                context["request"].industry
            )
            warnings.append(
                f"Professional LLC must maintain compliance with {prof_reqs['name_requirements']['board']} requirements"
            )
        
        # Check foreign LLC requirements
        if context["request"].is_foreign:
            foreign_reqs = state.get_foreign_requirements()
            warnings.append(
                f"Foreign LLC must maintain registered agent and comply with {context['request'].state_code} state requirements"
            )
        
        return warnings
    
    def _generate_error_response(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "status": "error",
            "errors": context["errors"],
            "recommendations": [
                "Review and correct any validation errors",
                "Ensure all required information is provided",
                "Consider consulting with a legal professional"
            ]
        }
