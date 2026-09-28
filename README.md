# OOP Calculator

A command-line calculator built in Python to practice object-oriented programming concepts including classes, inheritance, abstraction, encapsulation, testing, error handling, and continuous integration.

## Features

The calculator supports:

- Addition
- Subtraction
- Calculation history
- Removing calculations from history
- Help commands
- Graceful exit
- Invalid input handling

## Project Structure

```text
my-oop-calculator/
├── calculator/
│   ├── __init__.py
│   ├── __main__.py
│   ├── calculation.py
│   ├── cli.py
│   └── history.py
├── tests/
│   ├── test_calculation.py
│   ├── test_cli.py
│   ├── test_history.py
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── pytest.ini
├── requirements.txt
└── README.md

Running the Calculator
Create and activate a virtual environment:
python3 -m venv .venv
source .venv/bin/activate

Install the dependencies:
python -m pip install -r requirements.txt

Run the calculator:
python -m calculator

Example:
Calculator
Type 'help' to see commands.

> add
First number: 10
Second number: 5
Result: 15.0

> history
Calculation History
1. Add: 10.0, 5.0 = 15.0

> exit
Goodbye!

Testing
Run the full test suite with:
python -m pytest

The project requires 100% line and branch coverage.
Object-Oriented Design
The project uses an abstract Calculation class as a shared contract for arithmetic operations.
Add and Subtract inherit from Calculation and provide their own implementations of get_result().
The History class encapsulates the collection of calculation objects and provides methods for adding, removing, clearing, and retrieving calculations.
The command-line interface connects these objects together and handles user interaction.
Continuous Integration
GitHub Actions automatically runs the test suite whenever code is pushed or a pull request is opened.
This ensures that the project continues to pass all tests and maintain full coverage.

