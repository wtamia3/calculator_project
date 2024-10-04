import pytest
from src.calculator import Calculator

def test_simple_addition():
    calculator = Calculator()
    result = calculator.evaluate('V + III')
    assert result == 8

def test_multiplication_with_grouping():
    calculator = Calculator()
    result = calculator.evaluate('(VII + III) * II')
    assert result == 20

def test_invalid_input():
    calculator = Calculator()
    with pytest.raises(ValueError):
        calculator.evaluate('VII + XX +')
