#declaring the right password and its attempts
my_Pass=12345
maximum_attempt=5
i=0
# using while loop to ask the user password for 5 attempts
while i < maximum_attempt:
      password=int(input("Enter password:"))
# using if and else to check the password
      if password == my_Pass:
            print("Correct Password.")
            break
      else:
            i+=1
            if i < maximum_attempt:
             print(f"{maximum_attempt-i} attempts left")
            else:
             print("You have reached the maximum no: of attempts.the authorities have been alerted. ")
