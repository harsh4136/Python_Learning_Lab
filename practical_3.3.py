# Write a progame to find simple interest and compound interest .  equation for simple interest = (p * r * t) / 100
#                                                           equation for compound interest = p * (1 + (r/(100*n))^(n*t))

p = float(input("Enter principle amount : "))
r = float(input("Enter interest rate : "))
t = float(input("Enter time : "))
n = float(input("Enter the number of times interest applied per time period : "))   # n is always considered in months.

simple_interest = (p * r * t) / 100 
compound_interest = p * (1 + (r/(100*n)))^(n*t)

print(f"Simple Interest is : {simple_interest}")
print(f"Compund interest is : {compound_interest}")