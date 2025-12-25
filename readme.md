
# Assignment 1 – Module 2: Basic Python Concepts

> **Prepared by:** Avikal Chauhan

This repository contains two Python scripts completing the assignment:

- **`task1_math_ops.py`** – Prompts for two numbers and performs **addition**, **subtraction**, **multiplication**, and **division** with user-friendly validation and clear output.
- **`task2_greeting.py`** – Prompts for **first** and **last** name, concatenates to a **full name**, and prints a personalized greeting.

## How to run locally

1. Ensure you have Python 3.8+ installed. Verify with:
   ```bash
   python --version
   ```
2. Run Task 1:
   ```bash
   python task1_math_ops.py
   ```
3. Run Task 2:
   ```bash
   python task2_greeting.py
   ```

## Sample outputs

### Task 1
```
=== Task 1: Basic Mathematical Operations ===

Enter the first number: 12
Enter the second number: 4

Results:
Addition      : 16
Subtraction   : 8
Multiplication: 48
Division      : 3

Done.
```

### Task 2
```
=== Task 2: Personalized Greeting ===

Enter your first name: Avikal
Enter your last name: Chauhan

Hello, Avikal Chauhan! Welcome to Python Module 2.
```

## Validation & Error Handling
- Numbers accept integers or decimals, and common thousands separators (e.g., `1,234.56`).
- Division-by-zero is handled gracefully with an **undefined** message.
- Names allow letters, spaces, hyphens, and apostrophes, reject invalid characters, and normalize capitalization.

## GitHub Submission Steps
1. Create a new public or private repository on GitHub (e.g., `module-2-basic-python-assignment`).
2. Add these files to the repo root:
   - `task1_math_ops.py`
   - `task2_greeting.py`
   - `README.md`
3. Commit and push:
   ```bash
   git init
   git add task1_math_ops.py task2_greeting.py README.md
   git commit -m "Add Assignment 1 scripts and README"
   git branch -M main
   git remote add origin https://github.com/<your-username>/module-2-basic-python-assignment.git
   git push -u origin main
   ```
4. Verify the README renders correctly and both scripts run from the GitHub Codespaces or your local environment.
5. Submit your **repository URL** as requested.

## Notes
- Tested on Python 3.12. If you use older versions, behavior should still be compatible.
- For any doubts, contact your mentor via chat support.

