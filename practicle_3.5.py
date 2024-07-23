# Write a program to find a maximum of given three numbers (Use ternary operator).

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your thrid number : "))

if num1 > num2 and num1 > num3 :
    print(f"Maximum value from the given 3 number is : {num1}")
    
elif num2 > num1 and num2 > num3 :
    print(f"Maximum value from the given 3 number is : {num2}")
    
else :
    print(f"Maximum value from the given 3 number is : {num3}")

