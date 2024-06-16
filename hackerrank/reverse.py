#!/usr/bin/python3
if __name__ == "__main__":
    output = ""
    num = list(input())
    if num[0] == "-":
        output += "-"
        num.remove("-")
    num.reverse()
    if int(num[0]) == 0:
        num.remove(num[0])
    output += ''.join(num)
    print(output)
