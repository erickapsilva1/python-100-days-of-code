import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
number_letters = int(input('How many letters would you like? '))
number_symbols = int(input('How many symbols would you like? '))
number_numbers = int(input('How many numbers would you like? '))

my_secret = []

for l in range(0, number_letters):
    my_secret += letters[random.randint(0, len(letters)-1)]

for s in range(0, number_symbols):
    my_secret += symbols[random.randint(0, len(symbols)-1)]

for n in range(0, number_numbers):
    my_secret += numbers[random.randint(0, len(numbers)-1)]

random.shuffle(my_secret)

for c in my_secret:
    print(c , end='')

print('')
