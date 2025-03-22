
from memory import MemoryManager
 # core.py
import os
import importlib.util
from module_base import BionyxModule

class BionyxCore:
    def __init__(self, name="Bionyx"):
        self.name = name
        self.modules = []

    def boot(self):
        print(f"{self.name}: Hello! I'm {self.name} – your modular AI companion.")
        self.load_modules()  # Dynamically load all modules in the 'modules' folder.
        print("Type 'help' to list available commands, or 'exit' to quit.")

    def load_modules(self, modules_folder="modules"):
        """
        Dynamically scans the given folder for .py files,
        imports them, and registers any classes that subclass BionyxModule.
        """
        for filename in os.listdir(modules_folder):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_path = os.path.join(modules_folder, filename)
                module_name = filename[:-3]  # remove .py extension
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                # Look for classes that are subclasses of BionyxModule (excluding BionyxModule itself)
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if (
                        isinstance(attribute, type)
                        and issubclass(attribute, BionyxModule)
                        and attribute is not BionyxModule
                    ):
                        instance = attribute()
                        self.modules.append(instance)
                        print(f"Loaded module: {instance.name}")

    def list_abilities(self):
        print("Available abilities:")
        for mod in self.modules:
            print(f"- {mod.name}: {mod.description}")

    def respond(self, user_input: str) -> str:
        # Special command for help.
        if user_input.lower() == "help":
            self.list_abilities()
            return ""

        # Iterate over modules to find one that can handle the input.
        for mod in self.modules:
            if mod.can_handle(user_input):
                return mod.handle(user_input)
        return "I'm not sure how to handle that."

    def run(self):
        self.boot()
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print(f"{self.name}: Goodbye!")
                break
            response = self.respond(user_input)
            if response:
                print(f"{self.name}: {response}")

if __name__ == "__main__":
    bionyx = BionyxCore()
    bionyx.run()

