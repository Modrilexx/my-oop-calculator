import pytest

from calculator.calculation import Add, Subtract
from calculator.history import History


def test_history_starts_empty():
    history = History()

    assert history.count() == 0
    assert history.get_all() == []


def test_add_calculation_to_history():
    history = History()
    calculation = Add(10, 5)

    history.add(calculation)

    assert history.count() == 1
    assert history.get_all()[0] is calculation


def test_add_multiple_calculations():
    history = History()
    first = Add(10, 5)
    second = Subtract(20, 7)

    history.add(first)
    history.add(second)

    assert history.count() == 2
    assert history.get_all() == [first, second]


def test_remove_calculation():
    history = History()
    first = Add(10, 5)
    second = Subtract(20, 7)

    history.add(first)
    history.add(second)

    removed = history.remove(0)

    assert removed is first
    assert history.get_all() == [second]


def test_clear_history():
    history = History()

    history.add(Add(10, 5))
    history.add(Subtract(20, 7))

    history.clear()

    assert history.count() == 0


def test_get_all_returns_copy():
    history = History()
    calculation = Add(10, 5)

    history.add(calculation)

    copy_of_history = history.get_all()
    copy_of_history.clear()

    assert history.count() == 1