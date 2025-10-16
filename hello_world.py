#!/usr/bin/env python3
"""
Hello World Program
A simple Python program to demonstrate basic functionality.
"""

def main():
    """Main function that prints a greeting message."""
    print("Hello, World!")
    print("Welcome to your first Python program!")
    print("This program is running in your virtual environment.")
    
    # Demonstrate basic Python features
    print("\nLet's do some basic math:")
    a = 10
    b = 5
    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")
    
    # Show current Python version
    import sys
    print(f"\nPython version: {sys.version}")
    
    print("\nProgram completed successfully!")

    #added a comment to test the git commit

if __name__ == "__main__":
    main()