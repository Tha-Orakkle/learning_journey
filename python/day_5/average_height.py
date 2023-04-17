#!/usr/bin/python3
student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_sum = 0
count = 0

for n in student_heights:
    count += 1
    total_sum += n


average = round(total_sum / count)
print(average)
