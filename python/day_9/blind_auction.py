#!/usr/bin/python3

import os
from blind_auction_art import logo
from subprocess import call


def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')


print(logo)
print("Welcome to the secret auction program")
end_of_auction = False
bid_log = {}
highest = 0
while not end_of_auction:
    bidder = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_log[bidder] = bid
    flag = input("Are there any other Bidders? Type 'yes' or 'no'.\n").lower()
    if flag == 'no':
        clear()
        end_of_auction = True
    else:
        clear()

for key in bid_log:
    check_bids = bid_log[key]
    if check_bids > highest:
        highest = check_bids
        highest_bidder = key

print("The winner is {} with a bid of ${}.".format(highest_bidder, highest))
