import random

name = input('Please enter the name of the group [separated by comma]: ')

names_string = name.split(',')

choice = random.randint(0, len(names_string) - 1)

chosen = names_string[choice].strip()

print(f'{chosen} is going to buy the meal today!')
