# Initial the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# asking user name we're searching for
search_name = input("ENTER THE NAME YOU ARE LOOKING FOR: ")

# Check if the given name is in the list
if search_name in names:
    print(f"{search_name} was found ")
else:
    print(f"{search_name} was not found ")
