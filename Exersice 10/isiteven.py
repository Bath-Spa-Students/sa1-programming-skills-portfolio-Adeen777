# This function check if a number is even or odd.
def check_even_odd(num):
#Checking if the number is divisible by 2.
    if num % 2 == 0:
        return f"{num} is even."
    else:
# If not it is odd
        return f"{num} is odd."

#This is the main() for handling user input and displaying the result.
def main():
# This is asking user input of a number.
    try:
        my_num = int(input("Please enter a number: "))
# This is to call the function check_even_odd and get the result number.
        result_num = check_even_odd(my_num)
# print the result number.
        print(result_num)
    except ValueError:
# This is to check in case the user enters a non integer number.
        print("Incorrect input. enter only integer.")

# This line checks if script is being run directly or indirectly.
if __name__ == "__main__":
    main()