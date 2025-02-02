"""
Job descriptions for both human and AI agent positions.
"""

from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class JobDescription:
    """Represents a job description for either human or AI agent positions."""
    title: str
    type: str  # "Human" or "AI Agent"
    description: str
    responsibilities: List[str]
    requirements: List[str]
    salary_range: str = None  # Only for human positions
    capabilities: List[str] = None  # Only for AI agents
    integration_points: List[str] = None  # Only for AI agents

class JobDescriptionGenerator:
    """Generates job descriptions for various roles."""
    
    @staticmethod
    def create_legal_architect_jobs() -> List[Dict[str, Any]]:
        """Create legal architect related job descriptions."""
        return [
            {
                "title": "Legal Compliance Officer",
                "type": "Human",
                "description": "Oversee legal compliance and regulatory requirements",
                "responsibilities": [
                    "Monitor and ensure compliance with state and federal regulations",
                    "Review and update legal documents",
                    "Provide legal guidance to management",
                    "Manage regulatory reporting requirements"
                ],
                "requirements": [
                    "JD degree required",
                    "5+ years corporate law experience",
                    "State bar admission",
                    "Experience with LLC formations"
                ],
                "salary_range": "$120,000 - $180,000"
            },
            {
                "title": "Legal Document Assistant",
                "type": "AI Agent",
                "description": "Automate legal document preparation and review",
                "capabilities": [
                    "Generate legal documents",
                    "Review contracts and agreements",
                    "Track regulatory changes",
                    "Maintain compliance records"
                ],
                "requirements": [
                    "Natural language processing",
                    "Legal document analysis",
                    "Pattern recognition",
                    "Regulatory compliance checking"
                ],
                "integration_points": [
                    "Document management system",
                    "E-signature platform",
                    "Compliance tracking system"
                ]
            }
        ]
    
    @staticmethod
    def create_hr_strategist_jobs() -> List[Dict[str, Any]]:
        """Create HR strategist related job descriptions."""
        return [
            {
                "title": "HR Director",
                "type": "Human",
                "description": "Lead HR strategy and operations",
                "responsibilities": [
                    "Develop HR policies and procedures",
                    "Manage recruitment and onboarding",
                    "Oversee benefits and compensation",
                    "Handle employee relations"
                ],
                "requirements": [
                    "Bachelor's in HR or related field",
                    "7+ years HR experience",
                    "SHRM-SCP or SPHR certification",
                    "Strong leadership skills"
                ],
                "salary_range": "$100,000 - $150,000"
            },
            {
                "title": "HR Process Automation Agent",
                "type": "AI Agent",
                "description": "Automate HR processes and workflows",
                "capabilities": [
                    "Process employee documentation",
                    "Generate HR reports",
                    "Track employee metrics",
                    "Automate routine HR tasks"
                ],
                "requirements": [
                    "Process automation",
                    "Data analysis",
                    "Document processing",
                    "Workflow optimization"
                ],
                "integration_points": [
                    "HRIS system",
                    "Payroll system",
                    "Document management system"
                ]
            }
        ]
    
    @staticmethod
    def create_financial_expert_jobs() -> List[Dict[str, Any]]:
        """Create financial expert related job descriptions."""
        return [
            {
                "title": "Financial Controller",
                "type": "Human",
                "description": "Oversee financial operations and reporting",
                "responsibilities": [
                    "Manage financial reporting",
                    "Oversee accounting operations",
                    "Ensure tax compliance",
                    "Develop financial strategies"
                ],
                "requirements": [
                    "CPA required",
                    "7+ years accounting experience",
                    "Master's in Finance/Accounting preferred",
                    "Experience with ERP systems"
                ],
                "salary_range": "$110,000 - $160,000"
            },
            {
                "title": "Financial Analysis Agent",
                "type": "AI Agent",
                "description": "Perform financial analysis and reporting",
                "capabilities": [
                    "Generate financial reports",
                    "Analyze financial data",
                    "Monitor financial metrics",
                    "Forecast financial trends"
                ],
                "requirements": [
                    "Financial modeling",
                    "Data analysis",
                    "Report generation",
                    "Pattern recognition"
                ],
                "integration_points": [
                    "Accounting system",
                    "ERP system",
                    "Business intelligence tools"
                ]
            }
        ]
    
    @staticmethod
    def create_governance_officer_jobs() -> List[Dict[str, Any]]:
        """Create governance officer related job descriptions."""
        return [
            {
                "title": "Corporate Governance Officer",
                "type": "Human",
                "description": "Oversee corporate governance and compliance",
                "responsibilities": [
                    "Develop governance frameworks",
                    "Ensure regulatory compliance",
                    "Manage board relations",
                    "Oversee policy implementation"
                ],
                "requirements": [
                    "Master's in Business or Law",
                    "10+ years governance experience",
                    "Certified Corporate Governance Professional",
                    "Strong leadership skills"
                ],
                "salary_range": "$130,000 - $190,000"
            },
            {
                "title": "Governance Monitoring Agent",
                "type": "AI Agent",
                "description": "Monitor and report on governance compliance",
                "capabilities": [
                    "Track governance metrics",
                    "Generate compliance reports",
                    "Monitor policy implementation",
                    "Identify governance risks"
                ],
                "requirements": [
                    "Policy analysis",
                    "Risk assessment",
                    "Compliance monitoring",
                    "Report generation"
                ],
                "integration_points": [
                    "Governance management system",
                    "Risk management system",
                    "Board portal"
                ]
            }
        ]
    
    @staticmethod
    def create_pmo_director_jobs() -> List[Dict[str, Any]]:
        """Create PMO director related job descriptions."""
        return [
            {
                "title": "Project Management Office Director",
                "type": "Human",
                "description": "Lead project management office and oversee project portfolio",
                "responsibilities": [
                    "Develop project management frameworks",
                    "Oversee project portfolio",
                    "Manage resource allocation",
                    "Drive project success"
                ],
                "requirements": [
                    "PMP certification required",
                    "10+ years project management experience",
                    "Master's in Project Management preferred",
                    "Strong leadership skills"
                ],
                "salary_range": "$120,000 - $180,000"
            },
            {
                "title": "Project Automation Agent",
                "type": "AI Agent",
                "description": "Automate project management processes",
                "capabilities": [
                    "Track project metrics",
                    "Generate project reports",
                    "Optimize resource allocation",
                    "Identify project risks"
                ],
                "requirements": [
                    "Project analytics",
                    "Resource optimization",
                    "Risk assessment",
                    "Automation capabilities"
                ],
                "integration_points": [
                    "Project management system",
                    "Resource management system",
                    "Time tracking system"
                ]
            }
        ]
    
    @staticmethod
    def create_evaluation_analyst_jobs() -> List[Dict[str, Any]]:
        """Create evaluation analyst related job descriptions."""
        return [
            {
                "title": "Business Analysis Director",
                "type": "Human",
                "description": "Lead business analysis and evaluation initiatives",
                "responsibilities": [
                    "Conduct business analysis",
                    "Evaluate business processes",
                    "Recommend improvements",
                    "Track performance metrics"
                ],
                "requirements": [
                    "CBAP certification preferred",
                    "8+ years business analysis experience",
                    "Master's in Business or related field",
                    "Strong analytical skills"
                ],
                "salary_range": "$100,000 - $150,000"
            },
            {
                "title": "Analysis Automation Agent",
                "type": "AI Agent",
                "description": "Automate business analysis processes",
                "capabilities": [
                    "Process analysis",
                    "Data visualization",
                    "Performance monitoring",
                    "Trend analysis"
                ],
                "requirements": [
                    "Data analysis",
                    "Process modeling",
                    "Statistical analysis",
                    "Machine learning"
                ],
                "integration_points": [
                    "Business intelligence tools",
                    "Process mining tools",
                    "Analytics platforms"
                ]
            }
        ]
    
