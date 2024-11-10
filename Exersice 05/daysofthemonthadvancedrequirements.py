def get_days_month(month,year):
    # using dictionary to map all 12 months and the number of days
    month_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31 }
    
    # this is for the leap year so that the number of days in february is 29
    if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return 29
    
    return month_days.get(month, "Incorrect month")

# Get user input for the month and year
month = int(input("Enter month number: "))
year = int(input("Enter the year: "))

# Get the days of specified month
days = get_days_month(month, year)

# using if and else statement to cheack the month number
if days == "Incorrect month":
    print("Incorrect month number. enter a month number between 1 to 12.")
else:
    print(f"There are {days} days in month {month}.")