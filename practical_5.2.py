# Write a program that prompts the user to enter 10 integers and displays all the combinations of picking two numbers
# from the 10.

numbers = []
for i in range(10):
    number = int(input(f"Enter integer {i + 1}: "))
    numbers.append(number)
# print(numbers)