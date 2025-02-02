"""
Industry Specialist Agent for handling industry-specific LLC formation requirements.
"""

from typing import Dict, List, Optional
from ..base_agent import BaseAgent, AgentCapability
from rich.table import Table
from rich.panel import Panel

class IndustrySpecialistAgent(BaseAgent):
    """Specialized agent for industry-specific guidance."""
    
    def _get_title(self) -> str:
        return "Industry Specialist"
    
    def _get_introduction(self) -> str:
        return (
            "I'm your Industry Specialist, ready to provide tailored guidance "
            "for your specific business sector. I can help with industry-specific "
            "regulations, licensing, and best practices."
        )
    
    def _get_capabilities(self) -> List[AgentCapability]:
        return [
            AgentCapability(
                name="tech_startup",
                description="Guidance for technology startups",
                examples=[
                    "starting a tech company",
                    "software startup",
                    "SaaS business"
                ],
                required_context=["industry", "state_code"]
            ),
            AgentCapability(
                name="ecommerce",
                description="E-commerce business formation",
                examples=[
                    "online store",
                    "e-commerce business",
                    "digital marketplace"
                ],
                required_context=["industry", "state_code"]
            ),
            AgentCapability(
                name="professional_services",
                description="Professional services LLC formation",
                examples=[
                    "consulting firm",
                    "law practice",
                    "accounting firm"
                ],
                required_context=["industry", "state_code", "license_info"]
            ),
            AgentCapability(
                name="healthcare",
                description="Healthcare business formation",
                examples=[
                    "medical practice",
                    "healthcare provider",
                    "wellness center"
                ],
                required_context=["industry", "state_code", "license_info"]
            ),
            AgentCapability(
                name="real_estate",
                description="Real estate business formation",
                examples=[
                    "real estate agency",
                    "property management",
                    "real estate investment"
                ],
                required_context=["industry", "state_code"]
            ),
            AgentCapability(
                name="restaurant",
                description="Restaurant and hospitality business formation",
                examples=[
                    "restaurant business",
                    "cafe",
                    "food service"
                ],
                required_context=["industry", "state_code"]
            ),
            AgentCapability(
                name="manufacturing",
                description="Manufacturing business formation",
                examples=[
                    "manufacturing company",
                    "production facility",
                    "factory"
                ],
                required_context=["industry", "state_code"]
            ),
            AgentCapability(
                name="creative",
                description="Creative services business formation",
                examples=[
                    "design studio",
                    "marketing agency",
                    "media production"
                ],
                required_context=["industry", "state_code"]
            )
        ]
    
    async def _generate_response(
        self, capability: AgentCapability, user_input: str
    ) -> Dict:
        """Generate industry-specific response."""
        industry_info = self._get_industry_info(capability.name)
        
        # Create visual components
        requirements_table = self._create_requirements_table(industry_info)
        timeline = self.create_visual_guide(
            f"{industry_info['name']} LLC Formation Timeline",
            industry_info['timeline']
        )
        
        return {
            'message': self._format_industry_response(industry_info),
            'visual': {
                'requirements': requirements_table,
                'timeline': timeline
            },
            'actions': [
                {
                    'type': 'button',
                    'text': 'View Detailed Requirements'
                },
                {
                    'type': 'button',
                    'text': 'Start Formation Process'
                },
                {
                    'type': 'button',
                    'text': 'Schedule Consultation'
                }
            ]
        }
    
    def _get_industry_info(self, industry_type: str) -> Dict:
        """Get detailed information for specific industry."""
        industry_data = {
            'tech_startup': {
                'name': 'Technology Startup',
                'requirements': [
                    ('IP Protection', 'Essential', 'Patents, Trademarks, NDAs'),
                    ('Data Privacy', 'Required', 'GDPR, CCPA Compliance'),
                    ('Tech Insurance', 'Required', 'Cyber Liability Coverage'),
                    ('Dev Contracts', 'Essential', 'Contractor Agreements')
                ],
                'timeline': [
                    'Business Plan & MVP Definition',
                    'IP Protection Setup',
                    'Technical Infrastructure',
                    'Privacy Compliance',
                    'Funding Structure',
                    'Launch Preparation'
                ]
            },
            'ecommerce': {
                'name': 'E-commerce Business',
                'requirements': [
                    ('Payment Processing', 'Required', 'PCI Compliance'),
                    ('Sales Tax', 'Required', 'Multi-state Registration'),
                    ('Shipping', 'Essential', 'Logistics Setup'),
                    ('Returns Policy', 'Required', 'Consumer Protection')
                ],
                'timeline': [
                    'Platform Selection',
                    'Payment Gateway Setup',
                    'Tax Registration',
                    'Shipping Integration',
                    'Inventory System',
                    'Launch Preparation'
                ]
            },
            # Add more industries here
        }
        
        return industry_data.get(industry_type, {
            'name': 'Generic Business',
            'requirements': [
                ('Business License', 'Required', 'State Registration'),
                ('Insurance', 'Required', 'General Liability'),
                ('Permits', 'Varies', 'Local Requirements'),
                ('Compliance', 'Required', 'Industry Standards')
            ],
            'timeline': [
                'Business Planning',
                'Registration',
                'Licensing',
                'Setup Operations',
                'Launch Preparation'
            ]
        })
    
    def _create_requirements_table(self, industry_info: Dict) -> Table:
        """Create a requirements table for the industry."""
        table = Table(title=f"{industry_info['name']} Requirements")
        
        table.add_column("Requirement")
        table.add_column("Status")
        table.add_column("Details")
        
        for req in industry_info['requirements']:
            table.add_row(*req)
        
        return table
    
    def _format_industry_response(self, industry_info: Dict) -> str:
        """Format the response message for the industry."""
        return (
            f"Let me help you set up your {industry_info['name']}. "
            "I've prepared a detailed breakdown of requirements and a "
            "timeline for your LLC formation. Here are the key steps "
            "and requirements specific to your industry.\n\n"
            "Would you like to review the detailed requirements or "
            "start the formation process?"
        )
