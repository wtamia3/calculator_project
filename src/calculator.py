# calculator.py
import re
from roman import RomanNumeralConverter

class Calculator:
    def __init__(self):
        self.converter = RomanNumeralConverter()

    def evaluate(self, equation):
        try:
            # Convert Roman numerals to integers
            integer_equation = self._convert_romans_to_integers(equation)
            result = self._evaluate_expression(integer_equation)
            return result
        except ZeroDivisionError:
            raise ValueError("There is no concept of a fractional number in Roman numerals.")
        except Exception as e:
            raise ValueError("I don’t know how to read this.")

    def _convert_romans_to_integers(self, equation):
        # Convert Roman numerals in the equation to integers
        return re.sub(r'([IVXLCDM]+)', lambda match: str(self.converter.to_integer(match.group(0))), equation)

    def _evaluate_expression(self, equation):
        # Implement logic to evaluate the equation respecting the order of operations
        # Use eval safely after replacing Roman numerals
        try:
            result = eval(equation)
            return result
        except Exception:
            raise ValueError("I don’t know how to read this.")
