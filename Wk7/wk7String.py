# ---------------------------------------------Exercise 1--------------------------------------------- #
# Solution 1
"""str1 = "James"
print("Original String is", str1)
res = str1[0] + str1[2] + str1[4]
print("New String is:", res)"""

# Solution 2
"""str1 = "James"
print("Original String is", str1)

res = str1[0]                         # Get first character
length = len(str1)                    # Get string size
middle = int(length / 2)              # Get middle index number
res = res + str1[middle]              # Get middle character and add it to result
res = res + str1[length - 1]          # Get last character and add it to result

print("New String:", res)"""

# Solution 3
"""str1 = "James"
print("Original String is", str1)

length = len(str1)
middle = int(len(str1) / 2)
res = str1[0] + str1[middle] + str1[length - 1]

print("New String:", res)"""


# ---------------------------------------------Exercise 2--------------------------------------------- #
"""Str1 = "JohnDipPete"
Str2 = "JaSonAy"

mid1 = int(len(Str1)/2)
mid2 = int(len(Str2)/2)
res1 = Str1[mid1 - 1:mid1 + 2]
res2 = Str2[mid2 - 1:mid2 + 2]

print("Original String is", Str1)
print("Middle three chars are:", res1)
print("Original String is", Str2)
print("Middle three chars are:", res2)"""


# ---------------------------------------------Exercise 3--------------------------------------------- #
str1 = "PYnACtivE"
print("Original String:", str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to upper list
        upper.append(char)

# Join both list
sorted_str = "".join(lower + upper)
print("Result:", sorted_str)


# ---------------------------------------------Exercise 4--------------------------------------------- #


# ---------------------------------------------Exercise 5--------------------------------------------- #


# ---------------------------------------------Exercise 6--------------------------------------------- #


# ---------------------------------------------Exercise 7--------------------------------------------- #


# ---------------------------------------------Exercise 8--------------------------------------------- #


# ---------------------------------------------Exercise 9--------------------------------------------- #


# ---------------------------------------------Exercise 10--------------------------------------------- #

# https://pynative.com/python-string-exercise/
