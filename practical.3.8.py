# Write a program to determine the length of ladder required to reach a given height when leaned against the house. The
# height and the angle of the ladder are given as inputs (Use math Library).
import  math

# Input height and angle from the user
height = float(input("Enter the height the ladder needs to reach (in meters): "))
angle_degrees = float(input("Enter the angle of the ladder with the ground (in degrees): "))

# Convert the angle from degrees to radians
angle_radians = math.radians(angle_degrees)

# Calculate the length of the ladder using the sine function
ladder_length = height / math.sin(angle_radians)

# Output the length of the ladder
print(f"The length of the ladder required to reach the given height is: {ladder_length:.2f} meters") # '.2f' is used for rounding off the value .
