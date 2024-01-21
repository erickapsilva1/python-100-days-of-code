list_of_strings = input().split(',')

# convert the strings to integer
list_of_integers = [int(n) for n in list_of_strings]

# filter the even numbers
result = [n for n in list_of_integers if n % 2 == 0]

print(result)