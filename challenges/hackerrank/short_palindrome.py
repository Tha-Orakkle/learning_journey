#!/usr/bin/python3
def short_palindrome(s):
    li1 = list(s)
    li2 = li1[:]
    li2 = li2.reverse()
    print(li1, end="\n========\n")
    print(li2)
    if li1 == li2:
        return s
    else:
        sub_str = list(s[1:])
        sub_str.reverse()
        pal = ''.join(sub_str)
        s = pal + s
        return s

if __name__ == "__main__":
    print(short_palindrome(input()))
