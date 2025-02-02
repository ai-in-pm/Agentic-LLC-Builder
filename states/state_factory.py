"""
Factory for creating state-specific instances.
"""

import importlib
from typing import Dict, Any, Type
from states.base_state import BaseState
from states.state_data import STATE_DATA
from states.requirements.professional_llc import PROFESSIONAL_LLC_REQUIREMENTS
from states.requirements.foreign_llc import FOREIGN_LLC_REQUIREMENTS
from states.requirements.tax import TAX_REGISTRATION_REQUIREMENTS
from states.requirements.regulated_professions import REGULATED_PROFESSIONS

class StateFactory:
    """Factory for creating state-specific instances."""
    
    @staticmethod
    def get_state(state_code: str) -> BaseState:
        """
        Get state-specific implementation.
        
        Args:
            state_code: Two-letter state code (e.g., 'CA' for California)
            
        Returns:
            Instance of state-specific implementation
        """
        try:
            # Import state-specific module
            module = importlib.import_module(f"states.{state_code.lower()}.state")
            
            # Get state class (assumed to be named after the state)
            state_name = STATE_DATA[state_code].get("name", state_code)
            state_class: Type[BaseState] = getattr(module, state_name)
            
            # Create instance with requirements
            return state_class(
                professional_requirements=PROFESSIONAL_LLC_REQUIREMENTS.get(
                    state_code,
                    PROFESSIONAL_LLC_REQUIREMENTS["default"]
                ),
                foreign_requirements=FOREIGN_LLC_REQUIREMENTS.get(
                    state_code,
                    FOREIGN_LLC_REQUIREMENTS["default"]
                ),
                tax_requirements=TAX_REGISTRATION_REQUIREMENTS.get(
                    state_code,
                    TAX_REGISTRATION_REQUIREMENTS["default"]
                ),
                regulated_professions=REGULATED_PROFESSIONS
            )
            
        except ImportError:
            raise ValueError(f"No implementation found for state code: {state_code}")
        except AttributeError:
            raise ValueError(f"Invalid state implementation for state code: {state_code}")

    @staticmethod
    def get_requirements(state_code: str) -> Dict[str, Any]:
        """
        Get comprehensive requirements for a state.
        
        Args:
            state_code: Two-letter state code (e.g., 'CA' for California)
            
        Returns:
            Dictionary containing all requirements for the state
        """
        return {
            "state_data": STATE_DATA.get(state_code, {}),
            "professional_requirements": PROFESSIONAL_LLC_REQUIREMENTS.get(
                state_code,
                PROFESSIONAL_LLC_REQUIREMENTS["default"]
            ),
            "foreign_requirements": FOREIGN_LLC_REQUIREMENTS.get(
                state_code,
                FOREIGN_LLC_REQUIREMENTS["default"]
            ),
            "tax_requirements": TAX_REGISTRATION_REQUIREMENTS.get(
                state_code,
                TAX_REGISTRATION_REQUIREMENTS["default"]
            ),
            "regulated_professions": REGULATED_PROFESSIONS
        }
