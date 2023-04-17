#!/usr/bin/python3

def commonPrefix(li):
    sz = len(li)
    if (sz == 0):
        return ""
    if (sz == 1):
        return li[0]

    min = sorted(li, key=lambda x:len(x))
    print(min)
    min = len(min[0])
    print(min)
    li.sort()
    print(li)

    i = 0
    while (i < min and li[0][i] == li[sz - 1][i]):
        i += 1

    prefix = li[0][0:i]
    return prefix

if __name__ ==  "__main__":
    li = input().split()
    print(li)
    print(commonPrefix(li))
