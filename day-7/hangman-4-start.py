import random

word_list = ['ardvark','baboon','camel']

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
lives = 5

secret = []
for l in chosen_word:
    secret += '_'

print(f'The solution is {chosen_word}')
print(secret)

while True:
    guess = input('Guess a letter: ').lower()
    #print(stages[lives+1])

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            secret[position] = letter
            wrong = False
        position += 1
    
    if guess not in chosen_word:
        lives -= 1
    print(stages[lives+1])
    print(secret)
    
    if '_' not in secret:
        print('You win')
        break
    elif lives < 0:
        print('You lose')
        break
