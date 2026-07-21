def calculator(a: float, b: float, operation: str):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":

        if b == 0:
            return "Cannot divide by zero."

        return a / b

    return "Invalid operation."