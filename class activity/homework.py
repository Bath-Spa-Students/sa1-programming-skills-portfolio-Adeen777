# using int input to enter the marks in number
my_score = int(input("Enter your mark: ")) 
# using if,elif and else statements to grade the mark
if my_score >= 90:
  print("Your grade is A")
elif my_score >= 80:
  print("Your grade is B")
elif my_score >= 70:
  print("Your grade is C")
elif my_score >= 60:
  print("Your grade is D")
else:
  print("Your grade is F")