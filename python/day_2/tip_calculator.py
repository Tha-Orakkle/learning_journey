#calculates the bill + tip to be paid by each person

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip will you like to give? 10, 12 or 15? "))
people = int(input("How many people to split? "))

total_bill = bill + ((tip / 100) * bill)
#each_person = round(total_bill / people, 2)
each_person = "{:.2f}".format(total_bill / people)
print(f"Each person should pay: {each_person}")
