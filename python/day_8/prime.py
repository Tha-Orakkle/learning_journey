#!/usr/bin/python3
import math

def prime_checker(number):
    flag = True
    temp = math.ceil(math.sqrt(number))
    while temp >= 2:
        if number % temp == 0:
            flag = False
        temp -= 1
    if flag == True or number == 1 or number == 2:
        print("{} is a prime number.".format(number))
    elif flag == False:
        print("{} is not a prime number.".format(number))

n = int(input("Check this number: "))
prime_checker(number=n)


#########################################

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
