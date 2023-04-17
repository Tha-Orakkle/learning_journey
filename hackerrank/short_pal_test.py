#!/usr/bin/python3
def ispalindrome(s):
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
