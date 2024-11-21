# Creating a dictionary to store information 
my_info = {"name": input("enter your name (only enter your first and second name): "),"hometown": input("enter your hometown: ")}

# taking age outside the dictionary as age cannot be entered in string 
my_age = input("Please enter your age: ")

# cheaking if the age is a string or an integer
while not my_age.isdigit():
    print("your age must be entered in number!")
    my_age = input("Please enter your age: ")

# Converting age to integer
my_info["age"] = int(my_age)

# Printing information
print("Name:",my_info["name"])
print("Hometown:",my_info["hometown"])
print("Age:",my_info["age"])
