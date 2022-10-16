import os
from art import logo

clear = lambda: os.system('clear')
clear()

print(logo)
print('Welcome to the secret auction program.')

continue_auction = True
auction = []

while continue_auction:
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    
    new_auction = {}
    new_auction['name'] = name
    new_auction['bid'] = bid

    auction.append(new_auction)

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if other_bidders == 'no':
        continue_auction = False
        max_bid_value = 0
        winner = ''
        for bid in auction:
            if bid['bid'] > max_bid_value:
                max_bid_value = bid['bid']
                winner = bid['name']
        print(f'The winner is {winner} with a bid of ${max_bid_value}.')
    else:
        clear()
    
    
