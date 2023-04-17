pi2 = 3.14159
radius = float(input("Enter the radius of the circle:"))
print("\n******************MENU******************")
print("What do you want to compute?")
print("1. Diameter")
print("2. Circumference")
print("3. Area")
print("****************************************\n")

while True:
    choice = int(input("Enter your choice(1-3): "))
    if choice == 1:
        diameter = 2 * radius
        print("Diameter = ", diameter)
        break
    if choice == 2:
        circumference = 2 * pi2 * radius
        print("Circumference: ", circumference)
        break
    if choice == 3:
        area = pi2 * radius**2
        print("Area: ", area)
        break
    else:
        print("Invalid choice, please enter again")
        continue