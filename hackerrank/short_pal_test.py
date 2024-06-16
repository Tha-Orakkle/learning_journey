#!/usr/bin/python3
"""shortest palindrome"""


def ispalindrome(s):
    """checks if str is a palindrome"""
    l = len(s)
    i = 0
    j = l - 1
    while i <= j:
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

def convert_palindrome(s):
    """coverts a word to a palindrome"""
    flag = 0
    tmp = s
    pre = ""

    while(len(tmp) > 0):
        if(ispalindrome(tmp)):
            flag = 1
            break
        else:
            pre += tmp[-1]
            tmp = tmp[:-1]

    if (flag):
        s = pre + s

    return s




if __name__ == "__main__":
    s = input()
    print(convert_palindrome(s))
