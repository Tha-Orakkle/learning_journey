#!/usr/bin/python3

def greet_with(name, location):
    print("Hello {}, How are you.".format(name))
    print(f"How is the weather in {location}?")

name = input("What is your name? ")
location = input("Where are you from? ")
greet_with(name, location)
