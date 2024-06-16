#!/usr/bin/python3
listInput = input().split()
prefix = ""
min = sorted(listInput, key=lambda x:len(x))
#for i in range(1, len(listInput)):
#    if len(listInput[i]) < len(min):
#        min = listInput[i]

min = min[0]
print(min)

for i in range(len(min)):
    flag = 0
    pre = ""
    for j in range(len(listInput) - 1):
        if listInput[j][i] == listInput[j + 1][i]:
            pre = listInput[j][i]
            flag += 1
        else:
            break;
    prefix += pre
    if flag > 0 and flag != len(listInput) - 1:
        prefix = prefix[:-1]
    if flag != len(listInput) - 1:
        break

print(prefix)

