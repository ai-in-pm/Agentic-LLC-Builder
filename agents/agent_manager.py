"""
Orchestrates the AI agents involved in LLC formation.
"""

from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime
from agents.legal_architect.agent import LegalArchitectAgent
from agents.hr_strategist.agent import HRStrategistAgent
from agents.financial_expert.agent import FinancialExpertAgent
from agents.governance_officer.agent import GovernanceOfficerAgent
from agents.pmo_director.agent import PMODirectorAgent
from agents.evaluation_analyst.agent import EvaluationAnalystAgent
from agents.iso_agent.agent import ISOAgent
from states.state_factory import StateFactory

@dataclass
class LLCFormationRequest:
    """LLC Formation Request details."""
    business_name: str
    state_code: str
    llc_type: str  # single-member, multi-member, professional, series
    industry: str
    owner_info: List[Dict[str, Any]]
    is_foreign: bool = False
    foreign_state: str = None
    expedited: bool = False
    registered_agent_needed: bool = True
    iso_standards_needed: bool = False

class AgentManager:
    """Manages and coordinates multiple AI agents for LLC formation."""
    
    def __init__(self):
        """Initialize the agent manager with all required agents."""
        self.legal_architect = LegalArchitectAgent()
        self.hr_strategist = HRStrategistAgent()
        self.financial_expert = FinancialExpertAgent()
        self.governance_officer = GovernanceOfficerAgent()
        self.pmo_director = PMODirectorAgent()
        self.evaluation_analyst = EvaluationAnalystAgent()
        self.iso_agent = ISOAgent()
    
    def process_llc_formation(self, request: LLCFormationRequest) -> Dict[str, Any]:
        """
        Process LLC formation request using all agents.
        
        Args:
            request: LLC formation request details
            
        Returns:
            Formation results from all agents
        """
        try:
            # Initialize context
            context = {
                "request": request,
                "state_requirements": StateFactory.get_requirements(request.state_code),
                "start_time": datetime.now(),
                "status": "in_progress",
                "errors": [],
                "warnings": [],
                "results": {}
            }
            
            # Step 1: Project Management Setup
            pmo_results = self.pmo_director.create_formation_workflow(context)
            if pmo_results["status"] != "ready":
                return self._handle_error(context, "PMO setup failed")
            context["results"]["pmo"] = pmo_results
            
            # Step 2: Initial Evaluation
            evaluation_results = self.evaluation_analyst.analyze_formation(context)
            if evaluation_results["status"] != "ready":
                return self._handle_error(context, "Initial evaluation failed")
            context["results"]["evaluation"] = evaluation_results
            
            # Step 3: Legal Formation
            legal_results = self.legal_architect.process_formation(context)
            if legal_results["status"] != "ready":
                return self._handle_error(context, "Legal formation failed")
            context["results"]["legal"] = legal_results
            
            # Step 4: HR Setup
            hr_results = self.hr_strategist.setup_hr_structure(context)
            if hr_results["status"] != "ready":
                return self._handle_error(context, "HR setup failed")
            context["results"]["hr"] = hr_results
            
            # Step 5: Financial Setup
            financial_results = self.financial_expert.setup_financial_structure(context)
            if financial_results["status"] != "ready":
                return self._handle_error(context, "Financial setup failed")
            context["results"]["financial"] = financial_results
            
            # Step 6: Governance Setup
            governance_results = self.governance_officer.review_formation(context)
            if governance_results["status"] != "ready":
                return self._handle_error(context, "Governance setup failed")
            context["results"]["governance"] = governance_results
            
            # Step 7: ISO Standards (if requested)
            if request.iso_standards_needed:
                iso_results = self.iso_agent.evaluate_iso_requirements({
                    "business_name": request.business_name,
                    "industry": request.industry,
                    "llc_type": request.llc_type,
                    "state": request.state_code
                })
                if not iso_results["recommended_standards"]:
                    context["warnings"].append("No applicable ISO standards found")
                context["results"]["iso"] = iso_results
            
            # Step 8: Final Evaluation
            final_evaluation = self.evaluation_analyst.analyze_formation(context)
            context["results"]["final_evaluation"] = final_evaluation
            
            # Update status
            context["status"] = "completed"
            context["completion_time"] = datetime.now()
            
            return self._prepare_response(context)
            
        except Exception as e:
            return self._handle_error(context, str(e))
    
    def _handle_error(self, context: Dict[str, Any], error: str) -> Dict[str, Any]:
        """Handle errors during formation process."""
        context["status"] = "failed"
        context["errors"].append(error)
        return self._prepare_response(context)
    
    def _prepare_response(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare final response from context."""
        return {
            "status": context["status"],
            "errors": context["errors"],
            "warnings": context["warnings"],
            "results": context["results"],
            "timeline": {
                "start": context["start_time"],
                "end": context.get("completion_time", datetime.now())
            }
        }
