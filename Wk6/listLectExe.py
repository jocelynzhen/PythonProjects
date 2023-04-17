# ---------------------------------------------Exercise 1--------------------------------------------- #
# Solution 1: List function
"""list1 = [100, 200, 300, 400, 500]
list1.sort(reverse=True)
print(list1)"""

# Solution 2: Using negative slicing
"""list1 = [100, 200, 300, 400, 500]
print(list1[::-1])"""

# Solution 3: List function
"""list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1 )"""


# ---------------------------------------------Exercise 2--------------------------------------------- #
# Using zip() function
"""list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

res = [i + j for i, j in zip(list1, list2)]
print(res)"""


# ---------------------------------------------Exercise 3--------------------------------------------- #
# Solution 1: Using loop
"""numbers = [1, 2, 3, 4, 5, 6, 7]
res = []
for i in numbers:
    res.append(i*i)
print(res)"""

# Solution 2: Using list comprehension
"""numbers = [1, 2, 3, 4, 5, 6, 7]
res = [i * i for i in numbers]
print(res)"""

# Solution 3: Using complex list comprehension
"""numbers = [1, 2, 3, 4, 5, 6, 7]
numbers1 = [int(numbers[i])**2 for i in range(len(numbers))]
print(numbers1)"""


# ---------------------------------------------Exercise 4--------------------------------------------- #
# Using zip() function
"""list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)"""


# ---------------------------------------------Exercise 5--------------------------------------------- #
# Solution 1: Using for loop
"""list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

new_list = []
for x in list1:
    if x != "":
        new_list.append(x)

print(new_list)"""

# Solution 2: Using a list comprehension
"""list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
new_list = [x for x in list1 if x != ""]
print(new_list)"""

# Solution 3: Using filter() function
"""list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
new_list = list(filter(None, list1))
print(new_list)"""

# Solution 4: Using filter and lambda
"""list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
new_list = list(filter(lambda x: x != "", list1))
print(new_list)"""


# ---------------------------------------------Exercise 6--------------------------------------------- #
# Using append() with indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000
"""list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)"""

# ---------------------------------------------Exercise 7--------------------------------------------- #
# Using extend
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']
"""Main_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

Main_list[2][1][2].extend(sub_list)
print(Main_list)"""


# ---------------------------------------------Exercise 8--------------------------------------------- #
# Solution 1: Using indexing
"""list1 = [5, 10, 15, 20, 25, 50, 20]
list1[3] = 200
print(list1)"""

# Solution 2: Using index(20)
"""list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)"""

# ---------------------------------------------Exercise 9--------------------------------------------- #
# Solution 1: Using for loop
"""list1 = [5, 20, 15, 20, 25, 50, 20]

new_list = []
for x in list1:
    if x != 20:
        new_list.append(x)

print(new_list)"""

# Solution 2: Using while loop
"""list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)"""

# Solution 3: Using a list comprehension
"""list1 = [5, 20, 15, 20, 25, 50, 20]
new_list = [x for x in list1 if x != 20]
print(new_list)"""

# https://pynative.com/python-list-exercise-with-solutions/
# https://www.programiz.com/python-programming/methods/list/append
