#!/usr/bin/python3

"""
A guessing game
"""

from guessing_game_art import logo
import random


def guess_game():
    """
    The guess game main function:
    takes a guess and checks if it matches
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a Number between 1 and 100")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lives = 10 if difficulty == 'easy' else 5
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > answer:
            print("Too high")
            print("Guess again.")
            lives -= 1
        elif guess < answer:
            print("Too low")
            print("Guess again")
            lives -= 1
        elif guess == answer:
            print(f"You got it! Your answer is {answer}.")
            break

        if lives == 0:
            print("You've run out of guesses, you lose.")


guess_game()
