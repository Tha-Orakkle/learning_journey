#!/usr/bin/python3
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

how_many_people = len(names)
i = random.randint(0, how_many_people - 1)
print(f"{names[i]} is going to buy the meal today!")
