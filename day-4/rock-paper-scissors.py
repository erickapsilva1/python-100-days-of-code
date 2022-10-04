import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))

computer_choice = random.randint(0,2)

#print(f'Your choice: {player_choice} PC choice: {computer_choice}')

if player_choice == 0 and computer_choice == 0:
    print(f'{rock}\nComputer chose: \n {rock} \n Draw.')
elif player_choice == 0 and computer_choice == 1:
    print(f'{rock}\nComputer chose: \n {paper} \n You lose.')
elif player_choice == 0 and computer_choice == 2:
    print(f'{rock}\nComputer chose: \n {scissors} \n You win.')

if player_choice == 1 and computer_choice == 0:
    print(f'{paper}\nComputer chose: \n {rock} \n You win.')
elif player_choice == 1 and computer_choice == 1:
    print(f'{paper}\nComputer chose: \n {paper} \n Draw.')
elif player_choice == 1 and computer_choice == 2:
    print(f'{paper}\nComputer chose: \n {scissors} \n You lose.')

if player_choice == 2 and computer_choice == 0:
    print(f'{scissors}\nComputer chose: \n {rock} \n You lose.')
elif player_choice == 2 and computer_choice == 1:
    print(f'{scissors}\nComputer chose: \n {paper} \n You win.')
elif player_choice == 2 and computer_choice == 2:
    print(f'{scissors}\nComputer chose: \n {scissors} \n Draw.')

if player_choice > 2:
    print('You typed an invalid number. You lose!')
