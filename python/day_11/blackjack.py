#!/usr/bin/python3

"""
A Blackjack Project
"""

import os
import random
from subprocess import call
from blackjack_art import logo


def clear():
    """clears the stdout"""
    _ = call('clear' if os.name == 'posix' else 'cls')


def deal_card():
    """returns a random card"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw. "
    elif computer_score == 0:
        return "You lose, opponent has a Blackjack "
    elif player_score == 0:
        return "You win with a Blackjack "
    elif player_score > 21:
        return "You lose, you went over "
    elif computer_score > 21:
        return "You win, opponent went over "
    elif player_score > computer_score:
        return "You win "
    else:
        return "You lose "


def play_game():
    clear()
    print(logo)
    is_game_over = False
    player_cards = []
    computer_cards = []
    for _ in range(0, 2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Opponent's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("==========")
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Opponent's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
