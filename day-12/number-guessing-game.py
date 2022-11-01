
# Intro
# PC escolhe num aleatório entre 1 e 100. 
# User escolhe dificuldade facil ou dificil
    # Facil 10 tentativas
    # Dificil 5 tentativas
# Valor acima too high - Adivinha de novo
    # Perde tentativa
# Valor abaixo too low - Adivinha de novo
    # Perde tentativa

from random import randint
from art import logo

number = randint(1, 100)
guesses = 0

print(logo)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    guesses_remaining = 10
elif difficulty == 'hard':
    guesses_remaining = 5
else:
    guesses_remaining = 0

def check_guess(number, guess):
    if number == int(guess): return True

def wrong_guess(number, guess):
   
    if int(guess) > number:
        print("Too high.")
        return guesses_remaining - 1
    else:
        print("Too low.")
        return guesses_remaining - 1

while guesses_remaining != 0:
    print(f"You have {guesses_remaining} attempts remaining to guess the number.")
    guess = input("Make a guess: ")

    if not check_guess(number, guess):
        guesses_remaining = wrong_guess(number, guess)
    else:
        print("You win!")
        break

if guesses_remaining == 0:
    print(f"You lose! The number is {number}.")