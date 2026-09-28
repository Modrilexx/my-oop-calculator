from calculator.calculation import Add


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