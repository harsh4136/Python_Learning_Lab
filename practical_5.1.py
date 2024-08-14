# Write a program to read n numbers from users and calculate the average of those n numbers.
n = int(input("Enter the value of n : "))
i = 1
sum = 0
average = 0

while i <= n :
    sum += i
    i += 1  
average = sum/n

print(f"The Average is : {average}")
