from random import choice
from game_data import data
import os
import art

command = 'clear'
if os.name == 'nt': command = 'cls'
clear = lambda: os.system(command)

def print_data(person_data, letter):
    name = person_data['name']
    follower_count = person_data['follower_count']
    description = person_data['description']
    country = person_data['country']

    print(f"Compare {letter}: {name}, a {description}, from {country}.")

def more_followers(data1, data2):
    if data1['follower_count'] > data2['follower_count']: return True

user_score = 0
wrong_answer = False
person2 = choice(data)

while True:
    clear()
    person1 = person2
    person2 = choice(data)
    
    while person2 == person1:
        person2 = choice(data)

    print(art.logo)

    if user_score > 0 and not wrong_answer: 
        print(f"You're right! Current score: {user_score}")
    elif wrong_answer:
        print(f"Sorry, that's wrong. Final score {user_score}.")
        break

    print_data(person1, "A")
    print(art.vs)
    print_data(person2, "B")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    result = False

    if user_choice == 'a':
        result = more_followers(person1, person2)
        if result == True:
            print('You win!')
            user_score += 1
        else:
            wrong_answer = True
    else:
        result = more_followers(person2, person1)
        if result == True:
            print('You win!')
            user_score += 1
        else:
            wrong_answer = True




