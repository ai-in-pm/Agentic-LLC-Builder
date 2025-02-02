"""
Configuration manager for API keys and settings.
"""

import os
from typing import Dict, Optional
from dotenv import load_dotenv

class APIConfig:
    """Manages API configurations and keys."""
    
    def __init__(self):
        """Initialize API configuration."""
        # Load environment variables from .env file
        load_dotenv()
        
        # All possible API keys
        self.available_keys = [
            'OPENAI_API_KEY',
            'ANTHROPIC_API_KEY',
            'GOOGLE_API_KEY',
            'AZURE_API_KEY',
            'AWS_API_KEY',
            'COHERE_API_KEY'
        ]
        
        # Load API keys
        self.api_keys = self._load_api_keys()
    
    def _load_api_keys(self) -> Dict[str, str]:
        """Load API keys from environment variables."""
        return {
            key: os.getenv(key)
            for key in self.available_keys
            if os.getenv(key)  # Only include keys that are present
        }
    
    def get_api_key(self, key_name: str) -> Optional[str]:
        """
        Get API key by name.
        
        Args:
            key_name: Name of the API key to retrieve
            
        Returns:
            API key if found, None otherwise
        """
        return self.api_keys.get(key_name)
    
    def get_all_keys(self) -> Dict[str, str]:
        """
        Get all API keys.
        
        Returns:
            Dictionary of all API keys
        """
        return self.api_keys.copy()
    
    def validate_key(self, key_name: str) -> bool:
        """
        Validate if an API key exists and is not empty.
        
        Args:
            key_name: Name of the API key to validate
            
        Returns:
            True if key exists and is not empty, False otherwise
        """
        key = self.get_api_key(key_name)
        return bool(key and key.strip())
