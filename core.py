# Create the updated bionyx_core.py file with the new logic
import os
import datetime
from interpreter_runner import run_interpreter_query
import pluggy
from hookspecs import BionyxSpecs
from memory import MemoryManager


class BionyxCore:
    def __init__(self, name="Bionyx", log_file="memory_logs/bionyx_log.txt"):
        self.name = name
   
        # Setup plugin manager
        self.pm = pluggy.PluginManager("bionyx")
        self.pm.add_hookspecs(BionyxSpecs)
        self._register_default_plugins()
        self.memory = MemoryManager()
        self.memory.log_interaction(user_input, response)
        self.log("Initialized with LLM-first, tools-on-command behavior.")

    def _ensure_log_dir_exists(self):
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

   
    def _register_default_plugins(self):
        try:
            from plugins import chat_plugin, funfact_plugin
            self.pm.register(chat_plugin.ChatPlugin())
            self.pm.register(funfact_plugin.FunFactPlugin())
        except ImportError as e:
            print(f"[WARN] Plugins not fully loaded: {e}")

    def list_abilities(self):
        print("Available abilities:")
        for ability in self.pm.hook.list_abilities():
            print(f" - {ability}")

    def process_input(self, user_input: str) -> str:
        responses = self.pm.hook.process_input(user_input=user_input)
        responses = [r for r in responses if r]
        return responses[0] if responses else None

    def simulate_llm_response(self, query: str) -> str:
        return f"I understand you're asking about: '{query}'.\\nWould you like me to run a tool or interpreter on this? Type '!run [task]' to proceed."

    def run(self):
        print(f"{self.name}: Online. Type 'help' to list abilities, 'exit' to quit.")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print(f"{self.name}: Session ended.")
                self.log("Session closed by user.")
                break
            elif user_input.lower() == "help":
                self.list_abilities()
                continue
            elif user_input.startswith("!run"):
                stripped_input = user_input.replace("!run", "", 1).strip()
                response = run_interpreter_query(stripped_input)
                print(f"{self.name}: [INTERPRETER] {response}")
                self.log(f"{self.name} (INTERPRETER): {response}")
                continue

            self.log(f"User: {user_input}")
            native_response = self.process_input(user_input)

            if native_response:
                print(f"{self.name}: {native_response}")
                self.log(f"{self.name}: {native_response}")
            else:
                simulated_response = self.simulate_llm_response(user_input)
                print(f"{self.name}: {simulated_response}")
                self.log(f"{self.name}: {simulated_response}")


if __name__ == "__main__":
    agent = BionyxCore()
    agent.run()



