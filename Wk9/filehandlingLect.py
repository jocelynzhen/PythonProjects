# Opens a file for reading (default value), error is the file doesn't exist
"""fhand = open("testing1.txt", "r")"""

# Opens a file for appending (at the end of file), creates the file if it doesn't exist
"""fhand = open("testing1.txt", "a")"""

# Opens a file for writing (any existing content), creates the file if it doesn't exist
"""fhand = open("testing1.txt", "w")"""

# Creates the specified file, error iif the file exists
"""fhand = open("testing1.txt", "x")"""


# Read and Print the data of test file
"""fhand = open("testing1.txt", "r")
print(fhand.read())"""


# Write to existing file
f = open("testing1.txt", "a")
f.write("\nNow the file has more content!")
f.close()
f = open("testing1.txt", "r")
print(f.read())
f.close()
