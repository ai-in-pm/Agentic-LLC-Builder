"""
HR Strategist Agent for LLC formation.
"""

from typing import Dict, Any, List
from states.state_factory import StateFactory
from ..job_descriptions import JobDescriptionGenerator

class HRStrategistAgent:
    """
    AI agent responsible for HR aspects of LLC formation.
    Handles EIN application, employment policies, and HR setup.
    """
    
    def __init__(self):
        """Initialize the HR Strategist Agent."""
        self.job_generator = JobDescriptionGenerator()
    
    def setup_hr_structure(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Setup HR structure for LLC formation.
        
        Args:
            context: Formation context including request and state requirements
            
        Returns:
            HR setup information and next steps
        """
        try:
            state = StateFactory.get_state(context["request"].state_code)
            
            # Determine EIN requirements
            ein_requirements = self._determine_ein_requirements(context)
            
            # Generate employment policies
            policies = self._generate_employment_policies(context)
            
            # Create onboarding checklist
            onboarding = self._create_onboarding_checklist(context)
            
            # Generate compliance requirements
            compliance = self._generate_compliance_requirements(context)
            
            # Get required job roles
            job_roles = self.get_required_job_roles()
            
            return {
                "status": "ready",
                "ein_requirements": ein_requirements,
                "employment_policies": policies,
                "onboarding_checklist": onboarding,
                "compliance_requirements": compliance,
                "job_roles": job_roles,
                "next_steps": self._generate_next_steps(context),
                "warnings": self._generate_warnings(context)
            }
            
        except Exception as e:
            context["errors"].append(f"HR setup error: {str(e)}")
            return self._generate_error_response(context)
    
    def get_required_job_roles(self) -> List[Dict[str, Any]]:
        """Get required job roles for HR operations."""
        return self.job_generator.create_hr_strategist_jobs()
    
    def _determine_ein_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Determine EIN requirements."""
        return {
            "required": True,  # All LLCs need an EIN
            "application_method": "online",
            "requirements": [
                "Legal business name",
                "Trade name (if applicable)",
                "Responsible party's SSN",
                "Physical business address",
                "Start date of business",
                "Principal business activity"
            ],
            "timeline": "2-4 weeks for processing",
            "cost": "No cost",
            "next_steps": [
                "Gather required information",
                "Complete Form SS-4 online",
                "Receive EIN immediately upon completion"
            ]
        }
    
    def _generate_employment_policies(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate employment policies."""
        state = StateFactory.get_state(context["request"].state_code)
        
        return {
            "required_policies": [
                "Equal Employment Opportunity",
                "Anti-Harassment",
                "Workplace Safety",
                "Wage and Hour",
                "Leave Policies",
                "Code of Conduct"
            ],
            "state_specific": state.get_employment_requirements(),
            "recommended_policies": [
                "Remote Work",
                "Social Media",
                "Confidentiality",
                "Data Privacy"
            ],
            "implementation_timeline": "1-2 months",
            "review_frequency": "Annual"
        }
    
    def _create_onboarding_checklist(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create onboarding checklist."""
        return [
            {
                "phase": "Pre-employment",
                "tasks": [
                    "Complete I-9 verification",
                    "Submit W-4 form",
                    "Sign employment agreement",
                    "Complete background check (if applicable)"
                ]
            },
            {
                "phase": "First Day",
                "tasks": [
                    "Review employee handbook",
                    "Set up workstation and credentials",
                    "Complete safety training",
                    "Meet team members"
                ]
            },
            {
                "phase": "First Week",
                "tasks": [
                    "Complete orientation training",
                    "Review job responsibilities",
                    "Set up benefits enrollment",
                    "Review company policies"
                ]
            },
            {
                "phase": "First Month",
                "tasks": [
                    "Complete role-specific training",
                    "Schedule performance expectations meeting",
                    "Review 30-day goals",
                    "Gather initial feedback"
                ]
            }
        ]
    
    def _generate_compliance_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate compliance requirements."""
        state = StateFactory.get_state(context["request"].state_code)
        
        return {
            "federal_requirements": [
                "Display required workplace posters",
                "Maintain employee records",
                "Follow FLSA guidelines",
                "Comply with OSHA regulations"
            ],
            "state_requirements": state.get_employment_compliance_requirements(),
            "reporting_requirements": [
                "Quarterly tax filings",
                "Annual tax forms",
                "Workers' compensation reports",
                "New hire reporting"
            ],
            "record_keeping": {
                "required_records": [
                    "Employment applications",
                    "Personnel files",
                    "Payroll records",
                    "Tax documents"
                ],
                "retention_period": "3-7 years depending on document type"
            }
        }
    
    def _generate_next_steps(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate next steps."""
        return [
            {
                "action": "Apply for EIN",
                "priority": 1,
                "deadline": "Immediate",
                "assigned_to": "Business Owner"
            },
            {
                "action": "Set up payroll system",
                "priority": 2,
                "deadline": "Before first hire",
                "assigned_to": "Business Owner"
            },
            {
                "action": "Create employee handbook",
                "priority": 2,
                "deadline": "Before first hire",
                "assigned_to": "Business Owner"
            },
            {
                "action": "Set up workers' compensation insurance",
                "priority": 1,
                "deadline": "Before first hire",
                "assigned_to": "Business Owner"
            }
        ]
    
    def _generate_warnings(self, context: Dict[str, Any]) -> List[str]:
        """Generate warnings."""
        warnings = [
            "Ensure all employment policies comply with state and federal laws",
            "Keep accurate records of all employee-related documentation",
            "Stay current with changing employment regulations"
        ]
        
        state = StateFactory.get_state(context["request"].state_code)
        state_warnings = state.get_employment_warnings()
        if state_warnings:
            warnings.extend(state_warnings)
        
        return warnings
    
    def _generate_error_response(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "status": "error",
            "errors": context["errors"],
            "recommendations": [
                "Review all required HR documentation",
                "Ensure compliance with state and federal regulations",
                "Consider consulting with an HR professional"
            ]
        }
