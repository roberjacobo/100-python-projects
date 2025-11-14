# addition, subtraction, multiplication and division


def addition(num1: float, num2: float) -> float:
    return num1 + num2


def subtraction(num1: float, num2: float) -> float:
    return num1 - num2


def multiplication(num1: float, num2: float) -> float:
    return num1 * num2


def division(num1: float, num2: float) -> float:
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2


message = """Select an option:
				1. Addition
				2. Subtraction
				3. Multiplication
				4. Division
				5. Exit
"""

i = 1
try:
    while i != 5:
        number = int(input(f"{message} \n"))
        i = number
        if i > 5 or i < 1: 
            raise ValueError("Option not allowed")

except ValueError:
    print("Option must be a number")
