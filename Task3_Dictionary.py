name = input("Enter your name: ")
age = input("Enter your age: ")
colour = input("Enter your favourite colour: ")

new_dict = {
    "name": name,
    "age": age,
    "colour": colour
}
print("User Information:")
for key, value in new_dict.items():
    print(f"{key}: {value}")