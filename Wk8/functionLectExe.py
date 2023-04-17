# ---------------------------------------------Exercise 1--------------------------------------------- #
# Solution 1
"""def info(name, age):
    print(name, age)

info("Chris", 10)"""

# Solution 2  #Best Answer
"""def info(name, age):
    print("Hi", name, age, "welcome")

x = input("Enter name:")
y = int(input("Enter age:"))
info(x, y)"""


# ---------------------------------------------Exercise 2--------------------------------------------- #
# Solution 1
"""def calculation(a, b):
    add = a + b
    subtract = a - b
    return add, subtract

x = calculation(5, 3)
print(x)"""

# Solution 2  #Best Answer
"""def calculation(a, b):
    add = a + b
    subtract = a - b
    print(add)
    print(subtract)
    return add, subtract

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
calculation(x, y)"""

# ---------------------------------------------Exercise 3--------------------------------------------- #
def outer_fun(a, b):
    #square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)


# https://pynative.com/python-functions-exercise-with-solutions/

