# ---------------------------------------------Question 1--------------------------------------------- #
# Solution 1: Using while loop
"""list1 = []
num = 0

while num < 10:
    x = str(input("Enter 10 elements: "))
    num += 1
    list1.append(x)

print(list1)"""

# Solution 2: Using for loop
"""list1 = []

for i in range(10):
    x = str(input("Enter 10 elements: "))
    list1.append(x)
    
print(list1)"""


# ---------------------------------------------Question 2--------------------------------------------- #
# Solution 1: Using for loop
"""list2 = []
n = int(input("Enter the size of the list: "))

for i in range(0, n):  # for i in range(n)
    ele = int(input("Enter a number: "))
    list2.append(ele)

print(list2)
for i in range(0, n):  # for i in range(n)
    total = sum(list2)
print("The sum of all elements in the list is ", total)"""

# Solution 2: Using while loop
"""n = 0
total = 0
list2 = []
length = int(input("Enter the size of the list: "))

while n < length:
    ele = int(input("Enter a number: "))
    list2.append(ele)
    n += 1

total = sum(list2)

print(list2)
print("The sum of all elements in the list is ", total)"""


# ---------------------------------------------Question 3--------------------------------------------- #
# Solution 1: Using while loop
"""list3 = []
i = 0
n = int(input("Enter the number of students in class: "))

while i < n:
    name = str(input("Enter their names: "))
    list3.append(name)
    i += 1

print(list3)"""

# Solution 2: Using for loop
"""list3 = []
n = int(input("Enter the number of students in class: "))

for i in range(0, n):
    name = str(input("Enter their names: "))
    list3.append(name)

print(list3)"""


# ---------------------------------------------Question 4--------------------------------------------- #
"""list4 = [65, 75, 85, 95, 105]

def check_number ():
    num = int(input("Enter a number to search for: "))
    if num in list4:
        print(num, "is available in the list")
    else:
        print(num, "is not available in the list")

check_number()"""


# ---------------------------------------------Question 5--------------------------------------------- #
# Solution 1: Using a while loop
"""list5 = []
n = 0
num = int(input("Enter the number of total students in class: "))

while n < num:
    marks = int(input("Enter their class test marks: "))
    n += 1
    list5.append(marks)

average = sum(list5)/num
print("Average: ", average)"""

# Solution 2: Using a for loop
"""list5 = []
num = int(input("Enter the number of total students in class: "))

for i in range(0, num):
    marks = int(input("Enter their class test marks: "))
    list5.append(marks)

average = sum(list5)/num
print("Average: ", average)"""


# ---------------------------------------------Question 6--------------------------------------------- #
# Solution 1: List function
"""listA = [100, 200, 300, 400, 500]
listA.sort(reverse=True)
print(listA)"""

# Solution 2: Using negative slicing
"""listA = [100, 200, 300, 400, 500]
print(listA[::-1])"""

# Solution 3: List function
"""listA = [100, 200, 300, 400, 500]
listA.reverse()
print(listA)"""


# ---------------------------------------------Question 7--------------------------------------------- #
# Solution 1: Using loop
"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = []
for i in numbers:
    res.append(i*i)
print(res)"""

# Solution 2: Using list comprehension
"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i * i for i in numbers]
print(res)"""

# Solution 3: Using complex list comprehension
"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1 = [int(numbers[i])**2 for i in range(len(numbers))]
print(numbers1)"""


# ---------------------------------------------Question 8--------------------------------------------- #
# Solution 1
"""list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
res = [i + j for i in list1 for j in list2]
print(res)"""

# Solution 2
"""list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
list3 = []

for x in list1:
    for y in list2:
        list3.append(x + " " + y)

print(list3)"""


# ---------------------------------------------Question 9--------------------------------------------- #
"""list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)"""


# ---------------------------------------------Question 10--------------------------------------------- #
"""name = input("Student name: ")
tp_num = input("TP Number: ")
num = int(input("Total number of subjects: "))
list10 = []

for i in range(0, num):
    marks = int(input("Enter all your subject marks: "))
    list10.append(marks)

percentage = (sum(list10)/num)
print("**********************************************")
print("Student name: ", name)
print("TP Number: ", tp_num)
print("Total marks: ", sum(list10))
print("Average percentage: ", percentage, "%")

if 0 <= percentage <= 49:
    print("Grade of the semester: D/Fail")
elif 50 <= percentage <= 55:
    print("Grade of the semester: C-")
elif 56 <= percentage <= 59:
    print("Grade of the semester: C")
elif 60 <= percentage <= 65:
    print("Grade of the semester: C+")
elif 66 <= percentage <= 69:
    print("Grade of the semester: B")
elif 70 <= percentage <= 75:
    print("Grade of the semester: B+")
elif 76 <= percentage <= 79:
    print("Grade of the semester: A")
elif 80 <= percentage <= 100:
    print("Grade of the semester: A+")"""
