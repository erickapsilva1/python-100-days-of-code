
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

num1 = int(input("What's the first number?: "))

for operation in operations:
    print(operation)

operation_symbol = input('Pick an operation: ')
num2 = int(input("What's the second number?: "))

function = operations[operation_symbol]
answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ").lower()

while should_continue:

    if should_continue == 'y':
        operation_symbol = input('Pick an operation: ')
        next_number = int(input("What's the next number?: "))
        function = operations[operation_symbol]
        old_answer = answer
        answer = function(answer, next_number)
        print(f"{old_answer} {operation_symbol} {next_number} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ").lower()
    else:
        break

