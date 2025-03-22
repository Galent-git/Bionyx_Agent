# module_base.py
class BionyxModule:
    """
    Base class for all Bionyx modules.
    Each module should have a name and description, and implement a can_handle() and handle() method.
    """
    name = "BaseModule"
    description = "A base Bionyx module."

    def can_handle(self, user_input: str) -> bool:
        """Return True if this module can handle the given input."""
        raise NotImplementedError

    def handle(self, user_input: str) -> str:
        """Process the input and return a response."""
        raise NotImplementedError
