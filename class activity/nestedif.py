salary = int(input("enter your salary : "))
if salary >= 30000:
    years_on_job = float(input("enter the years of job : "))
    if  years_on_job >= 2:
        print ("your qualified for your job ")
    else:
        print("experience is less than 2 ")

else:
    print("you earn atleast 30k to qualify")

