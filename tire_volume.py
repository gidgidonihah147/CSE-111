# Problem Statement
# The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

# v = 
# π w2 aw a + 2,540 d
# 10,000,000,000
# v is the volume in liters,
# π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.
# If you’re curious about how the above formula was derived, you can read the tire volume formula derivation.

# Assignment
# Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.

import math

print("You will be given 3 variables to enter to help calculate the volume of your tire. Please answer the following questions: ")
width = int(input("Enter the width of the tire in mm: "))
ar = int(input("Enter the aspect ratio of the tire: "))
diameter = int(input("Enter the diameter of the wheel in inches: "))

volume = round((math.pi*pow(width, 2)*ar*(width*ar+2540*diameter))/10000000000,2)

print(f"The aproxomate volume is {volume} liters")
