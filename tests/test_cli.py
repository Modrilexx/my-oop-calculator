from unittest.mock import patch

from calculator.cli import run


def test_cli_add(capsys):
    inputs = iter(["add", "10", "5", "exit"])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Result: 15.0" in output
    assert "Goodbye!" in output


def test_cli_subtract(capsys):
    inputs = iter(["subtract", "20", "7", "exit"])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Result: 13.0" in output


def test_cli_history(capsys):
    inputs = iter([
        "add", "10", "5",
        "subtract", "20", "7",
        "history",
        "exit",
    ])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Calculation History" in output
    assert "1. Add: 10.0, 5.0 = 15.0" in output
    assert "2. Subtract: 20.0, 7.0 = 13.0" in output

def test_cli_help(capsys):
    inputs = iter(["help", "exit"])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Commands: add, subtract, history, remove, help, exit" in output


def test_cli_empty_history(capsys):
    inputs = iter(["history", "exit"])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Calculation History" in output
    assert "No calculations yet." in output


def test_cli_remove(capsys):
    inputs = iter([
        "add", "10", "5",
        "subtract", "20", "7",
        "remove", "1",
        "history",
        "exit",
    ])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Calculation removed." in output
    assert "1. Subtract: 20.0, 7.0 = 13.0" in output
    assert "1. Add: 10.0, 5.0 = 15.0" not in output