
"""
Assignment 1 – Module 2: Basic Python Concepts
Task 2: Create a Personalized Greeting

This script:
1) Accepts user's first and last name.
2) Concatenates them into a full name.
3) Prints a personalized greeting message.
"""

# Tip: You can run this file with:  python task2_greeting.py

import re

def read_name(part: str) -> str:
    """Read a name part (first/last). Allow letters, spaces, hyphens, and apostrophes.
    Re-prompt until valid. """
    pattern = re.compile(r"^[A-Za-z][A-Za-z\-' ]*[A-Za-z]$")
    while True:
        s = input(f"Enter your {part} name: ").strip()
        if len(s) < 2:
            print("Name is too short. Please enter at least 2 characters.")
            continue
        if not pattern.match(s):
            print("Invalid characters detected. Use letters, spaces, hyphens (-), or apostrophes (').")
            continue
        # Normalize whitespace and casing
        s = " ".join(word.capitalize() for word in s.split())
        return s

def main():
    print("
=== Task 2: Personalized Greeting ===
")
    first = read_name("first")
    last = read_name("last")
    full_name = f"{first} {last}".strip()
    print(f"
Hello, {full_name}! Welcome to Python Module 2.
")

if __name__ == "__main__":
    main()

