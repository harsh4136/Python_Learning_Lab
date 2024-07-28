# Write a program to find slope of an equation . equation = (y2 - y1) / (x2 - x1) .
x1 = float(input("Enter the value of x1 : "))
x2 = float(input("Enter the value of x2 : "))
y1 = float(input("Enter the value of y1 : "))
y2 = float(input("Enter the value of y2 : "))

slope = ((y2 - y1) / (x2 - x1))

print(f"Slope of an given equation is : {slope}")