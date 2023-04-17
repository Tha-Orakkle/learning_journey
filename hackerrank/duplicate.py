#!/usr/bin/python3
def checkDuplicate(li):
    dup = "false"
    for i in range(len(li)):
        for j in range(len(li)):
            if i == j:
                continue
            if (int(li[j]) == int(li[i])):
                dup = "true"

    return dup

if __name__ == "__main__":
    li = input().split()
    print(checkDuplicate(li))
