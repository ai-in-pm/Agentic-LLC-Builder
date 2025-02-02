"""
Legal advisor agent for LLC formation assistance.
"""

from typing import Dict, List
from ..base_agent import BaseAgent

class LegalAdvisorAgent(BaseAgent):
    """Legal advisor agent for LLC formation."""
    
    def _validate_api_keys(self):
        """Validate required API keys for legal advisor."""
        required_keys = [
            'ANTHROPIC_API_KEY',  # For legal analysis
            'AZURE_API_KEY',      # For document processing
            'COHERE_API_KEY'      # For compliance checking
        ]
        
        missing_keys = []
        for key in required_keys:
            if not self.api_config.validate_key(key):
                missing_keys.append(key)
        
        if missing_keys:
            raise ValueError(
                f"Missing required API keys for legal advisor: {', '.join(missing_keys)}"
            )
    
    async def process_request(self, request: str, context: Dict) -> Dict:
        """
        Process a legal consultation request.
        
        Args:
            request: User's request text
            context: Current conversation context
            
        Returns:
            Response dictionary with message and actions
        """
        try:
            # Example of using Anthropic API for legal analysis
            if 'state_requirements' not in context:
                if self.has_capability('advanced_nlp'):
                    # Use advanced NLP if available
                    # Here you would use self.anthropic_key to make API calls
                    return self._format_response(
                        "I'll analyze the legal requirements for your LLC. "
                        "Which state are you planning to form your LLC in?",
                        actions=[
                            {'text': 'Select State'},
                            {'text': 'Compare States'}
                        ]
                    )
                else:
                    # Fallback to basic state selection
                    return self._format_response(
                        "Please select the state where you'd like to form your LLC. "
                        "I'll provide you with the basic requirements.",
                        actions=[
                            {'text': 'Select State'},
                            {'text': 'View State List'}
                        ]
                    )
            
            # Example of using Azure API for document processing
            if 'operating_agreement' not in context:
                if self.has_capability('document_processing'):
                    # Use document processing if available
                    # Here you would use self.azure_key to make API calls
                    return self._format_response(
                        "I can help you create a customized Operating Agreement "
                        "based on your specific needs and state requirements. "
                        "Would you like to use a standard template or create a custom one?",
                        actions=[
                            {'text': 'Standard Template'},
                            {'text': 'Custom Agreement'}
                        ]
                    )
                else:
                    # Fallback to basic template
                    return self._format_response(
                        "I can provide you with a basic Operating Agreement template. "
                        "Would you like to proceed?",
                        actions=[
                            {'text': 'Use Template'},
                            {'text': 'Skip For Now'}
                        ]
                    )
            
            # Example of using Cohere API for compliance checking
            if 'compliance_check' not in context:
                if self.has_capability('advanced_nlp'):
                    # Use advanced NLP if available
                    # Here you would use self.cohere_key to make API calls
                    return self._format_response(
                        "I'll perform a comprehensive compliance check for your LLC formation. "
                        "This will ensure you meet all state requirements and regulations.",
                        actions=[
                            {'text': 'Start Compliance Check'},
                            {'text': 'Review Requirements First'}
                        ]
                    )
                else:
                    # Fallback to basic checklist
                    return self._format_response(
                        "Let's review a basic compliance checklist for your LLC formation. "
                        "This will help ensure you're meeting the main requirements.",
                        actions=[
                            {'text': 'View Checklist'},
                            {'text': 'Skip For Now'}
                        ]
                    )
            
            return self._format_response(
                "Great! I have reviewed all legal aspects of your LLC formation. "
                "You're ready to proceed with the filing process."
            )
        
        except Exception as e:
            raise Exception(f"Error processing legal consultation request: {str(e)}")
    
    def _get_required_info(self, context: Dict) -> List[str]:
        """Get required information for legal consultation."""
        return ['state_requirements', 'operating_agreement', 'compliance_check']
