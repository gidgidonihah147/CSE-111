#-----------------WEEK 05 ASSIGNMENT---------------#
# # Problem Statement
# Getting clean water to all buildings in a city is a large and expensive task. Many cities will build an elevated water tank, and install a pump that pushes water up to the tank where the water is stored. In the city, when a thirsty person opens a water faucet, water runs from the tank through pipes to the faucet. Earth’s gravity pulling on the water in the elevated tank pressurizes the water and causes it to spray from the faucet.

# A diagram of a city water distribution system that stores water in an elevated tank
# Before a city builds a water distribution system, an engineer must design the system and ensure water will flow to all buildings in the city. An engineer must choose the tower height, pipe type, pipe diameter, and pipe path. Engineers use software to help them make these choices and design a working water distribtuion system.

# Assignment
# Write a Python program that could help an engineer design a water distribution system. During this prove milestone, you will write three program functions and three test functions as described in the Steps section below.

# Helpful Documentation
# The preparation content for this lesson explains how to use pytest, assert, and approx to automatically verify that functions are correct. It also contains an example test function and links to additional documentation about pytest.
# The pytest approx function accepts optional named arguments. One of those named arguments is abs. The abs named argument causes the approx function to compare the actual and expected values up to a specified digit after the decimal point and to ignore the following digits. For example, the following two lines of code cause pytest to compare the actual number returned from pressure_loss_from_fittings to −0.306 to only the third digit after the decimal point and to ignore all digits in the actual number after the 6.
#     assert pressure_loss_from_fittings(1.75, 5) \
#         == approx(-0.306, abs=0.001)
# Notice in the previous example, that the value for abs is 0.001, which causes the approx function to ignore all digits after the third digit after the decimal point.

#-----------------Step 1---------------#
# Using VS Code, create a new file and save it as water_flow.py

#-----------------Step 3---------------#
# In your water_flow.py program, write a function named water_column_height that calculates and returns the height of a column of water from a tower height and a tank wall height. The function must have this header:
# def water_column_height(tower_height, tank_height):
# In your function, use the following formula for calculating the water column height.
# h = t + (3w/4)
# where
# h is height of the water column
# t is the height of the tower
# w is the height of the walls of the tank that is on top of the tower

def water_column_height(tower_height, tank_height):
    return tower_height + 3 * tank_height / 4

#-----------------Step 5---------------#
# In your water_flow.py program, write a function named pressure_gain_from_water_height that calculates and returns the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank. The function must have this header:
# def pressure_gain_from_water_height(height):
# In your function, use the following formula for calculating pressure caused by Earth’s gravity.

# P = ρgh/1000
# where
# P is the pressure in kilopascals
# ρ is the density of water (998.2 kilogram / meter3)
# g is the acceleration from Earths gravity (9.80665 meter / second2)
# h is the height of the water column in meters

def pressure_gain_from_water_height(height):
    rho = 998.2 
    g = 9.80665
    return rho * g * height / 1000

#-----------------Step 7---------------#
# In your water_flow.py program, write a function named pressure_loss_from_pipe that calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through. The function must have this header:
# def pressure_loss_from_pipe(pipe_diameter,
#         pipe_length, friction_factor, fluid_velocity):
# In your function, use the following formula for calculating pressure loss from friction within a pipe.

# P = − f L ρ v^2 / 2000 d
# where
# P is the lost pressure in kilopascals
# f is the pipe’s friction factor
# L is the length of the pipe in meters
# ρ is the density of water (998.2 kilogram / meter3)
# v is the velocity of the water flowing through the pipe in meters / second
# d is the diameter of the pipe in meters

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    rho = 998.2
    return -friction_factor * pipe_length * rho * fluid_velocity**2 / (2000 * pipe_diameter)