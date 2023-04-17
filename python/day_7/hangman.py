#!/usr/bin/python3

import random, os
from subprocess import call
from hangman_art import stages, logo
from hangman_words import word_list

def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

print(logo)


lives = 6
end_of_game = False
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}.")
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")

print(f"Word was \"{''.join(chosen_word)}\"")


