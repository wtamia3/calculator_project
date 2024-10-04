# main.py
import sys
from calculator import Calculator

def main():
    if len(sys.argv) < 2:
        print("I don’t know how to read this.")
        return

    equation = ' '.join(sys.argv[1:])
    
    calculator = Calculator()
    try:
        result = calculator.evaluate(equation)
        print(f"The result is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
