#!/usr/bin/python3
#checks if a year is a leap year
year = int(input("Which year do you want to check? "))

if year % 4 == 0 or year % 400 == 0:
  if year % 100 == 0 and year % 400 != 0:
    print("Not leap year")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
