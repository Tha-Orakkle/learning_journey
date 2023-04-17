#!/usr/bin/python3

"""
A calculator program
Using a iteration and if statements
"""

from calculator_art import logo


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b


print(logo)
operators = ["+", "-", "*", "/"]
flag = False

n1 = float(input("What is your first number?: "))

while not flag:
    for op in operators:
        print(op)
    operand = input("pick an operator: ")
    n2 = float(input("What is your next number?: "))

    if operand == "+":
        result = add(n1, n2)
    elif operand == "-":
        result = sub(n1, n2)
    elif operand == "*":
        result = mul(n1, n2)
    elif operand == "/":
        result = div(n1, n2)

    print("{} ".format(n1) + operand + " {} = {}".format(n2, result))
    choice = input(f"Type 'y' to continue calculating with {result}," +
                   " or type 'n' to start a new calculation or" +
                   " type 'q' to end calculation: ").lower()
    if choice == "y":
        n1 = result
    elif choice == "n":
        n1 = float(input("What is your first number?: "))
    elif choice == "q":
        flag = True
