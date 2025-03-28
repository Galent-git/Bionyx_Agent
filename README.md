# Bionyx

Bionyx is a minimal, **bioinformatics‐oriented** assistant that leverages [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) to run commands locally, optionally paired with OpenAI for advanced language reasoning. It aims to simplify common bioinformatics workflows, offering:

- **Local Code Execution:** Perform file operations, run scripts, and install packages—always under user control.  
- **Bioinformatics Focus:** Share domain‐specific knowledge, disclaimers, and best practices.  
- **Expandable Architecture:** You can easily add modules or adapt the system message to fit your research needs.

---

## Why Bionyx?

1. **Streamlined Setup:** Just `pip install open-interpreter` (and optionally set your `OPENAI_API_KEY`) to get started.  
2. **Local + Cloud Flexibility:** Use GPT‐4o (or other) via OpenAI, or point Open Interpreter to a local model if you prefer offline usage.  
3. **Memory Logging:** Maintain context across sessions with simple log files.  
4. **Bioinformatics Guidance:** Focus on relevant tasks like sequence analysis, alignment tips, or data visualization ideas.

---

## Quick Start

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YourUsername/bionyx.git
   cd bionyx
