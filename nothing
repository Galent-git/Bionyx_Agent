# modules.py
import random
from faker import Faker

class ChatModule:
    name = "ChatModule"
    description = "Engage in simple conversation."

    def __init__(self):
        self.conversation_history = []

    def handle(self):
        print("Chat Module: Type 'stop' to return to the main menu.")
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() == "stop":
                print("Returning to the main menu...")
                break
            self.conversation_history.append(user_input)
            responses = [
                "Interesting, tell me more!",
                "Could you elaborate on that?",
                "I'm intrigued, please continue.",
                "That's fascinating!"
            ]
            print("Bionyx:", random.choice(responses))

class FunFactModule:
    name = "FunFactModule"
    description = "Share a random fun fact."

    def __init__(self):
        self.faker = Faker()

    def handle(self):
        # Generate a fun fact using Faker
        fact = self.faker.sentence(nb_words=10)
        print("Bionyx [Fun Fact]:", fact)

class AbilitiesModule:
    name = "AbilitiesModule"
    description = "Display my abilities and available actions."

    def handle(self):
        abilities = [
            "Chat with you via the Chat Module.",
            "Share random fun facts using the Fun Fact Module.",
            "List my abilities with this module.",
            "I can be extended with more functionalities in the future!"
        ]
        print("Bionyx: My current abilities:")
        for ability in abilities:
            print(" -", ability)
