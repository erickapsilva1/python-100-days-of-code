from art import logo
from random import randint

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return cards[randint(0, len(cards)-1)]

def calculate_score(card_list):
    has_as = False
    has_ten = False

    if len(card_list) == 2:
        for card in card_list:
            if card == 11:
                has_as = True
            if card == 10:
                has_ten = True
        if has_as and has_ten:
            return 0
        else:
            return sum(card_list)

    has_as = False
    has_ten = False

    if len(card_list) > 2:
        for card in card_list:
            if card == 11:
                has_as = True
            if card == 10:
                has_ten = True
        if has_as and has_ten:
            card_list.remove(11)
            card_list.append(1)
            return sum(card_list)
        else:
            return sum(card_list)

def compare(u_score, c_score):
    if sum(u_score) > 21:
        return 'You lose'
    elif sum(c_score) > 21:
        return 'You win'
    elif sum(u_score) > sum(c_score):
        return 'You win'
    elif sum(c_score) > sum(u_score):
        return 'You lose'
    else:
        return 'Draw'

user_cards = []
computer_cards = []

print(logo)

while True:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    play_is_running = True

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    if want_to_play == 'y':

        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        if calculate_score(user_cards) == 0:
            print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score {calculate_score(computer_cards)}")
            print("Win, you have Blackjack")
            user_cards = []
            computer_cards = []
            play_is_running = False
    
        elif calculate_score(computer_cards) == 0:
            print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score {calculate_score(computer_cards)}")
            print("Lose, opponent has Blackjack")
            user_cards = []
            computer_cards = []
            play_is_running = False

        while play_is_running:

            want_to_draw = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
            while want_to_draw == 'y' and sum(user_cards) <= 21:
                user_cards.append(deal_card())  
                print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
                print(f"Computer's first card: {computer_cards[0]}")
                if sum(user_cards) < 21:
                    want_to_draw = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
            else:
                while sum(computer_cards) <= 17:
                    computer_cards.append(deal_card())
                
                print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
                print(f"Computer's final hand: {computer_cards}, final score {calculate_score(computer_cards)}")
                print(compare(user_cards, computer_cards))
                play_is_running = False

            user_cards = []
            computer_cards = []

    else:
        user_cards = []
        computer_cards = []
        break

