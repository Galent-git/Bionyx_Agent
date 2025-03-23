# modules/chat_module.py
from module_base import BionyxModule
import random

class ChatModule(BionyxModule):
    name = "ChatModule"
    description = "Engage in conversation with Bionyx."

    def __init__(self):
        self.conversation_history = []

    def can_handle(self, user_input: str) -> bool:
        # For example, ChatModule might be the default for any input not handled by others.
        return True

    def handle(self, user_input: str) -> str:
        self.conversation_history.append(user_input)
        responses = [
            "Interesting, tell me more!",
            "Could you elaborate on that?",
            "I'm intrigued, please continue.",
            "That's fascinating!"
        ]
        return random.choice(responses)
