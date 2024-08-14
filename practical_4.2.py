# Many companies pay time-and-a-half for any hours worked above 40 hours in a given week. Write a program to input
# the number of hours worked and hourly rate and calculate the total wages for the week.
hours = float(input("Enter hours worked :  "))
rate = float(input("Enter hourly rate : "))
if hours > 40:
    total = 40 * rate + (hours - 40) * rate * 1.5
else:
    total = hours * rate
print("The total wages : ", total)