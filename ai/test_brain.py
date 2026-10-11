
import os
import sys

# Add the project root folder to Python's import path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from ai.brain import ask_ai

answer = ask_ai("Explain Python in simple words.")
print("KALKI:", answer)
