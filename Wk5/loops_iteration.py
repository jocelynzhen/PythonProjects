# Slide 5
"""
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!!")
print(n)
"""


# Slide 6
"""
n = 5
while n > 0:
    print("Lather")
    print("Rinse")
print("Dry off!")
"""


# Slide 7
"""
n = 0
while n > 0:
    print("Lather")
    print("Rinse")
print("Dry off!")
"""


# Slide 8
"""
while True:
    line = input(">")
    if line == "done":
        break
    print(line)
print("Done!")
"""


# Slide 11
"""
while True:
    line = input(">")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")
"""


# Slide 15
"""
for i in[5,4,3,2,1]:
    print(i)
print("Blastoff!")
"""


# Slide 16
"""
friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year:", friend)
print("Done!")
"""


# Slide 22
"""
print("Before")
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print("After")
"""


# Slide 23
"""
zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork += thing     # zork = zork + thing
    print(zork, thing)
print("After", zork)
"""


# Slide 24
"""
count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count += 1        # count = count + 1
    sum += value      # sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum/count)
"""