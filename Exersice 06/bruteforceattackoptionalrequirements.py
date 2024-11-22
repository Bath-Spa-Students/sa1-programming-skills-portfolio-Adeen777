Pass=12345
maximum_attempt=5
i=0
while i < maximum_attempt:
      password=int(input("Enter the password:"))
      if password==Pass:
            print("Correct Password.")
            break
      else:
            i+=1
            if i < maximum_attempt:
             print(f"{maximum_attempt-i} attempts left")
            else:
             print("You have reached the maximum no: of attempts.the authorities have been alerted. ")