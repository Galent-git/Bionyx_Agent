# modules/file_analysis_module.py
import os
from module_base import BionyxModule

class FileAnalysisModule(BionyxModule):
    name = "FileAnalysisModule"
    description = "Analyzes a file or directory. Usage: 'analyze <path>'."

    def can_handle(self, user_input: str) -> bool:
        # This module handles commands that start with "analyze "
        return user_input.lower().startswith("analyze ")

    def handle(self, user_input: str) -> str:
        # Expect a command like: analyze /path/to/file_or_directory
        parts = user_input.split(maxsplit=1)
        if len(parts) < 2:
            return "Usage: analyze <file_or_directory_path>"
        path = parts[1].strip()

        if not os.path.exists(path):
            return f"Path '{path}' does not exist."

        if os.path.isdir(path):
            try:
                files = os.listdir(path)
                if not files:
                    return f"Directory '{path}' is empty."
                file_list = "\n".join(files)
                return f"Directory '{path}' contains:\n{file_list}"
            except Exception as e:
                return f"Error reading directory '{path}': {e}"
        elif os.path.isfile(path):
            try:
                size = os.path.getsize(path)
                analysis = f"File '{path}' is {size} bytes."
                try:
                    with open(path, 'r', encoding="utf-8") as f:
                        lines = f.readlines()
                    analysis += f" It has {len(lines)} lines."
                except Exception:
                    analysis += " (Unable to read as a text file.)"
                return analysis
            except Exception as e:
                return f"Error analyzing file '{path}': {e}"
        else:
            return "The specified path is neither a file nor a directory."
