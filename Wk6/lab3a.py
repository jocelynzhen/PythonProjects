# ---------------------------------------------Question 1--------------------------------------------- #
# ['Football', 'Tennis', 'Rugby']
"""
games = ["Football", "Tennis", "Rugby"]
print(games)
"""


# ---------------------------------------------Question 2--------------------------------------------- #
# Football
"""
games = ["Football", "Tennis", "Rugby"]
print(games[0])
"""


# ---------------------------------------------Question 3--------------------------------------------- #
# Tennis
"""
games = ["Football", "Tennis", "Rugby"]
print(games[1])
"""


# ---------------------------------------------Question 4--------------------------------------------- #
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
print(games[2])
"""


# ---------------------------------------------Question 5--------------------------------------------- #
# — IndexError: list index out of range —
"""
games = ["Football", "Tennis", "Rugby"]
print(games[3])
"""


# ---------------------------------------------Question 6--------------------------------------------- #
# — IndexError: list index out of range —
"""
games = ["Football", "Tennis", "Rugby"]
print(games[100])
"""


# ---------------------------------------------Question 7--------------------------------------------- #
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
print(games[-1])
"""


# ---------------------------------------------Question 8--------------------------------------------- #
# Tennis
"""
games = ["Football", "Tennis", "Rugby"]
print(games[-2])
"""


# ---------------------------------------------Question 9--------------------------------------------- #
# Football
"""
games = ['Football', 'Tennis', 'Rugby']
print(games[-3])
"""


# ---------------------------------------------Question 10--------------------------------------------- #
# — IndexError: list index out of range —
"""
games = ['Football', 'Tennis', 'Rugby']
print(games[-4])
"""


# ---------------------------------------------Question 11--------------------------------------------- #
# — IndexError: list index out of range —
"""
games = ['Football', 'Tennis', 'Rugby']
print(games[-100])
"""


# ---------------------------------------------Question 12--------------------------------------------- #
# Football
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(3):
    print(games[i])
"""


# ---------------------------------------------Question 13--------------------------------------------- #
# Football
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(0, 3):
    print(games[i])
"""


# ---------------------------------------------Question 14--------------------------------------------- #
# Football
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(0, 3, 1):
    print(games[i])
"""


# ---------------------------------------------Question 15--------------------------------------------- #
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(1, 3, 1):
    print(games[i])
"""


# ---------------------------------------------Question 16--------------------------------------------- #
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(2, 3, 1):
    print(games[i])
"""


# ---------------------------------------------Question 17--------------------------------------------- #
#  — no output —
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(3, 3, 1):
    print(games[i])
"""


# ---------------------------------------------Question 18--------------------------------------------- #
#  — no output —
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(4, 3, 1):
    print(games[i])
"""


# ---------------------------------------------Question 19--------------------------------------------- #
#  — no output —
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(100, 3, 1):
    print(games[i])
"""


# ---------------------------------------------Question 20--------------------------------------------- #
# Football
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(0, 3, 2):
    print(games[i])
"""


# ---------------------------------------------Question 21--------------------------------------------- #
# Tennis
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(1, 3, 2):
    print(games[i])
"""


# ---------------------------------------------Question 22--------------------------------------------- #
# Football
# Tennis
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(2):
    print(games[i])
"""


# ---------------------------------------------Question 23--------------------------------------------- #
# Football
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(1):
    print(games[i])
"""


# ---------------------------------------------Question 24--------------------------------------------- #
# — no output —
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(0):
    print(games[i])
"""


# ---------------------------------------------Question 25--------------------------------------------- #
# — no output —
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(-1):
    print(games[i])
"""


# ---------------------------------------------Question 26--------------------------------------------- #
# — no output —
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(-100):
    print(games[i])
"""


# ---------------------------------------------Question 27--------------------------------------------- #
# Football
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
for i in range(len(games)):
    print(games[i])
"""


# ---------------------------------------------Question 28--------------------------------------------- #
# Football
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
for game in games:
    print(game)
"""


# ---------------------------------------------Question 29--------------------------------------------- #
# Squash
# Football
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(0, "Squash")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 30--------------------------------------------- #
# Football
# Squash
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(1, "Squash")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 31--------------------------------------------- #
# Football
# Tennis
# Squash
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(2, "Squash")

for game in games:
    print(game)
"""

# ---------------------------------------------Question 32--------------------------------------------- #
# Football
# Tennis
# Rugby
# Squash
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(3, "Squash")

for game in games:
    print(game)
"""

# ---------------------------------------------Question 33--------------------------------------------- #
# Football
# Tennis
# Rugby
# Squash
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(4, "Squash")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 34--------------------------------------------- #
# Football
# Tennis
# Rugby
# Squash
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(10, "Squash")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 35--------------------------------------------- #
# Football
# Tennis
# Squash
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(-1, "Squash")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 36--------------------------------------------- #
# Football
# Squash
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(-2, "Squash")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 37--------------------------------------------- #
# Squash
# Football
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(-3, "Squash")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 38--------------------------------------------- #
# Squash
# Football
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(-4, "Squash")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 39--------------------------------------------- #
# Squash
# Football
# Tennis
# Rugby
"""
games = ["Football", "Tennis", "Rugby"]
games.insert(-100, "Squash")

for game in games:
    print(game)
"""
