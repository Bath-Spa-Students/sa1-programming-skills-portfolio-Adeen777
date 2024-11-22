def find_name(name_list, search_name):
    if search_name in name_list:
        return f"{search_name} is found in list."
    else:
        return f"{search_name} is not found in list."

def main():
#list of names
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
 #asking user to enter the name they are searching for
    search_term = input("Enter the name you want to search for: ")
#Call the find_name function 
    result = find_name(names, search_term)
    print(result)

if __name__ == "__main__":
    main()
