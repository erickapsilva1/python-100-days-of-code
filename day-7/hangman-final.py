import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list

stages = hangman_art.stages

chosen_word = random.choice(word_list)
lives = 5

# Create blanks
secret = []
for l in chosen_word:
    secret += '_'

print(hangman_art.logo)
print(f'The solution is {chosen_word}')
print(secret)

while True:
    guess = input('Guess a letter: ').lower()
    
    if guess in secret:
        print(f"You've already guessed {guess}!")
    
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word! You lose a life.")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            secret[position] = letter
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
