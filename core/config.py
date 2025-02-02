from typing import Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the LLC Generator system."""
    
    # API Configuration
    API_KEYS = {
        "openai": os.getenv("OPENAI_API_KEY"),
        "anthropic": os.getenv("ANTHROPIC_API_KEY"),
        "groq": os.getenv("GROQ_API_KEY"),
        "google": os.getenv("GOOGLE_API_KEY"),
        "cohere": os.getenv("COHERE_API_KEY"),
        "emergence": os.getenv("EMERGENCEAI_API_KEY")
    }
    
    # Model Configuration
    MODELS = {
        "legal_architect": "gpt-4",
        "hr_strategist": "claude-2",
        "financial_expert": "mixtral-8x7b",
        "governance_officer": "gemini-pro",
        "pmo_director": "command-nightly",
        "evaluation_analyst": "emergence-latest"
    }
    
    # System Paths
    PATHS = {
        "templates": "templates",
        "legal_templates": "templates/legal",
        "hr_templates": "templates/hr",
        "financial_templates": "templates/financial",
        "governance_templates": "templates/governance",
        "pmo_templates": "templates/pmo"
    }
    
    # Validation Settings
    VALIDATION = {
        "required_documents": [
            "articles_of_organization",
            "operating_agreement",
            "ein_application"
        ],
        "required_compliance_checks": [
            "state_requirements",
            "federal_requirements",
            "industry_requirements"
        ]
    }
    
    # Processing Settings
    PROCESSING = {
        "max_retries": 3,
        "timeout_seconds": 300,
        "batch_size": 10
    }
    
    @classmethod
    def get_api_key(cls, service: str) -> str:
        """Get API key for a specific service."""
        return cls.API_KEYS.get(service, "")
    
    @classmethod
    def get_model(cls, agent_type: str) -> str:
        """Get model name for a specific agent type."""
        return cls.MODELS.get(agent_type, "gpt-4")
    
    @classmethod
    def get_path(cls, path_type: str) -> str:
        """Get system path for a specific type."""
        return cls.PATHS.get(path_type, "")
