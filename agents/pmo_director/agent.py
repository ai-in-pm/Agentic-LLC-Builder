"""
PMO Director Agent for managing project timelines, deliverables, and coordination.
"""

from typing import Dict, Any, List
from datetime import datetime, timedelta
from states.state_factory import StateFactory
from ..job_descriptions import JobDescriptionGenerator

class PMODirectorAgent:
    """
    PMO Director Agent responsible for project management and coordination
    during the LLC formation process.
    """
    
    def __init__(self):
        """Initialize the PMO Director Agent."""
        self.job_generator = JobDescriptionGenerator()
    
    def manage_formation(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Manage the LLC formation process.
        
        Args:
            context: Formation context including request and state requirements
            
        Returns:
            Project management plan and status
        """
        try:
            state = StateFactory.get_state(context["request"].state_code)
            
            # Create project timeline
            timeline = self._create_timeline(context)
            
            # Define deliverables
            deliverables = self._define_deliverables(context)
            
            # Identify dependencies
            dependencies = self._identify_dependencies(context)
            
            # Generate resource plan
            resources = self._generate_resource_plan(context)
            
            # Get required job roles
            job_roles = self.get_required_job_roles()
            
            return {
                "status": "ready",
                "timeline": timeline,
                "deliverables": deliverables,
                "dependencies": dependencies,
                "resources": resources,
                "job_roles": job_roles,
                "next_steps": self._generate_next_steps(context),
                "risks": self._identify_risks(context)
            }
            
        except Exception as e:
            context["errors"].append(f"Project management error: {str(e)}")
            return self._generate_error_response(context)
    
    def get_required_job_roles(self) -> List[Dict[str, Any]]:
        """Get required job roles for project management operations."""
        return self.job_generator.create_pmo_director_jobs()
    
    def _create_timeline(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Create formation timeline."""
        state = StateFactory.get_state(context["request"].state_code)
        processing_time = state.get_processing_time()
        
        timeline = {
            "start_date": datetime.now(),
            "estimated_completion": datetime.now() + timedelta(days=processing_time),
            "phases": [
                {
                    "name": "Pre-Formation",
                    "tasks": [
                        {
                            "name": "Business name verification",
                            "duration": 1,
                            "dependencies": [],
                            "status": "pending"
                        },
                        {
                            "name": "Document preparation",
                            "duration": 2,
                            "dependencies": ["Business name verification"],
                            "status": "pending"
                        }
                    ]
                },
                {
                    "name": "Formation",
                    "tasks": [
                        {
                            "name": "State filing",
                            "duration": processing_time,
                            "dependencies": ["Document preparation"],
                            "status": "pending"
                        },
                        {
                            "name": "EIN application",
                            "duration": 3,
                            "dependencies": ["State filing"],
                            "status": "pending"
                        }
                    ]
                },
                {
                    "name": "Post-Formation",
                    "tasks": [
                        {
                            "name": "Bank account setup",
                            "duration": 2,
                            "dependencies": ["EIN application"],
                            "status": "pending"
                        },
                        {
                            "name": "Compliance setup",
                            "duration": 5,
                            "dependencies": ["State filing"],
                            "status": "pending"
                        }
                    ]
                }
            ]
        }
        
        # Add state-specific requirements
        state_requirements = state.get_formation_requirements()
        if state_requirements.get("publication_required"):
            timeline["phases"][1]["tasks"].append({
                "name": "Publication requirements",
                "duration": state_requirements["publication_period"],
                "dependencies": ["State filing"],
                "status": "pending"
            })
        
        # Add professional LLC requirements
        if context["request"].llc_type == "professional":
            timeline["phases"][0]["tasks"].extend([
                {
                    "name": "Professional license verification",
                    "duration": 3,
                    "dependencies": [],
                    "status": "pending"
                },
                {
                    "name": "Professional board approval",
                    "duration": 10,
                    "dependencies": ["Professional license verification"],
                    "status": "pending"
                }
            ])
        
        return timeline
    
    def _define_deliverables(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Define formation deliverables."""
        state = StateFactory.get_state(context["request"].state_code)
        
        deliverables = [
            {
                "name": "Articles of Organization",
                "type": "document",
                "status": "pending",
                "owner": "Legal Architect",
                "deadline": "Pre-Formation"
            },
            {
                "name": "Operating Agreement",
                "type": "document",
                "status": "pending",
                "owner": "Legal Architect",
                "deadline": "Formation"
            },
            {
                "name": "EIN Confirmation",
                "type": "document",
                "status": "pending",
                "owner": "HR Strategist",
                "deadline": "Formation"
            },
            {
                "name": "Bank Account Documentation",
                "type": "document",
                "status": "pending",
                "owner": "Financial Expert",
                "deadline": "Post-Formation"
            },
            {
                "name": "Compliance Documentation",
                "type": "document",
                "status": "pending",
                "owner": "Governance Officer",
                "deadline": "Post-Formation"
            }
        ]
        
        # Add state-specific deliverables
        state_deliverables = state.get_required_deliverables()
        if state_deliverables:
            deliverables.extend(state_deliverables)
        
        return deliverables
    
    def _identify_dependencies(self, context: Dict[str, Any]) -> Dict[str, List[str]]:
        """Identify formation dependencies."""
        dependencies = {
            "Business name verification": [],
            "Document preparation": ["Business name verification"],
            "State filing": ["Document preparation"],
            "EIN application": ["State filing"],
            "Bank account setup": ["EIN application"],
            "Compliance setup": ["State filing"]
        }
        
        # Add professional LLC dependencies
        if context["request"].llc_type == "professional":
            dependencies.update({
                "Professional license verification": [],
                "Professional board approval": ["Professional license verification"],
                "State filing": ["Document preparation", "Professional board approval"]
            })
        
        return dependencies
    
    def _generate_resource_plan(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate resource plan."""
        return {
            "agents": {
                "Legal Architect": {
                    "responsibilities": [
                        "Business name verification",
                        "Document preparation",
                        "State filing"
                    ],
                    "deliverables": [
                        "Articles of Organization",
                        "Operating Agreement"
                    ]
                },
                "HR Strategist": {
                    "responsibilities": [
                        "EIN application"
                    ],
                    "deliverables": [
                        "EIN Confirmation"
                    ]
                },
                "Financial Expert": {
                    "responsibilities": [
                        "Bank account setup"
                    ],
                    "deliverables": [
                        "Bank Account Documentation"
                    ]
                },
                "Governance Officer": {
                    "responsibilities": [
                        "Compliance setup"
                    ],
                    "deliverables": [
                        "Compliance Documentation"
                    ]
                }
            },
            "external": {
                "State Filing Office": {
                    "role": "Process formation documents",
                    "timeline": "Per state requirements"
                },
                "IRS": {
                    "role": "Process EIN application",
                    "timeline": "2-3 business days"
                },
                "Bank": {
                    "role": "Process account opening",
                    "timeline": "1-2 business days"
                }
            }
        }
    
    def _generate_next_steps(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate next steps."""
        return [
            {
                "action": "Verify business name availability",
                "owner": "Legal Architect",
                "priority": 1,
                "deadline": "Immediate"
            },
            {
                "action": "Prepare formation documents",
                "owner": "Legal Architect",
                "priority": 1,
                "deadline": "Within 2 days"
            },
            {
                "action": "Review formation requirements",
                "owner": "All Agents",
                "priority": 1,
                "deadline": "Within 1 day"
            },
            {
                "action": "Schedule coordination meeting",
                "owner": "PMO Director",
                "priority": 2,
                "deadline": "Within 1 day"
            }
        ]
    
    def _identify_risks(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify formation risks."""
        state = StateFactory.get_state(context["request"].state_code)
        
        risks = [
            {
                "description": "Business name unavailability",
                "impact": "High",
                "mitigation": "Prepare alternative names",
                "owner": "Legal Architect"
            },
            {
                "description": "Delayed state processing",
                "impact": "Medium",
                "mitigation": "Submit early, monitor status",
                "owner": "Legal Architect"
            },
            {
                "description": "Missing documentation",
                "impact": "High",
                "mitigation": "Checklist verification",
                "owner": "All Agents"
            }
        ]
        
        # Add state-specific risks
        state_risks = state.get_formation_risks()
        if state_risks:
            risks.extend(state_risks)
        
        return risks
    
    def _generate_error_response(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "status": "error",
            "errors": context["errors"],
            "recommendations": [
                "Review project timeline",
                "Verify all dependencies",
                "Check resource availability"
            ]
        }
