"""
Week 3 - Assignment 3: Calculator Class with Exception Handling
"""


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return None
        except TypeError:
            print("Error: Both inputs must be numbers.")
            return None
        else:
            return result


if __name__ == "__main__":
    calc = Calculator()

    print("Add:", calc.add(10, 5))
    print("Subtract:", calc.subtract(10, 5))
    print("Multiply:", calc.multiply(10, 5))
    print("Divide:", calc.divide(10, 5))
    print("Divide by zero:", calc.divide(10, 0))
    print("Divide with bad type:", calc.divide(10, "a"))
