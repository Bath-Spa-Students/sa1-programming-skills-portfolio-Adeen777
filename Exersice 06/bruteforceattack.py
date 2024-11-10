#declaring the right password
right_password = 12345

#using while loop to run the code until the user get the right answer
while True:
    password = int(input("enter password: "))
    if password == right_password:
              print("correcet password")
              break
    else:
        print("password is wrong.try again")