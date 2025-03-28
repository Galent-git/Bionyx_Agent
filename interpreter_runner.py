# interpreter_runner.py
from interpreter import interpreter
from config_open_interpreter import setup_open_interpreter

setup_open_interpreter()  # Initialize config once

def run_interpreter_query(prompt: str) -> str:
    return interpreter.chat(prompt)
