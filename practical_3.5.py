# Write a program to find a maximum of given three numbers (Use ternary operator).

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your thrid number : "))

max_value = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)

print(f"Maximum from the given three number is : {max_value}")