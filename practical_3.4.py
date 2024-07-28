# Write a program to get change values in Quarter, Dime,Nickels and Pennies, and calculate the value of change in
# Dollars. Consider Quarter = 0.25 $, Dime = 0.10 $, Nickels =0.05 $ and Penny = 0.01 $.
# simple take the value in dollar and convert then into the following given currency.

Dollar = float(input("Enter the value in dollar : "))
Quarter = Dollar * 4
Dime = Dollar * 10
Nickels = Dollar * 20
Penny = Dollar * 100

print(f"Dollar into Quarter is : {Quarter}")
print(f"Dollar into Dime is : {Dime}")
print(f"Dollar into Nickels is : {Nickels}")
print(f"Dollar into Penny is : {Penny}")