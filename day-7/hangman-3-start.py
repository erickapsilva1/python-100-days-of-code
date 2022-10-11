import random

word_list = ['ardvark','baboon','camel']

chosen_word = random.choice(word_list)

secret = []
for l in chosen_word:
    secret += '_'

print(f'The solution is {chosen_word}')
print(secret)

while True:
    guess = input('Guess a letter: ').lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            secret[position] = letter
        position += 1

    print(secret)
    
    if '_' not in secret:
        print('You win')
        break
