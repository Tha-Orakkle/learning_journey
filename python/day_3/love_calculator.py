#!/usr/bin/python3
"""
Take both people's names and check for the number of times
the letters in the word TRUE occurs. Then check for the
number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
"""


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
name = combined_name.lower()

t = 0
l = 0
for i in "true":
    t += name.count(i)
for i in "love":
    l += name.count(i)
total = int(str(t) + str(l))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
