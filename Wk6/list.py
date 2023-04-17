new_list = []
print(new_list)
##################################################
list1 = [1, 2, 3, 4, 5, 6]
print(list1)
##################################################
list2 = list(range(10))
print(list2)
##################################################
list3 = list(range(2, 7))
print(list3)
##################################################
new_list.append(3)
print(new_list)
##################################################
list1[4] = 145
print(list1)
##################################################
new_list.append("Hello")
print(new_list)
##################################################
new_list.append(123)
print(new_list)
##################################################
list1[4] = 345
print(list1)
##################################################
list1[4] = "hi"
print(list1)
##################################################
new_list1 = [3, 4, 5, 6]
new_list2 = [1, 24, 45]
new_list1.append(new_list2)
print(new_list1)
##################################################



##################################################
list7 = [1, 2, 3, 4, 5, 6]
for item in list7:
    print(item)

for item in list7:
    if (item == 4):
        print(item)
##################################################
list8 = ["John", "Cat", "Marry", "Gold"]
name = str(input("Enter a name to search for: "))
for item in list8:
    if(item == name):
        print(item)
    else:
        print("Can't be found")


