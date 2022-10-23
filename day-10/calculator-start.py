
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
num2 = int(input("What's the second number?: "))

for operation in operations:
    print(operation)

operation_symbol = input('Pick an operation from the live above: ')

function = operations[operation_symbol]

answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
