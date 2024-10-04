# roman.py
class RomanNumeralConverter:
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }

    def to_integer(self, roman):
        total = 0
        prev_value = 0
        
        for char in reversed(roman):
            value = self.roman_numerals.get(char)
            if value is None:
                raise ValueError("Invalid Roman numeral")
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
            
        return total

    def from_integer(self, number):
        # Implement conversion from integer to Roman numeral if needed
        pass
