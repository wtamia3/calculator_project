import pytest
from src.roman import RomanNumeralConverter

def test_to_integer():
    converter = RomanNumeralConverter()
    assert converter.to_integer('X') == 10
    assert converter.to_integer('IX') == 9
    assert converter.to_integer('MMXX') == 2020

def test_to_roman():
    converter = RomanNumeralConverter()
    assert converter.to_roman(10) == 'X'
    assert converter.to_roman(9) == 'IX'
    assert converter.to_roman(2020) == 'MMXX'

def test_invalid_input_to_roman():
    converter = RomanNumeralConverter()
    with pytest.raises(ValueError):
        converter.to_roman(0)
    with pytest.raises(ValueError):
        converter.to_roman(4000)
