# ---------------------------------------------Question 1--------------------------------------------- #
"""
num = 0
sum = 0

while num < 3:
    x = int(input("Please enter three numbers: "))
    num += 1
    sum += x

print(sum)
"""


# ---------------------------------------------Question 2--------------------------------------------- #
"""
x = int(input("Maximum temperature: "))
y = int(input("Minimum temperature: "))
add = x + y
average = add/2

print("Average temperature is", average)
"""


# ---------------------------------------------Question 3--------------------------------------------- #
"""
x = input("Enter your name: ")
y = int(input("Enter your purchase amount: "))

while True:
    z = int(input("Enter the text code: "))
    if z == 0:
        tax_imposed = 0/100 * y
        break
    elif z == 1:
        tax_imposed = 6/100 * y
        break
    elif z == 2:
        tax_imposed = 16/100 * y
        break
    else:
        print("Invalid code, please enter again")
        continue

total = y + tax_imposed
print("Name:", x, "\nPurchase amount: RM", y, "\nTax imposed: RM", tax_imposed, "\nTotal amounts due: RM", total)
"""


# ---------------------------------------------Question 4--------------------------------------------- #
"""
num = 0
add = 0

while num < 10:
    x = input("Enter your student name: ")
    y = int(input("Enter your exam score: "))
    num += 1
    add += y

average = add/10
print("The average exam score is", average)
"""


# ---------------------------------------------Question 5--------------------------------------------- #
"""
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
bmi = weight / (height/100)**2
rounded_bmi = round(bmi, 2)
print("Your BMI is", rounded_bmi)

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 20:
    print("Your weight is normal.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
"""
