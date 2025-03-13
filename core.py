# core.py
from modules import ChatModule, FunFactModule, AbilitiesModule
from memory import MemoryManager

class BionyxCore:
    def __init__(self, name="Bionyx"):
        self.name = name
        self.modules = []
        self.memory = MemoryManager()  # For storing conversation history or other data

    def boot(self):
        print(f"{self.name}: Hello! I’m {self.name}—your new AI friend!")
        print("I’m eager to get started. Please choose an option below!")
        self.show_menu()

    def register_module(self, module):
        self.modules.append(module)

    def show_menu(self):
        menu = (
            "\n*** MAIN MENU ***\n"
            "1) Chat\n"
            "2) Fun Fact\n"
            "3) Abilities/Help\n"
            "4) Exit\n"
        )
        print(menu)

    def run(self):
        self.boot()
        while True:
            choice = input("Enter your choice: ").strip().lower()
            if choice == "1":
                self.handle_chat()
            elif choice == "2":
                self.handle_fun_fact()
            elif choice == "3":
                self.handle_abilities()
            elif choice == "4":
                print(f"{self.name}: Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                self.show_menu()

    def handle_chat(self):
        chat_module = self.get_module("ChatModule")
        if chat_module:
            chat_module.handle()
        else:
            print("Chat module not available.")

    def handle_fun_fact(self):
        fun_fact_module = self.get_module("FunFactModule")
        if fun_fact_module:
            fun_fact_module.handle()
        else:
            print("Fun Fact module not available.")

    def handle_abilities(self):
        abilities_module = self.get_module("AbilitiesModule")
        if abilities_module:
            abilities_module.handle()
        else:
            print("Abilities module not available.")

    def get_module(self, module_name):
        for mod in self.modules:
            if mod.name == module_name:
                return mod
        return None

if __name__ == "__main__":
    from modules import ChatModule, FunFactModule, AbilitiesModule

    bionyx = BionyxCore()
    bionyx.register_module(ChatModule())
    bionyx.register_module(FunFactModule())
    bionyx.register_module(AbilitiesModule())
    bionyx.run()
