# ------Week 04 Prepare--------
# Problem Statement
# Diagram of a right circular cone with radius r and height h
# A right circular cone with radius r and height h
# The following example Python program is supposed to ask the user for the radius and height of a right circular cone and then compute and print the volume of that cone. The code is almost correct, but it contains a common mistake. The programmer who wrote it assumed that the cone_volume function could use the radius and height variables that are defined in the main function. Of course, this assumption is incorrect because as the preparation content for this lesson explains, variables defined inside a function have local scope and can be used only inside their containing function.
    
# Assignment
# Do the following:

# Using VS Code, open a new file. Copy and paste all of the example program above into the new file. Save the new file as cone_volume.py
# Run your cone_volume.py program. What error message do you see in the terminal frame?
# Fix the cone_volume function which begins on line 37 by adding two parameters to its header. What parameter names should you use?

# Hint: the parameter names at line 37 and the variable names at line 39 must be the same.
# Fix the call to the cone_volume function that is in main at line 13 by adding two arguments. Because the cone_volume function has two parameters (you added the two parameters in the previous step), each call to the cone_volume function must have two arguments. What variable names should you use for the arguments?

# Hint: the only variables that you can use must be defined inside main above line 13.
# Fix the call to the cone_volume function that is in main at line 28 by adding two arguments. What variable names should you use for the arguments?

# Hint: the only variables that you can use must be defined inside main above line 28.
# Save your program and run it again. Did it run correctly? If not, fix the mistakes until it runs correctly.

"""Compute and print the volume of a right circular cone."""

# Import the standard math module so that
# math.pi can be used in this program.
import math


def main():
    # Call the cone_volume function to compute
    # the volume of an example cone.
    ex_radius = 2.8
    ex_height = 3.2
    ex_vol = cone_volume(ex_radius,ex_height)

    # Print several lines that describe this program.
    print("This program computes the volume of a right")
    print("circular cone. For example, if the radius of a")
    print(f"cone is {ex_radius} and the height is {ex_height}")
    print(f"then the volume is {ex_vol:.1f}")
    print()

    # Get the radius and height of the cone from the user.
    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))

    # Call the cone_volume function to compute the volume
    # for the radius and height that came from the user.
    vol = cone_volume(radius,height)

    # Print the radius, height, and
    # volume for the user to see.
    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {vol:.1f}")


def cone_volume(radius, height):
    """Compute and return the volume of a right circular cone."""
    volume = math.pi * radius**2 * height / 3
    return volume


# Start this program by
# calling the main function.
main()