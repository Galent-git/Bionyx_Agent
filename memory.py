# memory.py

import json
import os
from datetime import datetime

class MemoryManager:
    """
    Persistent memory manager for Bionyx.
    Stores conversation history, key-value data, and can be expanded with namespaces.
    """

    def __init__(self, filepath="memory_logs/memory.json"):
        self.filepath = filepath
        self.data = {
            "store": {},
            "history": []
        }
        self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception as e:
                print(f"[MemoryManager] Failed to load memory: {e}")

    def _save(self):
        try:
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"[MemoryManager] Failed to save memory: {e}")

    def store(self, key, value):
        self.data["store"][key] = value
        self._save()

    def recall(self, key):
        return self.data["store"].get(key)

    def clear_store(self):
        self.data["store"].clear()
        self._save()

    def log_interaction(self, user_input, response):
        timestamp = datetime.now().isoformat()
        self.data["history"].append({
            "timestamp": timestamp,
            "user": user_input,
            "bionyx": response
        })
        self._save()

    def get_history(self, n=5):
        return self.data["history"][-n:]

    def clear_history(self):
        self.data["history"].clear()
        self._save()
