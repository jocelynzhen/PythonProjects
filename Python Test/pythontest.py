# ---------------------------------------------Section A--------------------------------------------- #
# ---------------------------------------------Question 1--------------------------------------------- #
"""for i in range(1, 11):
    if i % 2 != 0:
        print(i ** 3)"""


# ---------------------------------------------Question 2--------------------------------------------- #
"""for i in range(1, 11):
    print("& " * i)
for i in range(9, 0, -1):
    print("& " * i)"""


# ---------------------------------------------Question 3--------------------------------------------- #
"""for i in range(50, 0, -1):
    print(i)"""


# ---------------------------------------------Question 4--------------------------------------------- #
"""list1 = [10, 15, 35, 48, 50, 55, 30, 60, 55, 75, 35, 55, 30, 25, 55]

while 55 in list1:
    list1.remove(55)

print(list1)"""


# ---------------------------------------------Question 5--------------------------------------------- #
# Best Answer
"""
print("**************************************************************")
print("Welcome to ABC Bookstore!")
print("We have two types of programming textbooks: Python and DBase.")
print("Python costs RM225 per book while DBase costs RM320 per book.")
print("**************************************************************")
print("")

python_price = 225
dbase_price = 320

total_python_books = 0
total_dbase_books = 0

while True:
    print("Please enter the number of books you want to purchase for each type of book (enter 0 for both to exit):")
    num_python_books = int(input("Number of Python books: "))
    num_dbase_books = int(input("Number of DBase books: "))

    if num_python_books == 0 and num_dbase_books == 0:
        print("Thank you for shopping with us. Goodbye!")
        break

    total_python_books += num_python_books
    total_dbase_books += num_dbase_books

    total_books = total_python_books + total_dbase_books

    python_cost = python_price * total_python_books
    dbase_cost = dbase_price * total_dbase_books
    total_cost = python_cost + dbase_cost

    if total_books <= 3:
        discount = 0.05
    elif 4 <= total_books <= 10:
        discount = 0.1
    else:
        discount = 0.2

    total_discount = total_cost * discount
    total_price_after_discount = total_cost - total_discount

    print("\nOrder Summary:")
    print("---------------")
    print(f"Number of Python books: {total_python_books}")
    print(f"Number of DBase books: {total_dbase_books}")
    print(f"Total number of books: {total_books}")
    print(f"Discount earned: {discount * 100}%")
    print(f"Total price before discount: RM{total_cost:.2f}")
    print(f"Total discount: RM{total_discount:.2f}")
    print(f"Amount due after discount: RM{total_price_after_discount:.2f}")
    print("")
"""

# Random Answer
"""
python_price = 225
dbase_price = 320

while True:
    python_books = int(input("Enter the number of Python books you want to purchase: "))
    dbase_books = int(input("Enter the number of DBase books you want to purchase: "))

    total_books = python_books + dbase_books
    total_price = python_books * python_price + dbase_books * dbase_price

    if total_books < 3:
        discount = 0.05
    elif total_books >= 4 and total_books <= 10:
        discount = 0.1
    else:
        discount = 0.2

    discount_amount = total_price * discount
    amount_due = total_price - discount_amount

    print("\nNumber of Python books purchased:", python_books)
    print("Number of DBase books purchased:", dbase_books)
    print("Discount earned: {}%".format(discount * 100))
    print("Amount due after discount: RM{:.2f}".format(amount_due))

    x = input("\nDo you want to purchase more books? (y/n): ")
    if x.lower() == "y":
        continue
    if x.lower() == "n":
        break
"""



# ---------------------------------------------Section B--------------------------------------------- #
# ---------------------------------------------Question 1--------------------------------------------- #
"""PROGRAM IterateAndDisplayNumbers
BEGIN
LOOP count FROM 1 TO 100 STEP 1
   		IF (i < 100) THEN
       			CONTINUE
   		ELSE
        			IF (i = 99) THEN
           				BREAK
        			ELSE
           				Print i
        			ENDIF
    		ENDIF
ENDLOOP
END"""


# ---------------------------------------------Question 2--------------------------------------------- #
"""PROGRAM CubeOfEvenNumbers
BEGIN
LOOP FROM 1 TO 10 STEP 1
    		IF (i % 2 == 0) THEN
        			cube = i * i * i
           			Print cube
    		ENDIF
ENDLOOP
END"""


