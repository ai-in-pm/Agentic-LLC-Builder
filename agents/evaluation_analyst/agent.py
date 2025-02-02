"""
Evaluation Analyst Agent for analyzing and evaluating business formation decisions.
"""

from typing import Dict, Any, List
from states.state_factory import StateFactory
from ..job_descriptions import JobDescriptionGenerator

class EvaluationAnalystAgent:
    """
    Evaluation Analyst Agent responsible for analyzing business formation decisions
    and providing recommendations.
    """
    
    def __init__(self):
        """Initialize the Evaluation Analyst Agent."""
        self.job_generator = JobDescriptionGenerator()
    
    def analyze_formation(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze LLC formation decisions and provide recommendations.
        
        Args:
            context: Formation context including request and state requirements
            
        Returns:
            Analysis results and recommendations
        """
        try:
            state = StateFactory.get_state(context["request"].state_code)
            
            # Evaluate state selection
            state_analysis = self._evaluate_state_selection(context)
            
            # Evaluate structure selection
            structure_analysis = self._evaluate_structure_selection(context)
            
            # Analyze costs and benefits
            cost_benefit = self._analyze_cost_benefit(context)
            
            # Generate recommendations
            recommendations = self._generate_recommendations(context)
            
            # Get required job roles
            job_roles = self.get_required_job_roles()
            
            return {
                "status": "ready",
                "state_analysis": state_analysis,
                "structure_analysis": structure_analysis,
                "cost_benefit_analysis": cost_benefit,
                "recommendations": recommendations,
                "risks": self._identify_risks(context),
                "job_roles": job_roles,
                "next_steps": self._generate_next_steps(context),
                "warnings": self._generate_warnings(context)
            }
            
        except Exception as e:
            context["errors"].append(f"Analysis error: {str(e)}")
            return self._generate_error_response(context)
    
    def get_required_job_roles(self) -> List[Dict[str, Any]]:
        """Get required job roles for evaluation and analysis operations."""
        return self.job_generator.create_evaluation_analyst_jobs()
    
    def _evaluate_state_selection(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate state selection."""
        state = StateFactory.get_state(context["request"].state_code)
        
        return {
            "tax_environment": {
                "score": self._calculate_tax_score(state),
                "factors": {
                    "income_tax": state.get_income_tax_rate(),
                    "sales_tax": state.get_sales_tax_rate(),
                    "tax_incentives": state.get_tax_incentives()
                }
            },
            "formation_costs": {
                "score": self._calculate_cost_score(state),
                "factors": {
                    "filing_fees": state.get_filing_fees(),
                    "registered_agent": state.get_registered_agent_requirements(),
                    "publication": state.get_publication_requirements()
                }
            },
            "business_environment": {
                "score": self._calculate_environment_score(state),
                "factors": {
                    "processing_time": state.get_processing_time(),
                    "regulatory_burden": state.get_regulatory_burden(),
                    "business_support": state.get_business_support_programs()
                }
            }
        }
    
    def _evaluate_structure_selection(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate structure selection."""
        state = StateFactory.get_state(context["request"].state_code)
        
        return {
            "liability_protection": {
                "score": self._calculate_liability_score(context),
                "factors": {
                    "personal_asset_protection": "Strong",
                    "veil_piercing_risk": "Low",
                    "insurance_requirements": state.get_insurance_requirements()
                }
            },
            "management_flexibility": {
                "score": self._calculate_management_score(context),
                "factors": {
                    "decision_making": "Flexible",
                    "ownership_transfer": "Unrestricted",
                    "governance_options": "Multiple"
                }
            },
            "compliance_requirements": {
                "score": self._calculate_compliance_score(context),
                "factors": {
                    "annual_requirements": state.get_annual_requirements(),
                    "record_keeping": state.get_record_keeping_requirements(),
                    "reporting_obligations": state.get_reporting_requirements()
                }
            }
        }
    
    def _analyze_cost_benefit(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze costs and benefits."""
        state = StateFactory.get_state(context["request"].state_code)
        
        return {
            "costs": {
                "initial": {
                    "filing_fees": state.get_filing_fees(),
                    "registered_agent": state.get_registered_agent_fees(),
                    "legal_services": self._estimate_legal_costs(context),
                    "total": self._calculate_total_initial_costs(context)
                },
                "ongoing": {
                    "annual_fees": state.get_annual_fees(),
                    "compliance": self._estimate_compliance_costs(context),
                    "professional_services": self._estimate_service_costs(context),
                    "total": self._calculate_total_ongoing_costs(context)
                }
            },
            "benefits": {
                "primary": [
                    "Limited liability protection",
                    "Tax flexibility",
                    "Professional credibility",
                    "Perpetual existence"
                ],
                "secondary": [
                    "Banking separation",
                    "Business credit building",
                    "Contract capabilities",
                    "Growth flexibility"
                ],
                "financial": self._estimate_financial_benefits(context)
            },
            "roi": self._calculate_roi(context)
        }
    
    def _generate_recommendations(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate recommendations."""
        state = StateFactory.get_state(context["request"].state_code)
        
        recommendations = [
            {
                "category": "Structure",
                "suggestion": "Proceed with LLC formation",
                "rationale": "Optimal balance of liability protection and flexibility",
                "priority": "High"
            },
            {
                "category": "Management",
                "suggestion": "Member-managed" if len(context["request"].owner_info) <= 3 else "Manager-managed",
                "rationale": "Based on number of owners and operational needs",
                "priority": "High"
            },
            {
                "category": "Compliance",
                "suggestion": "Implement compliance tracking system",
                "rationale": "Ensure adherence to state requirements",
                "priority": "Medium"
            }
        ]
        
        # Add state-specific recommendations
        state_recommendations = state.get_formation_recommendations()
        if state_recommendations:
            recommendations.extend(state_recommendations)
        
        return recommendations
    
    def _identify_risks(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify formation risks."""
        state = StateFactory.get_state(context["request"].state_code)
        
        risks = [
            {
                "category": "Compliance",
                "description": "Missing state-specific requirements",
                "impact": "High",
                "mitigation": "Regular compliance audits"
            },
            {
                "category": "Financial",
                "description": "Unexpected formation costs",
                "impact": "Medium",
                "mitigation": "Maintain contingency budget"
            },
            {
                "category": "Operational",
                "description": "Inadequate record keeping",
                "impact": "Medium",
                "mitigation": "Implement record keeping system"
            }
        ]
        
        # Add state-specific risks
        state_risks = state.get_formation_risks()
        if state_risks:
            risks.extend(state_risks)
        
        return risks
    
    def _calculate_tax_score(self, state) -> float:
        """Calculate tax environment score."""
        tax_rate = state.get_income_tax_rate()
        if tax_rate == 0:
            return 1.0
        elif tax_rate < 5:
            return 0.8
        elif tax_rate < 10:
            return 0.6
        else:
            return 0.4
    
    def _calculate_cost_score(self, state) -> float:
        """Calculate formation cost score."""
        filing_fees = state.get_filing_fees()
        if filing_fees < 100:
            return 1.0
        elif filing_fees < 250:
            return 0.8
        elif filing_fees < 500:
            return 0.6
        else:
            return 0.4
    
    def _calculate_environment_score(self, state) -> float:
        """Calculate business environment score."""
        processing_time = state.get_processing_time()
        if processing_time <= 2:
            return 1.0
        elif processing_time <= 5:
            return 0.8
        elif processing_time <= 10:
            return 0.6
        else:
            return 0.4
    
    def _calculate_liability_score(self, context: Dict[str, Any]) -> float:
        """Calculate liability protection score."""
        return 0.9  # LLCs provide strong liability protection
    
    def _calculate_management_score(self, context: Dict[str, Any]) -> float:
        """Calculate management flexibility score."""
        return 0.8  # LLCs offer good management flexibility
    
    def _calculate_compliance_score(self, context: Dict[str, Any]) -> float:
        """Calculate compliance burden score."""
        state = StateFactory.get_state(context["request"].state_code)
        requirements = len(state.get_annual_requirements())
        if requirements <= 2:
            return 0.9
        elif requirements <= 4:
            return 0.7
        else:
            return 0.5
    
    def _estimate_legal_costs(self, context: Dict[str, Any]) -> float:
        """Estimate legal service costs."""
        return 500.0  # Base legal service cost
    
    def _estimate_compliance_costs(self, context: Dict[str, Any]) -> float:
        """Estimate annual compliance costs."""
        return 300.0  # Base compliance cost
    
    def _estimate_service_costs(self, context: Dict[str, Any]) -> float:
        """Estimate professional service costs."""
        return 1000.0  # Base professional service cost
    
    def _calculate_total_initial_costs(self, context: Dict[str, Any]) -> float:
        """Calculate total initial costs."""
        state = StateFactory.get_state(context["request"].state_code)
        return (state.get_filing_fees() +
                state.get_registered_agent_fees() +
                self._estimate_legal_costs(context))
    
    def _calculate_total_ongoing_costs(self, context: Dict[str, Any]) -> float:
        """Calculate total ongoing costs."""
        state = StateFactory.get_state(context["request"].state_code)
        return (state.get_annual_fees() +
                self._estimate_compliance_costs(context) +
                self._estimate_service_costs(context))
    
    def _estimate_financial_benefits(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Estimate financial benefits."""
        return {
            "tax_savings": "Variable based on income",
            "liability_protection": "Significant",
            "business_opportunities": "Enhanced",
            "asset_protection": "Strong"
        }
    
    def _calculate_roi(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate return on investment."""
        initial_costs = self._calculate_total_initial_costs(context)
        ongoing_costs = self._calculate_total_ongoing_costs(context)
        
        return {
            "timeframe": "1-3 years",
            "factors": {
                "initial_investment": initial_costs,
                "annual_costs": ongoing_costs,
                "potential_benefits": "Variable based on business success"
            },
            "notes": [
                "ROI varies by business type and success",
                "Consider both tangible and intangible benefits",
                "Factor in risk mitigation value"
            ]
        }
    
    def _generate_next_steps(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate next steps for evaluation process."""
        return [
            {
                "step": "Complete Requirements Review",
                "priority": "High",
                "timeline": "1-2 days"
            },
            {
                "step": "Finalize Risk Assessment",
                "priority": "High",
                "timeline": "2-3 days"
            },
            {
                "step": "Present Recommendations",
                "priority": "Medium",
                "timeline": "1-2 days"
            }
        ]
    
    def _generate_warnings(self, context: Dict[str, Any]) -> List[str]:
        """Generate warnings for evaluation process."""
        return [
            "Ensure all requirements are thoroughly reviewed",
            "Address identified risks promptly",
            "Monitor progress against success metrics"
        ]
    
    def _generate_error_response(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "status": "error",
            "errors": context.get("errors", []),
            "warnings": self._generate_warnings(context)
        }
