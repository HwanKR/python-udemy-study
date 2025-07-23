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

game_array = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_input = random.randint(0, 2)
fight = user_input-computer_input

print(game_array[user_input])
print(f"Computer chose: {computer_input}")
print(game_array[computer_input])

if user_input == computer_input:
    print("draw")
elif fight == -2 or fight == 1:
    print("You win")
else:
    print("You lose")