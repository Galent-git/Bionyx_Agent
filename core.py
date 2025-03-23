
import pluggy
from hookspecs import BionyxSpecs

class BionyxCore:
    def __init__(self, name="Bionyx"):
        self.name = name
        # Create a plugin manager for the "bionyx" project
        self.pm = pluggy.PluginManager("bionyx")
        # Register our hook specifications
        self.pm.add_hookspecs(BionyxSpecs)
    
    def load_plugins(self):
        """
        Load plugins dynamically. For demonstration, we register plugins manually.
        In a more advanced setup, you can use setuptools entry points or dynamic discovery.
        """
        # Example: manually import and register plugins from the plugins folder.
        # Ensure your plugins folder is in the PYTHONPATH.
        try:
            from plugins import chat_plugin, funfact_plugin  # these are example plugin modules
            self.pm.register(chat_plugin.ChatPlugin())
            self.pm.register(funfact_plugin.FunFactPlugin())
        except ImportError as e:
            print(f"Error loading plugins: {e}")

    def list_abilities(self):
        print("Available abilities:")
        for ability in self.pm.hook.list_abilities():
            print(f" - {ability}")

    def process_input(self, user_input: str) -> str:
        # Call all plugins' process_input hook implementations.
        responses = self.pm.hook.process_input(user_input=user_input)
        # Filter out empty responses and return the first meaningful answer.
        responses = [resp for resp in responses if resp]
        if responses:
            return responses[0]
        return "I'm not sure how to handle that."

    def run(self):
        print(f"{self.name}: Booting up using Pluggy for dynamic modules...")
        self.load_plugins()
        print("Type 'help' for a list of abilities or 'exit' to quit.")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print(f"{self.name}: Goodbye!")
                break
            elif user_input.lower() == "help":
                self.list_abilities()
            else:
                response = self.process_input(user_input)
                print(f"{self.name}: {response}")

if __name__ == "__main__":
    core = BionyxCore()
    core.run()
