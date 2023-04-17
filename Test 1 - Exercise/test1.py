# ---------------------------------------------Section A--------------------------------------------- #
# ---------------------------------------------Question 1--------------------------------------------- #
"""
listA = [5, 10, 15, [20, 30, 40, [45, 55, 75], 50, 60], 100]
listA[3][3].append(65)
print(listA)
"""



# ---------------------------------------------Question 2--------------------------------------------- #
"""
numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
res = []
for i in numbers:
    res.append(i*i)
print(res)
"""



# ---------------------------------------------Question 3--------------------------------------------- #
"""
list1 = [10, 20, 30, 40, 50, 30, 60, 70, 80, 30]

while 30 in list1:
    list1.remove(30)
print(list1)
"""



# ---------------------------------------------Question 4--------------------------------------------- #
"""
for i in range(55, 3, -1):
    print(i)
"""



# ---------------------------------------------Question 5--------------------------------------------- #
"""
import math

def diameter(radius):
    return 2 * radius

def circumference(radius):
    return 2 * 3.14159 * radius

def area(radius):
    return 3.14159 * radius**2

def menu():
    radius = float(input("Enter the radius of the circle: "))
    print("\n******************MENU******************")
    print("What do you want to compute?")
    print("1. Diameter")
    print("2. Circumference")
    print("3. Area")
    print("****************************************\n")
    while True:
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            print("Diameter = ", diameter(radius))
            break
        elif choice == 2:
            print("Circumference = ", circumference(radius))
            break
        elif choice == 3:
            print("Area = ", area(radius))
            break
        else:
            print("Invalid choice, please enter again")
            continue

menu()
"""



# ---------------------------------------------Question 6--------------------------------------------- #
"""
income = 45000  # income in RM
tax = 0  # initialize tax to 0

if income > 15000:
    tax += 5000 * 0.1  # 10% tax on the next RM5,000
if income > 20000:
    tax += (income - 20000) * 0.2  # 20% tax on the remaining income

print("The income tax for RM45,000 is RM{:.2f}".format(tax))
"""

