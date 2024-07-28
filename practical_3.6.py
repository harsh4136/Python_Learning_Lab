# Write a program to calculate area and volume of sphere. equation for area = 4*pi*r^r.
#                                                         equation for volume = 4/3 * pi * r^3.
import math
radius = float(input("Enter the value radius : "))

area = 4 * math.pi * radius**2
print(f"The area of sphere is : {area}")

volume = (4/3) * math.pi * radius**3
print(f"The volume of sphere is : {volume}")