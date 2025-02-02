"""
Base agent class for LLC formation assistance.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from config.api_config import APIConfig

class BaseAgent(ABC):
    """Base class for specialized agents."""
    
    def __init__(self):
        """Initialize base agent."""
        try:
            # Initialize API configuration
            self.api_config = APIConfig()
            
            # Load API keys for different services (all optional)
            self.openai_key = self.api_config.get_api_key('OPENAI_API_KEY')
            self.anthropic_key = self.api_config.get_api_key('ANTHROPIC_API_KEY')
            self.google_key = self.api_config.get_api_key('GOOGLE_API_KEY')
            self.azure_key = self.api_config.get_api_key('AZURE_API_KEY')
            self.aws_key = self.api_config.get_api_key('AWS_API_KEY')
            self.cohere_key = self.api_config.get_api_key('COHERE_API_KEY')
            
            # Initialize capabilities based on available API keys
            self.capabilities = self._initialize_capabilities()
        
        except Exception as e:
            raise Exception(f"Failed to initialize agent: {str(e)}")
    
    def _initialize_capabilities(self) -> Dict[str, bool]:
        """Initialize agent capabilities based on available API keys."""
        return {
            'advanced_nlp': bool(self.openai_key or self.anthropic_key or self.cohere_key),
            'document_processing': bool(self.azure_key or self.aws_key),
            'data_lookup': bool(self.google_key)
        }
    
    def has_capability(self, capability: str) -> bool:
        """
        Check if agent has a specific capability.
        
        Args:
            capability: Name of capability to check
            
        Returns:
            True if agent has capability, False otherwise
        """
        return self.capabilities.get(capability, False)
    
    @abstractmethod
    async def process_request(self, request: str, context: Dict) -> Dict:
        """
        Process a user request.
        
        Args:
            request: User's request text
            context: Current conversation context
            
        Returns:
            Response dictionary with message and actions
        """
        pass
    
    def _get_required_info(self, context: Dict) -> List[str]:
        """
        Get list of required information fields.
        
        Args:
            context: Current conversation context
            
        Returns:
            List of required information fields
        """
        return []
    
    def _validate_info(self, info: Dict) -> bool:
        """
        Validate collected information.
        
        Args:
            info: Information to validate
            
        Returns:
            True if valid, False otherwise
        """
        return True
    
    def _format_response(self, message: str, actions: List[Dict] = None) -> Dict:
        """
        Format agent response.
        
        Args:
            message: Response message
            actions: Optional list of action buttons
            
        Returns:
            Formatted response dictionary
        """
        response = {'message': message}
        if actions:
            response['actions'] = actions
        return response
