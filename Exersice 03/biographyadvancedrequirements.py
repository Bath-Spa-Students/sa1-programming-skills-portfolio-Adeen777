# Creating a dictionary to store information 
my_info = {"name": input("enter your name (only enter your first and second name): "),"hometown": input("enter your hometown: ")}

my_age = input("Please enter your age: ")

while not my_age.isdigit():
    print("Invalid input! Please enter a valid age (numeric value).")
    my_age = input("Please enter your age: ")

# Convert the age to an integer
my_info["age"] = int(my_age)

# Printing information
print("Name:",my_info["name"])
print("Hometown:",my_info["hometown"])
print("Age:",my_info["age"])
