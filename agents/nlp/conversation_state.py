"""
Conversation state management.
"""

from dataclasses import dataclass, field
from typing import Dict, Optional
from enum import Enum, auto

class Stage(Enum):
    """Conversation stages."""
    INITIAL = auto()
    BUSINESS_INFO = auto()
    INDUSTRY_SELECTION = auto()
    STATE_SELECTION = auto()
    REQUIREMENTS = auto()
    DOCUMENTATION = auto()
    REVIEW = auto()
    FILING = auto()
    COMPLETE = auto()

@dataclass
class ConversationState:
    """Maintains the state of a conversation."""
    
    # Current stage in the conversation flow
    stage: Stage = Stage.INITIAL
    
    # Information collected during conversation
    collected_info: Dict = field(default_factory=dict)
    
    # Current active agent
    current_agent: Optional[str] = None
    
    # Last recognized intent
    last_intent: Optional[str] = None
    
    # Conversation history
    history: list = field(default_factory=list)
    
    def update_stage(self, new_stage: Stage):
        """Update conversation stage."""
        self.stage = new_stage
    
    def add_info(self, key: str, value: str):
        """Add collected information."""
        self.collected_info[key] = value
    
    def get_info(self, key: str) -> Optional[str]:
        """Get collected information."""
        return self.collected_info.get(key)
    
    def set_agent(self, agent: str):
        """Set current active agent."""
        self.current_agent = agent
    
    def set_intent(self, intent: str):
        """Set last recognized intent."""
        self.last_intent = intent
    
    def add_to_history(self, message: Dict):
        """Add message to conversation history."""
        self.history.append(message)
    
    def clear_history(self):
        """Clear conversation history."""
        self.history = []
    
    def reset(self):
        """Reset conversation state."""
        self.stage = Stage.INITIAL
        self.collected_info = {}
        self.current_agent = None
        self.last_intent = None
        self.history = []
