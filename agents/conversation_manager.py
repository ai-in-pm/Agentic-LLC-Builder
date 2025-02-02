"""
Conversation Manager for handling user interactions and agent delegation.
"""

from typing import Dict, List, Optional, Tuple
from .agent_manager import AgentManager
from .nlp.enhanced_processor import EnhancedNLPProcessor, Intent
from .nlp.conversation_state import ConversationState, Stage

class ConversationManager:
    """Manages conversations and delegates to appropriate agents."""
    
    def __init__(self):
        """Initialize conversation manager."""
        try:
            self.agent_manager = AgentManager()
            self.nlp_processor = EnhancedNLPProcessor()
            self.state = ConversationState()
            
            # Initialize consultation flow
            self._consultation_flow = {
                Stage.INITIAL: {
                    'next': Stage.BUSINESS_INFO,
                    'required_info': [],
                    'agent': None
                },
                Stage.BUSINESS_INFO: {
                    'next': Stage.INDUSTRY_SELECTION,
                    'required_info': ['business_name', 'business_type'],
                    'agent': 'business_consultant'
                },
                Stage.INDUSTRY_SELECTION: {
                    'next': Stage.STATE_SELECTION,
                    'required_info': ['industry'],
                    'agent': 'business_consultant'
                },
                Stage.STATE_SELECTION: {
                    'next': Stage.REQUIREMENTS,
                    'required_info': ['state'],
                    'agent': 'legal_advisor'
                },
                Stage.REQUIREMENTS: {
                    'next': Stage.DOCUMENTATION,
                    'required_info': ['licenses', 'permits'],
                    'agent': 'compliance_specialist'
                },
                Stage.DOCUMENTATION: {
                    'next': Stage.REVIEW,
                    'required_info': ['articles', 'operating_agreement'],
                    'agent': 'document_specialist'
                },
                Stage.REVIEW: {
                    'next': Stage.FILING,
                    'required_info': ['review_complete'],
                    'agent': 'legal_advisor'
                },
                Stage.FILING: {
                    'next': Stage.COMPLETE,
                    'required_info': ['filing_complete'],
                    'agent': 'filing_specialist'
                },
                Stage.COMPLETE: {
                    'next': None,
                    'required_info': [],
                    'agent': None
                }
            }
        
        except Exception as e:
            raise Exception(f"Failed to initialize conversation manager: {str(e)}")
    
    async def process_input(self, user_input: str, context: Dict) -> Dict:
        """
        Process user input and manage conversation flow.
        
        Args:
            user_input: User's input text
            context: Current conversation context
            
        Returns:
            Response dictionary with next actions
        """
        try:
            # Update context
            self.state.collected_info.update(context)
            
            # Process input with NLP
            intent, confidence = self.nlp_processor.process_text(user_input)
            
            # Check for global commands
            if self._is_global_command(user_input):
                return self._handle_global_command(user_input)
            
            # Get current flow stage
            stage = self._consultation_flow[self.state.stage]
            
            # Check if we need to delegate to a specific agent
            if stage['agent']:
                agent = self.agent_manager.get_agent(stage['agent'])
                if agent:
                    response = await agent.process_request(user_input, self.state.collected_info)
                    
                    # Update collected information
                    if response.get('collected_info'):
                        self.state.collected_info.update(response['collected_info'])
                    
                    # Check if we can move to next stage
                    if self._can_advance_stage(stage):
                        next_stage = stage['next']
                        self.state.update_stage(next_stage)
                        self.state.set_agent(self._consultation_flow[next_stage]['agent'])
                        
                        return {
                            'message': response.get('message', ''),
                            'next_stage': next_stage.name,
                            'delegate_to': self.state.current_agent,
                            'context': self.state.collected_info
                        }
                    
                    return response
            
            # Generate response based on intent
            return self._get_intent_response(intent, confidence, user_input)
        
        except Exception as e:
            raise Exception(f"Error processing input: {str(e)}")
    
    def _is_global_command(self, user_input: str) -> bool:
        """Check if input is a global command."""
        global_commands = ['help', 'status', 'restart', 'back']
        return any(cmd in user_input.lower() for cmd in global_commands)
    
    def _handle_global_command(self, command: str) -> Dict:
        """Handle global commands."""
        command = command.lower()
        
        if 'help' in command:
            return {
                'message': (
                    "I can help you form your LLC! Here are some things you can ask me:\n\n"
                    "• How do I form an LLC?\n"
                    "• What are the requirements for my state?\n"
                    "• How much does it cost to form an LLC?\n"
                    "• What documents do I need?\n"
                    "• How long does it take?\n\n"
                    "You can also use these commands:\n"
                    "• 'status' - Check your progress\n"
                    "• 'back' - Go to previous step\n"
                    "• 'restart' - Start over"
                )
            }
        elif 'status' in command:
            return {
                'message': self._get_status_message(),
                'visual': {
                    'progress': self._get_progress_visual()
                }
            }
        elif 'restart' in command:
            self.state.reset()
            return {
                'message': (
                    "Let's start fresh! How can I help you form your LLC today? "
                    "Feel free to ask me anything about the process."
                )
            }
        elif 'back' in command:
            return self._go_back_one_stage()
        
        return {
            'message': "I didn't understand that command. Type 'help' to see what I can do!"
        }
    
    def _can_advance_stage(self, stage: Dict) -> bool:
        """Check if all required information for current stage is collected."""
        required_info = stage['required_info']
        collected_info = self.state.collected_info
        
        return all(info in collected_info for info in required_info)
    
    def _get_status_message(self) -> str:
        """Get current status message."""
        stage = self.state.stage.name.replace('_', ' ').title()
        collected = len(self.state.collected_info)
        total = sum(len(s['required_info']) for s in self._consultation_flow.values())
        
        return (
            f"You're currently at the {stage} stage.\n"
            f"We've collected {collected} out of {total} required pieces of information.\n\n"
            "Need help? Just ask me anything about forming your LLC!"
        )
    
    def _get_progress_visual(self) -> Dict:
        """Get visual representation of progress."""
        stages = list(self._consultation_flow.keys())
        current_index = stages.index(self.state.stage)
        
        return {
            'stages': [s.name for s in stages],
            'current': current_index,
            'total': len(stages)
        }
    
    def _go_back_one_stage(self) -> Dict:
        """Go back to previous stage."""
        stages = list(self._consultation_flow.keys())
        current_index = stages.index(self.state.stage)
        
        if current_index > 0:
            previous_stage = stages[current_index - 1]
            self.state.update_stage(previous_stage)
            agent = self._consultation_flow[previous_stage]['agent']
            
            return {
                'message': (
                    f"I've taken you back to the {previous_stage.name.replace('_', ' ').title()} stage. "
                    "What would you like to know?"
                ),
                'delegate_to': agent,
                'context': self.state.collected_info
            }
        
        return {
            'message': "We're already at the beginning! What would you like to know about forming an LLC?"
        }
    
    def _get_intent_response(self, intent: Intent, confidence: float, user_input: str) -> Dict:
        """Generate response based on intent."""
        if confidence < 0.3:
            return {
                'message': (
                    "I'm not quite sure what you're asking. Could you rephrase that? "
                    "Or type 'help' to see what I can help you with."
                )
            }
        
        responses = {
            Intent.FORMATION: {
                'message': (
                    "I'll guide you through forming your LLC! The process involves several steps:\n\n"
                    "1. Choose a business name\n"
                    "2. Select your state of formation\n"
                    "3. Appoint a registered agent\n"
                    "4. File Articles of Organization\n"
                    "5. Create an Operating Agreement\n"
                    "6. Get an EIN\n\n"
                    "Would you like to start with choosing your business name?"
                ),
                'actions': [
                    {'text': 'Choose Business Name'},
                    {'text': 'Learn More First'}
                ]
            },
            Intent.CONSULTATION: {
                'message': (
                    "I'd be happy to help you with your LLC formation! "
                    "What specific aspect would you like to discuss?\n\n"
                    "• Business structure and planning\n"
                    "• State selection and requirements\n"
                    "• Document preparation\n"
                    "• Filing procedures"
                ),
                'actions': [
                    {'text': 'Discuss Business Structure'},
                    {'text': 'Review Requirements'}
                ]
            },
            Intent.INFORMATION: {
                'message': (
                    "An LLC (Limited Liability Company) is a flexible business structure "
                    "that combines the liability protection of a corporation with the tax "
                    "benefits of a partnership.\n\n"
                    "Would you like to learn more about:\n"
                    "• LLC benefits and features\n"
                    "• Formation requirements\n"
                    "• Costs and timeline\n"
                    "• Ongoing responsibilities"
                ),
                'actions': [
                    {'text': 'LLC Benefits'},
                    {'text': 'Formation Requirements'}
                ]
            },
            Intent.CLARIFICATION: {
                'message': (
                    "Let me clarify that for you. What specific part would you like me to explain? "
                    "I can help you understand any aspect of LLC formation."
                ),
                'actions': [
                    {'text': 'Get Help'},
                    {'text': 'Start Over'}
                ]
            },
            Intent.COMPARISON: {
                'message': (
                    "Let me help you compare your options. LLCs offer several advantages:\n\n"
                    "• Limited liability protection\n"
                    "• Flexible tax options\n"
                    "• Simple management structure\n"
                    "• Less paperwork than corporations\n\n"
                    "Would you like to compare LLCs with other business structures?"
                ),
                'actions': [
                    {'text': 'Compare Structures'},
                    {'text': 'LLC Advantages'}
                ]
            },
            Intent.COST: {
                'message': (
                    "The cost of forming an LLC varies by state. Typical expenses include:\n\n"
                    "• State filing fees ($50-$500)\n"
                    "• Registered agent fees ($100-$300/year)\n"
                    "• Operating Agreement preparation\n"
                    "• Business licenses and permits\n\n"
                    "Would you like to know the specific costs for your state?"
                ),
                'actions': [
                    {'text': 'State-Specific Costs'},
                    {'text': 'Optional Services'}
                ]
            },
            Intent.TIMELINE: {
                'message': (
                    "The timeline for forming an LLC typically looks like this:\n\n"
                    "• Name availability check: 1-2 days\n"
                    "• Document preparation: 1-3 days\n"
                    "• State filing: 5-10 business days\n"
                    "• EIN registration: 1-2 days\n\n"
                    "Some states offer expedited processing for an additional fee."
                ),
                'actions': [
                    {'text': 'Expedited Options'},
                    {'text': 'Start Formation'}
                ]
            },
            Intent.REQUIREMENTS: {
                'message': (
                    "To form an LLC, you'll need:\n\n"
                    "• A unique business name\n"
                    "• A registered agent\n"
                    "• Articles of Organization\n"
                    "• Operating Agreement\n"
                    "• EIN (for tax purposes)\n\n"
                    "Would you like me to explain any of these requirements?"
                ),
                'actions': [
                    {'text': 'Explain Requirements'},
                    {'text': 'Start Formation'}
                ]
            }
        }
        
        # Default to help response if intent not found
        return responses.get(intent, {
            'message': (
                "I'm here to help you form your LLC! You can ask me about:\n\n"
                "• Formation process and requirements\n"
                "• Costs and timeline\n"
                "• State-specific information\n"
                "• Document preparation\n\n"
                "What would you like to know?"
            ),
            'actions': [
                {'text': 'Formation Process'},
                {'text': 'Ask Question'}
            ]
        })
