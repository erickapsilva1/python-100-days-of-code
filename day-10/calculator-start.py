
# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 > 0:
        return n1 / n2
    else:
        return 'Infinity'


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

def calculator():
    num1 = int(input("What's the first number?: "))

    for operation in operations:
        print(operation)

    calculation_finished = False

    while not calculation_finished:

        operation_symbol = input('Pick an operation: ')
        next_number = int(input("What's the next number?: "))
        function = operations[operation_symbol]
        old_answer = num1
        answer = function(num1, next_number)
        print(f"{old_answer} {operation_symbol} {next_number} = {answer}")
        num1 = answer

        if answer != 'Infinity':
            should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'e' to exit. ").lower()
            if should_continue == 'e':
                calculation_finished = True
            else:
                calculator()
        else:
            break

calculator()