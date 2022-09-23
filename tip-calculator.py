print('Welcome to the tip calculator.')

bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people_to_split = int(input('How many people to split the bill? '))

bill_tip = bill * (1 + tip / 100)
bill_per_person = bill_tip / people_to_split

print('Each person should pay: ${:.2f}'.format(round(bill_per_person, 2)))
