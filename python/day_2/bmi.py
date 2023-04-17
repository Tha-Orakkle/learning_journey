#calculates the body mass index(BMI) of the user

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height = float(height)
weight = float(weight)
print(int(weight / (height ** 2)))
