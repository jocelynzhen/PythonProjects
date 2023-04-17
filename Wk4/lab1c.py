# ---------------------------------------------Part A--------------------------------------------- #

# Question 1
"""
x = input("Enter your name: ")
print("Welcome, ", x)
"""


# Question 2
"""
x = input("Enter your name: ")
y = int(input("Enter your age: "))
print("Welcome, ", x)
print("You're", y, "years old")
"""


# ---------------------------------------------Part B--------------------------------------------- #

# Question 1
"""
x = int(input("Enter a number: "))
if x % 2 == 0:
    print("You picked an even number")
else:
    print("You picked an odd number")
"""


# Question 2
"""
x = int(input("Enter two numbers: "))
y = int(input("Enter two numbers: "))

if x > y:
    print("First number is the largest number")
else:
    print("Second number is the largest number")
"""


# ---------------------------------------------Part C--------------------------------------------- #

# Question 1 (for)
"""
for num in range(2, 50, 2):
    print(num)
"""

# (while_1)
"""
lar: int = 48
num = 2
while num <= lar:
    if num % 2 == 0:
        print(num)
    num = num + 1
"""

# (while_2)
"""
num = 2
while num <= 48:
    print(num)
    num = num + 2

"""

# ---------------------------------------------Part D--------------------------------------------- #

# Question 1
"""
x = int(input("Enter your score:"))
if 0 <= x < 40:
    print("D")
elif 40 <= x < 60:
    print("C")
elif 60 <= x < 80:
    print("B")
elif x >= 80:
    print("A")
else:
    print("Please enter again")
"""


# Question 2
"""
while True:
    vegetarian = input("Is anyone a vegetarian? ")
    vegan = input("Is anyone a vegan? ")
    gluten_free = input("Is anyone a gluten-free? ")

    if vegetarian == "no" and vegan == "no" and gluten_free == "no":
        print("Joe's Gourmet Burgers")
        break
    elif vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
        print("Main Street Pizza Company")
        break
    elif vegetarian == "yes" and vegan == "yes" and gluten_free == "yes":
        print("Corner Cafe" "\nThe Chef's Kitchen")
        break
    elif vegetarian == "yes" and vegan == "no" and gluten_free == "no":
        print("Mama's Fine Italian")
        break
    else:
        print("Enter either 'yes' or 'no'")
        continue
"""