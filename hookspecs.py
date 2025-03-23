import pluggy

hookspec = pluggy.HookspecMarker("bionyx")
hookimpl = pluggy.HookimplMarker("bionyx")

class BionyxSpecs:
    @hookspec
    def process_input(self, user_input: str) -> str:
        """Process the user input and return a response (or an empty string if not applicable)."""
    
    @hookspec
    def list_abilities(self) -> str:
        """Return a description of this plugin's abilities."""
