"""
Main entry point for LLC Formation Assistant.
"""

import asyncio
from agents.conversation_manager import ConversationManager

async def main():
    """Main entry point."""
    try:
        # Initialize conversation manager
        manager = ConversationManager()
        
        # Print welcome message
        print("+-------------------------- LLC Formation Assistant --------------------------+")
        print("| Welcome to the LLC Formation Assistant!                                     |")
        print("|                                                                             |")
        print("| I'm here to help you form your LLC and guide you through the entire         |")
        print("| process. I can help you with:                                               |")
        print("| • Business formation strategy                                               |")
        print("| • State selection and requirements                                          |")
        print("| • Document preparation and filing                                           |")
        print("| • Compliance and ongoing maintenance                                        |")
        print("|                                                                             |")
        print("| Type 'help' at any time to see available commands.                          |")
        print("| Type 'exit' to quit.                                                        |")
        print("+-----------------------------------------------------------------------------+")
        print()
        
        # Main conversation loop
        context = {}
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Check for exit command
                if user_input.lower() == 'exit':
                    print("\nThank you for using the LLC Formation Assistant. Goodbye!")
                    break
                
                # Process user input
                if user_input:
                    response = await manager.process_input(user_input, context)
                    
                    # Update context with any new information
                    if 'context' in response:
                        context.update(response['context'])
                    
                    # Print response
                    print("\nAssistant:", response.get('message', ''))
                    
                    # Print any actions
                    actions = response.get('actions', [])
                    if actions:
                        print("\nAvailable actions:")
                        for action in actions:
                            print(f"• {action['text']}")
                    print()
            
            except EOFError:
                print("\nInput stream closed. Exiting...")
                break
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"\nError: {str(e)}")
                print("Please try again or type 'exit' to quit.")
    
    except Exception as e:
        print(f"\nFatal error: {str(e)}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
