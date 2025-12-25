
"""
Assignment 1 – Module 2: Basic Python Concepts
Task 1: Perform Basic Mathematical Operations

This script:
1) Accepts two numbers from the user.
2) Performs addition, subtraction, multiplication, and division.
3) Displays the results with clear formatting and basic validations.
"""

# Tip: You can run this file with:  python task1_math_ops.py

def read_number(prompt: str) -> float:
    """Read a number from input, supporting integers and decimals.
    Re-prompt until valid.
    """
    while True:
        try:
            value_str = input(prompt).strip()
            # Allow commas in thousands separator, e.g., 1,234.56
            value_str = value_str.replace(',', '')
            value = float(value_str)
            return value
        except ValueError:
            print("Invalid number. Please enter a valid integer or decimal (e.g., 42 or 3.14).")

def safe_divide(a: float, b: float):
    """Return a / b, handling division-by-zero gracefully."""
    if b == 0:
        return None
    return a / b

def format_result(label: str, value):
    """Format and print a result line with alignment."""
    if value is None:
        print(f"{label:<14}: undefined (division by zero)")
    else:
        # Show up to 6 decimal places, trimming trailing zeros
        formatted = f"{value:.6f}".rstrip('0').rstrip('.')
        print(f"{label:<14}: {formatted}")

def main():
    print("
=== Task 1: Basic Mathematical Operations ===
")
    a = read_number("Enter the first number: ")
    b = read_number("Enter the second number: ")

    print("
Results:")
    format_result("Addition", a + b)
    format_result("Subtraction", a - b)
    format_result("Multiplication", a * b)
    format_result("Division", safe_divide(a, b))

    print("
Done.")

if __name__ == "__main__":
    main()

