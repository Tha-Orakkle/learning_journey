#!/usr/bin/python3

"""
A calculator program
Using Recursion
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

operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
        }


def calculator():
    flag = False
    n1 = float(input("What's your first number?: "))

    while not flag:
        for op in operations:
            print(op)

        operator = input("Pick an operation: ")
        calculator_operation = operations[operator]
        n2 = float(input("What's your next number?: "))
        result = calculator_operation(n1, n2)

        print("{} {} {} = {}".format(n1, operator, n2, result))

        choice = input(f"Type 'y' to continue calculating with {result}," +
                       " or type 'n' to start a new calculation or" +
                       " type 'q' to end calculation: ").lower()
        if choice == "y":
            n1 = result
        elif choice == "n":
            calculator()
        elif choice == "q":
            flag = True


calculator()
