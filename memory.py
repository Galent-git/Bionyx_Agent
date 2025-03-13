# memory.py
class MemoryManager:
    """
    A simple memory manager for Bionyx.
    It could store conversation history, user preferences, or learned facts.
    """
    def __init__(self):
        self.data = {}

    def store(self, key, value):
        self.data[key] = value

    def recall(self, key):
        return self.data.get(key, None)

    def clear(self):
        self.data.clear()
