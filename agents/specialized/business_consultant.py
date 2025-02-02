"""
Business consultant agent for LLC formation assistance.
"""

from typing import Dict, List
from ..base_agent import BaseAgent

class BusinessConsultantAgent(BaseAgent):
    """Business consultant agent for LLC formation."""
    
    async def process_request(self, request: str, context: Dict) -> Dict:
        """
        Process a business consultation request.
        
        Args:
            request: User's request text
            context: Current conversation context
            
        Returns:
            Response dictionary with message and actions
        """
        try:
            # Example of using OpenAI API for advanced processing
            if 'business_type' not in context:
                if self.has_capability('advanced_nlp'):
                    # Use advanced NLP if available
                    # Here you would use self.openai_key to make API calls
                    return self._format_response(
                        "Let me analyze your business needs. "
                        "What type of business are you planning to start?",
                        actions=[
                            {'text': 'Service-based Business'},
                            {'text': 'Product-based Business'},
                            {'text': 'Online Business'},
                            {'text': 'Professional Practice'}
                        ]
                    )
                else:
                    # Fallback to basic processing
                    return self._format_response(
                        "What type of business would you like to start?",
                        actions=[
                            {'text': 'Service-based Business'},
                            {'text': 'Product-based Business'},
                            {'text': 'Online Business'},
                            {'text': 'Professional Practice'}
                        ]
                    )
            
            # Example of using Google API for market research
            if 'market_research' not in context:
                if self.has_capability('data_lookup'):
                    # Use data lookup if available
                    # Here you would use self.google_key to make API calls
                    return self._format_response(
                        "I can perform detailed market research for your business. "
                        "Would you like me to analyze the competition in your area?",
                        actions=[
                            {'text': 'Analyze Competition'},
                            {'text': 'Skip Market Research'}
                        ]
                    )
                else:
                    # Fallback to basic guidance
                    return self._format_response(
                        "Would you like some guidance on how to research your market?",
                        actions=[
                            {'text': 'Get Research Tips'},
                            {'text': 'Skip Market Research'}
                        ]
                    )
            
            # Example of using AWS for document processing
            if 'business_plan' not in context:
                if self.has_capability('document_processing'):
                    # Use document processing if available
                    # Here you would use self.aws_key to make API calls
                    return self._format_response(
                        "Based on your business type and market research, "
                        "I can help you create a customized business plan. "
                        "Would you like to start with a template?",
                        actions=[
                            {'text': 'Use Template'},
                            {'text': 'Custom Plan'}
                        ]
                    )
                else:
                    # Fallback to basic template
                    return self._format_response(
                        "I can provide you with a basic business plan template. "
                        "Would you like to use it?",
                        actions=[
                            {'text': 'Use Template'},
                            {'text': 'Skip Business Plan'}
                        ]
                    )
            
            return self._format_response(
                "Great! I have all the information needed for your business consultation. "
                "Let's move on to selecting your state of formation."
            )
        
        except Exception as e:
            raise Exception(f"Error processing business consultation request: {str(e)}")
    
    def _get_required_info(self, context: Dict) -> List[str]:
        """Get required information for business consultation."""
        return ['business_type', 'market_research', 'business_plan']
