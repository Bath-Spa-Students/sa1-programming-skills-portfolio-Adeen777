def get_days_month(month):
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
    
    # Return number of days for month
    return month_days.get(month, "Incorrect month")

month = int(input("Enter the month number: "))

# Gets number of days in entered month
days = get_days_month(month)

# using if and else statement to cheack the month number
if days == "Incorrect month":
    print("Incorrect month number. enter a month number between 1 to 12.")
else:
    print(f"There are {days} days in month {month}.")
