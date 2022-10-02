print('Welcome to [Py]zza Deliveries!')

size = input('What size pizza do you want? [S, M, L] ')
add_pepperoni = input('Do you want pepperoni? [Y, N] ')
extra_chesse = input('Do you want extra chesse? [Y, N] ')

small_size = 15
medium_size = 20
large_size = 25
pepperoni_small = 2
pepperoni_medium_large = 3
extra_cheese = 1
final_bill = 0

if extra_cheese.upper() == 'S':
    final_bill += 1

if size.upper() == 'S':
    final_bill += small_size
    if add_pepperoni.upper() == 'Y':
        final_bill += pepperoni_small

if size.upper() == 'M':
    final_bill += medium_size
    if add_pepperoni.upper() == 'Y':
        final_bill += pepperoni_medium_large

if size.upper() == 'L':
    final_bill += large_size
    if add_pepperoni.upper() == 'Y':
        final_bill += pepperoni_medium_large

print(f'Your final bill is: ${final_bill}.')
