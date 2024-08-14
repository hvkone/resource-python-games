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
user_input = input("You are playing rock paper scissors. Enter 0 for rock, enter 1 for paper, enter 2 for scissors: ")
user_input = int(user_input)
options = [rock, paper, scissors]
print(f"You choose:\n{options[user_input]}")
#print(options[0].locals())
puter_choice = random.randint(0,2)
print(f"Computer choose:\n{options[puter_choice]}")

if user_input == puter_choice:
    print("It's a tie! Try again...")
elif user_input == 0:
    if puter_choice == 1:
        print("You lose. Paper beats rock.")
    else:
        print("You win! Rock beats scissors.")
elif user_input == 1:
    if puter_choice == 0:
        print("You win! Paper beats rock.")
    else:
        print("You lose. Scissors beats paper.")
elif user_input == 2:
    if puter_choice == 0:
        print("You lose. Rock beats scissors.")
    else:
        print("You win. Scissors beats paper!")
else:
    print("Please enter a value of 0-2")
