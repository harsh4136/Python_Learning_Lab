# Function to determine if a year is a leap year
def is_leap_year(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

# Input: year to check
year = int(input("Enter the year you want to find whether it is a leap year or not: "))

# Check if the year is a leap year using the function
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
