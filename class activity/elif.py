a = 200
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#using input function to enter your marks
a = int(input("enter your marks: "))
#using if,elif and else statements to grade the marks
#using if statement to check if a greater or equal to 90
if a >= 90:
    print("your grade is A")
#using elif statement to check if a greater or equal to 80
elif a >= 80:
    print("your grade is B")
#using elif statement to check if a greater or equal to 70
elif a >= 70:
    print("you grade is C")
#using elif statement to check if a greater or equal to 60
elif a >= 60:
    print("your grade is D")
#using else statement to check if a lesser than 60
else:
    print("your grade is F")