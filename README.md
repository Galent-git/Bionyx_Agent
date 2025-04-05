# Bionyx – Your Bioinformatics Copilot ( In active learning development )

**Bionyx** is a modular AI agent designed to assist with bioinformatics workflows, natural language queries, and exploratory data tasks.

It combines:
- A plugin architecture for domain-specific tools
- An LLM interface for reasoning and suggestions
- OpenInterpreter for on-the-fly code execution
- A memory manager for interaction logs and persistent state

---

## Current Capabilities

- Accepts user input via CLI
- Checks for native tool plugins (e.g., fun facts, chat)
- Falls back to LLM-style reasoning when needed
- Offers to use OpenInterpreter if task execution is requested
- Logs all inputs/outputs and stores internal memory

---

## Repo Structure (Simplified)

```
bionyx_core.py                   # Main hybrid loop
memory.py                        # Persistent memory system
config_open_interpreter.py      # Domain config + LLM setup
interpreter_runner.py           # Clean OI interface
hookspecs.py                    # Plugin specification schema
plugins/                        # Example plugins (funfact, chat)
memory_logs/                    # JSON logs of user sessions
```

---

## How to Run

```
pip install -r requirements.txt
python bionyx_core.py
```

You will need an `OPENAI_API_KEY` set in your environment, or a local model available via Ollama.

---

## Philosophy

Bionyx is meant to be:
- A realistic LLM wrapper that doesn’t hallucinate blindly
- A modular AI copilot that can learn, expand, and assist
- A tool for thinkers in need of both code and conversation

---

## Future Vision

- Dynamic plugin registration
- GUI or terminal notebook mode
- Context-aware memory shaping
- Workflow pipelines (BLAST, QC, sequence parsing)
- Research-aware prompt engineering

---

## Status

This project is under active development.

