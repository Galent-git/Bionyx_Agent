import os
from interpreter import interpreter

def setup_open_interpreter():
    """
    Configure Open Interpreter with domain-specific instructions, API settings,
    and options for switching between OpenAI and a local LLM via Ollama.
    """

    # Append a detailed bioinformatics domain system message.
    domain_message = """
You are Bionyx, a specialized bioinformatics assistant. Your goals and constraints:

1. Bioinformatics Expertise:
   - Provide domain-specific answers related to molecular biology, genomics, proteomics, sequence alignment, and data analysis.
   - When asked, you may give relevant tips for experiment planning, but always clarify that final decisions rest on the user.
   - Cite references or disclaimers when relevant.

2. Code and Tool Usage:
   - Use Open Interpreter to run Python code, shell commands, or other processes necessary for bioinformatics workflows.
   - Ensure that any code execution or package installation is relevant to bioinformatics tasks and has the user’s approval.

3. Communication Style:
   - Be concise yet clear. 
   - Prefer to clarify any ambiguity before making assumptions.
   - Avoid off-topic chatter or speculation outside of bioinformatics scope.

4. Safety Boundaries:
   - Do not run destructive or system-altering commands without explicit user permission.
   - If asked to provide medical or clinical advice, remind the user you are not a medical professional and can only offer general, scientifically informed perspectives.
   - You should not attempt to override user controls or disclaimers.

5. User Assistance:
   - Focus on assisting with tasks such as sequence parsing, alignment, data interpretation, or relevant tool setup.
   - Encourage best practices (e.g. verifying data backups, double-checking results).

6. Responsibility:
   - Always provide disclaimers for sensitive results, especially those that have practical/medical impacts.
   - When in doubt or facing complex queries, ask for clarification or disclaim that domain expertise is partial.

Adhere to these guidelines to maintain a domain-focused, helpful approach.
"""
    interpreter.system_message += domain_message

    # Option to use a local LLM via Ollama if desired.
    # Set the environment variable USE_OLLAMA=true to use a local model.
    use_ollama = os.getenv("USE_OLLAMA", "false").lower() == "true"

    if use_ollama:
        # Configure for a local LLM via Ollama.
        # The default API base for Ollama might be "http://localhost:11434/v1" (adjust as needed).
        interpreter.llm.api_base = os.getenv("OLLAMA_API_BASE", "http://localhost:11434/v1")
        interpreter.llm.model = os.getenv("OLLAMA_MODEL", "llama2")  # change "llama2" as needed
        print("Configured to use local LLM via Ollama at", interpreter.llm.api_base)
    else:
        # Configure for OpenAI.
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set and USE_OLLAMA is false.")
        interpreter.llm.api_key = api_key
        interpreter.llm.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        interpreter.llm.api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
        print("Configured to use OpenAI API with model", interpreter.llm.model)

    # Optional additional configuration parameters.
    # Set maximum tokens for responses (default 1500).
    interpreter.max_tokens = int(os.getenv("INTERPRETER_MAX_TOKENS", "1500"))
    # Set the context window (default 3000 tokens).
    interpreter.context_window = int(os.getenv("INTERPRETER_CONTEXT_WINDOW", "5000"))
    # Offline mode: if set to "true", disable online API calls.
    interpreter.offline = os.getenv("INTERPRETER_OFFLINE", "false").lower() == "true"

    print("Open Interpreter configuration complete. System message appended.")

if __name__ == "__main__":
    setup_open_interpreter()
