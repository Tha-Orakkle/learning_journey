#!/usr/bin/python3
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_int = int(position)
i = int(position_int / 10)
j = position_int % 10
map[j - 1][i - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
