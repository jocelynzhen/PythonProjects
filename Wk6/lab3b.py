# ---------------------------------------------Question 1--------------------------------------------- #
# Football
# Tennis
# Rugby
# Squash
"""
games = ["Football", "Tennis", "Rugby"]
games.append("Squash")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 2--------------------------------------------- #
# — TypeError —
"""
games = ["Football", "Tennis", "Rugby"]
games.append("Squash", "Netball")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 3--------------------------------------------- #
# Football
# Tennis
# Rugby
# Squash
# Netball
"""
games = ["Football", "Tennis", "Rugby"]
games.append("Squash")
games.append("Netball")

for game in games:
    print(game)
"""


# ---------------------------------------------Question 4--------------------------------------------- #
# Football
# Tennis
# Rugby
# ['Squash', 'Netball', 'Cricket', 'Volleyball']
"""
firstList = ["Football", "Tennis", "Rugby"]
secondList = ["Squash", "Netball", "Cricket", "Volleyball"]

firstList.append(secondList)
for game in firstList:
    print(game)
"""


# ---------------------------------------------Question 5--------------------------------------------- #
# Squash
# Netball
# Cricket
# Volleyball
# ['Football', 'Tennis', 'Rugby']
"""
firstList = ["Football", "Tennis", "Rugby"]
secondList = ["Squash","Netball","Cricket", "Volleyball"]

secondList.append(firstList)
for game in secondList:
    print(game)
"""


# ---------------------------------------------Question 6--------------------------------------------- #
# Football
# Tennis
# Rugby
"""
firstList = ["Football", "Tennis", "Rugby"]
secondList = ["Squash", "Netball", "Cricket", "Volleyball"]

secondList.append(firstList)
for game in firstList:
    print(game)
"""


# ---------------------------------------------Question 7--------------------------------------------- #
# Football
# Tennis
# Rugby
# Squash
# Netball
# Cricket
# Volleyball
"""
firstList = ["Football", "Tennis", "Rugby"]
secondList = ["Squash", "Netball", "Cricket", "Volleyball"]

for game in secondList:
    firstList.append(game)

for game in firstList:
    print(game)
"""


# ---------------------------------------------Question 8--------------------------------------------- #
# Football
# Tennis
# Rugby
# Squash
# Netball
# Cricket
# Volleyball
"""
firstList = ["Football", "Tennis", "Rugby"]
secondList = ["Squash", "Netball", "Cricket", "Volleyball"]

firstList.extend(secondList)

for game in firstList:
    print(game)
"""


# ---------------------------------------------Question 9--------------------------------------------- #
# Cricket
# Football
# Netball
# Rugby
# Squash
# Tennis
# Volleyball
"""
firstList = ["Football", "Tennis", "Rugby"]
secondList = ["Squash", "Netball", "Cricket", "Volleyball"]

firstList.extend(secondList)

firstList.sort()
for game in firstList:
    print(game)
"""


# ---------------------------------------------Question 10--------------------------------------------- #
# Volleyball
# Tennis
# Squash
# Rugby
# Netball
# Football
# Cricket
"""
firstList = ["Football", "Tennis", "Rugby"]
secondList = ["Squash", "Netball", "Cricket", "Volleyball"]

firstList.extend(secondList)

firstList.sort(reverse=True)
for game in firstList:
    print(game)
"""
