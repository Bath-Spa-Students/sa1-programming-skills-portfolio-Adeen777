# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# The name we're searching for
search_name = input("enter the name your searching for: ")

# Check if 'Sam' is in the list
if search_name in names:
    print(f"{search_name} was found ")
else:
    print(f"{search_name} was not found ")