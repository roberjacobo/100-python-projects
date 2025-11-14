# addition, subtraction, multiplication and division


def function_helper(option):
    operations = {1: addition, 2: subtraction, 3: multiplication, 4: division}
    return operations[option]


def addition(num1: float, num2: float) -> float:
    print(f"{num1} + {num2}:")
    return num1 + num2


def subtraction(num1: float, num2: float) -> float:
    print(f"{num1} - {num2}:")
    return num1 - num2


def multiplication(num1: float, num2: float) -> float:
    print(f"{num1} * {num2}:")
    return num1 * num2


def division(num1: float, num2: float) -> float:
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    print(f"{num1} / {num2}:")
    return num1 / num2


message = """Select an option:
				1. Addition
				2. Subtraction
				3. Multiplication
				4. Division
				5. Exit
"""

i = 1
while i != 5:
    try:
        number = int(input(f"{message} \n"))
        i = number
        if i > 5 or i < 1:
            print("Invalid option. Please select 1 - 5.")
            continue
        if 1 <= i <= 4:
            # Get user inputs
            num1 = float(input("Enter first number\n"))
            num2 = float(input("Enter second number\n"))

            # Get the operation function and perform operation
            result = function_helper(i)(num1, num2)
            print(f"Result: {result}")

    except ValueError:
        print("Option must be a number.")
    except ZeroDivisionError as e:
        print(e)
