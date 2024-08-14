# Write a program that computes the real roots of a given quadratic equation (Use math libray).
# Discriminant = b**2 - (4 * a * c)  , real roots = (-b +/-  (discriminant**1/2))  / 2 * a  .
import math
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

Discriminant = (b**2) - ( 4 * a * c)

Real_Roots1 = ((-b) + math.sqrt(Discriminant)) / (2 * a)
Real_Roots2 = ((-b) - math.sqrt(Discriminant)) / (2 * a)

print(f"The real roots of the given equation is : {Real_Roots1} and {Real_Roots2}")
