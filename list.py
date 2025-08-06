my_list =[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

my_list.insert(1, 15)  # Insert 15 at index 1
print(my_list)

new_list = [50, 60, 70]
my_list.extend(new_list)  # Extend my_list with new_list
print(my_list)

my_list.pop(-1)  # Remove the last element
print(my_list)

my_list.sort()  # Sort the list
print(my_list)      

for i in range(len(my_list)):
    if my_list[i] == 30:
        print("Found 30 at index", i)