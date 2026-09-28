import pytest
from calculator.calculation import Calculation, Add, Subtract

def test_add_positive_numbers():
    calculation = Add(10, 5)
    result = calculation.get_result()

    assert result == 15


def test_add_negative_numbers():
    calculation = Add(-10, -5)
    result = calculation.get_result()

    assert result == -15


def test_add_zero():
    calculation = Add(10, 0)
    result = calculation.get_result()

    assert result == 10


def test_add_decimal_numbers():
    calculation = Add(2.5, 1.5)
    result = calculation.get_result()

    assert result == 4.0

def test_add_does_not_change_operands():
    calculation = Add(8, -3)

    assert calculation.get_result() == 5
    assert calculation.a == 8
    assert calculation.b == -3

def test_subtract_positive_numbers():
    calculation = Subtract(10, 5)
    assert calculation.get_result() == 5


def test_subtract_negative_result():
    calculation = Subtract(5, 10)
    assert calculation.get_result() == -5

def test_add_is_a_calculation():
    calculation = Add(10, 5)
    assert isinstance(calculation, Calculation)


def test_subtract_is_a_calculation():
    calculation = Subtract(10, 5)
    assert isinstance(calculation, Calculation)


def test_calculation_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Calculation(10, 5)