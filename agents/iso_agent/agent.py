"""
ISO Agent for ensuring compliance with international standards.
"""

from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ISOStandard:
    """Represents an ISO standard."""
    code: str
    name: str
    description: str
    requirements: List[str]
    applicability: Dict[str, Any]
    documentation_required: List[str]

class ISOAgent:
    """Agent responsible for ISO compliance and standards implementation."""
    
    def __init__(self):
        """Initialize the ISO Agent."""
        self._standards = self._initialize_standards()
    
    def _initialize_standards(self) -> Dict[str, ISOStandard]:
        """Initialize relevant ISO standards."""
        return {
            "ISO_9001": ISOStandard(
                code="9001:2015",
                name="Quality Management Systems",
                description="Requirements for quality management systems",
                requirements=[
                    "Document control system",
                    "Management responsibility",
                    "Resource management",
                    "Product/Service delivery",
                    "Measurement and improvement"
                ],
                applicability={
                    "business_size": "any",
                    "industry": "all"
                },
                documentation_required=[
                    "Quality Manual",
                    "Process Documentation",
                    "Work Instructions"
                ]
            ),
            "ISO_27001": ISOStandard(
                code="27001:2022",
                name="Information Security Management",
                description="Requirements for information security management systems",
                requirements=[
                    "Security policy",
                    "Asset management",
                    "Access control",
                    "Risk assessment",
                    "Security incident management"
                ],
                applicability={
                    "business_size": "any",
                    "industry": "all",
                    "priority": "high for digital businesses"
                },
                documentation_required=[
                    "Information Security Policy",
                    "Risk Assessment Reports",
                    "Security Procedures"
                ]
            ),
            "ISO_31000": ISOStandard(
                code="31000:2018",
                name="Risk Management",
                description="Guidelines for enterprise risk management",
                requirements=[
                    "Risk assessment framework",
                    "Risk treatment",
                    "Monitoring and review",
                    "Communication and consultation"
                ],
                applicability={
                    "business_size": "any",
                    "industry": "all"
                },
                documentation_required=[
                    "Risk Management Policy",
                    "Risk Register",
                    "Treatment Plans"
                ]
            ),
            "ISO_14001": ISOStandard(
                code="14001:2015",
                name="Environmental Management Systems",
                description="Requirements for environmental management systems",
                requirements=[
                    "Environmental policy",
                    "Environmental aspects assessment",
                    "Legal compliance",
                    "Environmental objectives",
                    "Performance monitoring"
                ],
                applicability={
                    "business_size": "any",
                    "industry": "all",
                    "priority": "high for manufacturing/industrial"
                },
                documentation_required=[
                    "Environmental Policy",
                    "Environmental Aspects Register",
                    "Legal Register",
                    "Environmental Objectives"
                ]
            ),
            "ISO_45001": ISOStandard(
                code="45001:2018",
                name="Occupational Health and Safety",
                description="Requirements for occupational health and safety management systems",
                requirements=[
                    "OH&S policy",
                    "Hazard identification",
                    "Risk assessment",
                    "Emergency preparedness",
                    "Performance evaluation"
                ],
                applicability={
                    "business_size": "any",
                    "industry": "all",
                    "priority": "high for industrial/construction"
                },
                documentation_required=[
                    "OH&S Policy",
                    "Hazard Register",
                    "Risk Assessments",
                    "Emergency Procedures"
                ]
            ),
            "ISO_22301": ISOStandard(
                code="22301:2019",
                name="Business Continuity Management",
                description="Requirements for business continuity management systems",
                requirements=[
                    "Business impact analysis",
                    "Risk assessment",
                    "Business continuity strategy",
                    "Incident response",
                    "Recovery procedures"
                ],
                applicability={
                    "business_size": "any",
                    "industry": "all",
                    "priority": "high for critical services"
                },
                documentation_required=[
                    "Business Continuity Plan",
                    "Incident Response Plan",
                    "Recovery Procedures",
                    "Training Records"
                ]
            ),
            "ISO_20000": ISOStandard(
                code="20000:2018",
                name="IT Service Management",
                description="Requirements for IT service management systems",
                requirements=[
                    "Service delivery",
                    "Service level management",
                    "Change management",
                    "Incident management",
                    "Problem management"
                ],
                applicability={
                    "business_size": "any",
                    "industry": "IT/Technology",
                    "priority": "high for IT service providers"
                },
                documentation_required=[
                    "Service Catalog",
                    "SLA Documentation",
                    "Change Management Procedures",
                    "Incident Management Procedures"
                ]
            ),
            "ISO_50001": ISOStandard(
                code="50001:2018",
                name="Energy Management",
                description="Requirements for energy management systems",
                requirements=[
                    "Energy policy",
                    "Energy planning",
                    "Energy baseline",
                    "Performance monitoring",
                    "Continuous improvement"
                ],
                applicability={
                    "business_size": "any",
                    "industry": "all",
                    "priority": "high for energy-intensive industries"
                },
                documentation_required=[
                    "Energy Policy",
                    "Energy Review",
                    "Energy Baseline",
                    "Action Plans"
                ]
            )
        }
    
    def create_job_descriptions(self) -> List[Dict[str, Any]]:
        """
        Create job descriptions for ISO-related positions.
        
        Returns:
            List of job descriptions
        """
        return [
            {
                "title": "ISO Compliance Manager",
                "type": "Human",
                "description": "Lead ISO compliance initiatives and maintain management systems",
                "responsibilities": [
                    "Develop and maintain ISO management systems",
                    "Conduct internal audits",
                    "Train staff on ISO requirements",
                    "Manage certification process"
                ],
                "requirements": [
                    "5+ years ISO compliance experience",
                    "Lead Auditor certification",
                    "Bachelor's degree in relevant field",
                    "Strong project management skills"
                ],
                "salary_range": "$80,000 - $120,000"
            },
            {
                "title": "ISO Documentation Specialist",
                "type": "AI Agent",
                "description": "Manage and maintain ISO-required documentation",
                "capabilities": [
                    "Generate and update ISO documentation",
                    "Track document versions and changes",
                    "Ensure compliance with documentation requirements",
                    "Generate compliance reports"
                ],
                "requirements": [
                    "Natural language processing",
                    "Document management",
                    "Version control",
                    "Report generation"
                ],
                "integration_points": [
                    "Document management system",
                    "Quality management system",
                    "Training platform"
                ]
            },
            {
                "title": "ISO Audit Assistant",
                "type": "AI Agent",
                "description": "Support internal and external ISO audits",
                "capabilities": [
                    "Prepare audit checklists",
                    "Collect and analyze evidence",
                    "Generate audit reports",
                    "Track corrective actions"
                ],
                "requirements": [
                    "Audit process automation",
                    "Data analysis",
                    "Report generation",
                    "Compliance checking"
                ],
                "integration_points": [
                    "Audit management system",
                    "Document management system",
                    "Corrective action tracking system"
                ]
            }
        ]
    
    def evaluate_iso_requirements(self, business_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluate ISO requirements based on business context.
        
        Args:
            business_context: Dictionary containing business information
            
        Returns:
            Dictionary with ISO compliance recommendations
        """
        recommendations = {
            "recommended_standards": [],
            "priority_actions": [],
            "documentation_needed": [],
            "job_roles_needed": []
        }
        
        # Evaluate each standard for applicability
        for standard_id, standard in self._standards.items():
            if self._is_standard_applicable(standard, business_context):
                recommendations["recommended_standards"].append({
                    "standard": standard_id,
                    "name": standard.name,
                    "priority": self._determine_priority(standard, business_context),
                    "implementation_timeline": self._estimate_timeline(standard)
                })
        
        # Sort by priority
        recommendations["recommended_standards"].sort(
            key=lambda x: x["priority"],
            reverse=True
        )
        
        # Generate priority actions
        recommendations["priority_actions"] = self._generate_priority_actions(
            recommendations["recommended_standards"]
        )
        
        # Compile required documentation
        recommendations["documentation_needed"] = self._compile_documentation_needs(
            recommendations["recommended_standards"]
        )
        
        # Add recommended job roles
        recommendations["job_roles_needed"] = self.create_job_descriptions()
        
        return recommendations
    
    def generate_compliance_checklist(self, standard_id: str) -> List[Dict[str, Any]]:
        """
        Generate a compliance checklist for a specific ISO standard.
        
        Args:
            standard_id: ID of the ISO standard
            
        Returns:
            List of checklist items
        """
        if standard_id not in self._standards:
            return []
        
        standard = self._standards[standard_id]
        checklist = []
        
        # Add requirements checklist
        for req in standard.requirements:
            checklist.append({
                "category": "Requirement",
                "item": req,
                "status": "Not Started",
                "documentation_needed": self._get_documentation_for_requirement(req),
                "verification_method": self._get_verification_method(req)
            })
        
        # Add documentation checklist
        for doc in standard.documentation_required:
            checklist.append({
                "category": "Documentation",
                "item": f"Create and maintain {doc}",
                "status": "Not Started",
                "template_available": self._has_template(doc),
                "review_frequency": self._get_review_frequency(doc)
            })
        
        return checklist
    
    def generate_implementation_plan(
        self,
        standard_id: str,
        business_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate an implementation plan for an ISO standard.
        
        Args:
            standard_id: ID of the ISO standard
            business_context: Dictionary containing business information
            
        Returns:
            Implementation plan dictionary
        """
        if standard_id not in self._standards:
            return {}
        
        standard = self._standards[standard_id]
        
        return {
            "standard": {
                "id": standard_id,
                "name": standard.name,
                "version": standard.code
            },
            "phases": [
                {
                    "name": "Planning",
                    "duration": "4-6 weeks",
                    "activities": [
                        "Gap analysis",
                        "Resource assessment",
                        "Team formation",
                        "Initial documentation review"
                    ]
                },
                {
                    "name": "Development",
                    "duration": "3-4 months",
                    "activities": [
                        "Process documentation",
                        "Policy creation",
                        "Training program development",
                        "Implementation of required controls"
                    ]
                },
                {
                    "name": "Implementation",
                    "duration": "2-3 months",
                    "activities": [
                        "Staff training",
                        "Process rollout",
                        "Documentation deployment",
                        "Initial compliance monitoring"
                    ]
                },
                {
                    "name": "Review and Certification",
                    "duration": "2-3 months",
                    "activities": [
                        "Internal audit",
                        "Management review",
                        "Corrective actions",
                        "Certification audit"
                    ]
                }
            ],
            "estimated_timeline": self._estimate_timeline(standard),
            "resource_requirements": self._estimate_resources(standard, business_context),
            "critical_success_factors": [
                "Management commitment",
                "Employee engagement",
                "Adequate resources",
                "Clear communication"
            ]
        }
    
    def _is_standard_applicable(
        self,
        standard: ISOStandard,
        business_context: Dict[str, Any]
    ) -> bool:
        """Determine if a standard is applicable to the business context."""
        # Implementation would check business size, industry, and other factors
        return True  # Simplified for now
    
    def _determine_priority(
        self,
        standard: ISOStandard,
        business_context: Dict[str, Any]
    ) -> str:
        """Determine implementation priority for a standard."""
        if "priority" in standard.applicability:
            return standard.applicability["priority"]
        return "medium"
    
    def _estimate_timeline(self, standard: ISOStandard) -> str:
        """Estimate implementation timeline for a standard."""
        return "6-12 months"  # Simplified estimate
    
    def _generate_priority_actions(
        self,
        recommended_standards: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Generate priority actions based on recommended standards."""
        actions = []
        for std in recommended_standards:
            actions.append({
                "standard": std["standard"],
                "action": f"Initial assessment for {std['name']}",
                "timeline": "1-2 weeks"
            })
        return actions
    
    def _compile_documentation_needs(
        self,
        recommended_standards: List[Dict[str, Any]]
    ) -> List[str]:
        """Compile list of required documentation."""
        docs = []
        for std in recommended_standards:
            if std["standard"] in self._standards:
                docs.extend(self._standards[std["standard"]].documentation_required)
        return list(set(docs))  # Remove duplicates
    
    def _get_documentation_for_requirement(self, requirement: str) -> List[str]:
        """Get required documentation for a specific requirement."""
        return ["Policy Document", "Procedure Document", "Records"]
    
    def _get_verification_method(self, requirement: str) -> str:
        """Get verification method for a requirement."""
        return "Audit and Review"
    
    def _has_template(self, document: str) -> bool:
        """Check if a template is available for a document."""
        return True  # Simplified - would actually check template library
    
    def _get_review_frequency(self, document: str) -> str:
        """Get review frequency for a document."""
        return "Annual"
    
    def _estimate_resources(
        self,
        standard: ISOStandard,
        business_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Estimate required resources for implementation."""
        return {
            "personnel": {
                "project_manager": 1,
                "quality_manager": 1,
                "technical_staff": "2-3"
            },
            "training": {
                "initial": "40 hours",
                "ongoing": "10 hours/month"
            },
            "documentation": {
                "effort": "100-150 hours",
                "tools": ["Document management system", "Training platform"]
            }
        }
