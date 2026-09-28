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

def test_cli_invalid_add_number(capsys):
    inputs = iter([
        "add",
        "banana",
        "10",
        "5",
        "exit",
    ])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Invalid number. Try again." in output
    assert "Result: 15.0" in output


def test_cli_invalid_subtract_number(capsys):
    inputs = iter([
        "subtract",
        "nope",
        "20",
        "7",
        "exit",
    ])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Invalid number. Try again." in output
    assert "Result: 13.0" in output


def test_cli_invalid_remove_text(capsys):
    inputs = iter([
        "remove",
        "abc",
        "exit",
    ])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Invalid calculation number." in output


def test_cli_remove_out_of_range(capsys):
    inputs = iter([
        "add",
        "10",
        "5",
        "remove",
        "99",
        "exit",
    ])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Invalid calculation number." in output  

def test_cli_unknown_command(capsys):
    inputs = iter(["whatever", "exit"])

    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        run()

    output = capsys.readouterr().out

    assert "Unknown command." in output


def test_cli_eof_exits(capsys):
    with patch("builtins.input", side_effect=EOFError):
        run()

    output = capsys.readouterr().out

    assert "Goodbye!" in output


def test_cli_keyboard_interrupt_exits(capsys):
    with patch("builtins.input", side_effect=KeyboardInterrupt):
        run()

    output = capsys.readouterr().out

    assert "Goodbye!" in output