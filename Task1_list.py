int_list = []

while True:
    user_input = input("Enter a number to add to the list (or type 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        add_number = int(user_input)
        int_list.append(add_number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("The final list is:", int_list)

#add all numbers in the list
results = sum(int_list)
print("The sum of all numbers in the list is:", results)