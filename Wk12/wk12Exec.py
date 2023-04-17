# Initial list
items = [10, 20, 30, 40, 50]

# Function to display the menu and get user input
def menu():
    print("\n********************************")
    print("1. Add new items to the list")
    print("2. Update an item in the list")
    print("3. Delete an item from the list")
    print("4. Display the list")
    print("5. Exit the program")
    print("********************************\n")
    choice = int(input("Enter your choice: "))
    return choice

# Function to add new items to the list
def add_items():
    for i in range(5):
        new_item = int(input("Enter a new item: "))
        items.append(new_item)
    print("New items have been added to the list.")

# Function to update an item in the list
def update_item():
    index = int(input("Enter the index of the item you want to update: "))
    if index >= len(items) or index < 0:
        print("Invalid index. Please try again.")
        return
    new_value = int(input("Enter the new value: "))
    items[index] = new_value
    print("Item has been updated.")

# Function to delete an item from the list
def delete_item():
    index = int(input("Enter the index of the item you want to delete: "))
    if index >= len(items) or index < 0:
        print("Invalid index. Please try again.")
        return
    del items[index]
    print("Item has been deleted.")

# Loop to continuously display the menu and perform the chosen action
while True:
    choice = menu()
    if choice == 1:
        print("This is your existing list: ", items)
        add_items()
        print("This is your existing list: ", items)
    elif choice == 2:
        print("This is your existing list: ", items)
        update_item()
        print("This is your existing list: ", items)
    elif choice == 3:
        print("This is your existing list: ", items)
        delete_item()
        print("This is your existing list: ", items)
    elif choice == 4:
        print(items)
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
