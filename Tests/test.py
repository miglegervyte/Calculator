from Calculator.Calculator import Calculator
import pytest


def test_reset_memory():
    calc = Calculator()
    calc.add(10)
    assert calc.reset_memory() == 0


def test_add():
    calc = Calculator()
    assert calc.add(10) == 10


def test_add_two_arguments():
    calc = Calculator()
    calc.add(10)
    assert calc.add(10, 10) == 20


def test_subtract():
    calc = Calculator()
    assert calc.subtract(10) == -10


def test_subtract_two_arguments():
    calc = Calculator()
    assert calc.subtract(30, 10) == 20


def test_multiply():
    calc = Calculator()
    calc.add(10)
    assert calc.multiply(10) == 100


def test_multiply_two_arguments():
    calc = Calculator()
    calc.add(10)
    assert calc.multiply(10, 10) == 100


def test_divide():
    calc = Calculator()
    calc.add(100)
    assert calc.divide(10) == 10


def test_divide_two_arguments():
    calc = Calculator()
    calc.add(100)
    assert calc.divide(10, 2) == 5


def test_divide_by_zero():
    calc = Calculator()
    calc.add(10)
    with pytest.raises(ZeroDivisionError):
        calc.divide(0)


def test_divide_by_zero_two_arguments():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


def test_n_root():
    calc = Calculator()
    calc.add(100)
    assert calc.n_root(2) == 10


def test_n_root_two_arguments():
    calc = Calculator()
    calc.add(100)
    assert calc.n_root(2, 16) == 4


def test_n_root_by_zero():
    calc = Calculator()
    calc.add(10)
    with pytest.raises(ZeroDivisionError):
        calc.n_root(0)


def test_n_root_by_zero_two_arguments():
    calc = Calculator()
    calc.add(10)
    with pytest.raises(ZeroDivisionError):
        calc.n_root(0, 16)
