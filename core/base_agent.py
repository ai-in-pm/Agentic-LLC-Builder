from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class BaseAgent(ABC):
    """Base class for all AI agents in the LLC Generator system."""
    
    def __init__(self, api_key: str, model_name: str = "gpt-4"):
        self.api_key = api_key
        self.model_name = model_name
        self.scratchpad: List[Dict[str, Any]] = []
        self._initialize_agent()
    
    @abstractmethod
    def _initialize_agent(self) -> None:
        """Initialize agent-specific components and configurations."""
        pass
    
    @abstractmethod
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process input data and return results."""
        pass
    
    def add_to_scratchpad(self, note: Dict[str, Any]) -> None:
        """Add a note to the agent's scratchpad for iterative processing."""
        self.scratchpad.append({
            "timestamp": datetime.now().isoformat(),
            "content": note
        })
    
    def get_scratchpad_history(self) -> List[Dict[str, Any]]:
        """Retrieve the agent's processing history."""
        return self.scratchpad
    
    @abstractmethod
    async def validate_output(self, output: Dict[str, Any]) -> bool:
        """Validate the output before returning results."""
        pass
    
    @abstractmethod
    async def self_improve(self, feedback: Dict[str, Any]) -> None:
        """Implement self-improvement based on feedback."""
        pass
