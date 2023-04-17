#!/usr/bin/python3
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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("You have made a wrong selection")

computer = random.randint(0, 2)
print("Computer chose: ")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if user_choice == computer:
    print("You draw")
elif user_choice == 0 and computer == 2:
    print("You win")
elif user_choice == 1 and computer == 0:
    print("You win")
elif user_choice == 2 and computer == 1:
    print("You win")
else:
    print("You lose. Computer wins.")
