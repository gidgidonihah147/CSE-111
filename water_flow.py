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

#-----------------WEEK 06 ASSIGNMENT---------------#
# Purpose
# Prove that you can write a Python program and write and run test functions to help you find and fix mistakes in your program.

# Assignment
# Write the second half of the Python program to help an engineer design a water distribution system that you began in the previous lesson’s prove milestone. Also, write more test functions that will automatically verify that your program functions work correctly.


#-----------------Week 05 - Step 1---------------#
# Using VS Code, create a new file and save it as water_flow.py

#-----------------Week 05 - Step 3---------------#
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

#-----------------Week 05 - Step 5---------------#
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

#-----------------Week 05 - Step 7---------------#
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

#-----------------Week 06 - Step 1---------------#
# In your water_flow.py program, write a function named pressure_loss_from_fittings that calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline. The function must have this header:
# def pressure_loss_from_fittings(
#         fluid_velocity, quantity_fittings):
# In your function, use the following formula for calculating pressure loss from pipe fittings.

# P = (−0.04ρv2n)/2000 
# where
# P is the lost pressure in kilopascals
# ρ is the density of water (998.2 kilogram / meter3)
# v is the velocity of the water flowing through the pipe in meters / second
# n is the quantity of fittings

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    rho = 998.2
    return -0.04 * rho * fluid_velocity**2 * quantity_fittings / 2000

#-----------------Week 06 - Step 3---------------#
# In your water_flow.py program write a function named reynolds_number that calculates and returns the Reynolds number for a pipe with water flowing through it. The Reynolds number is a unitless ratio of the inertial and viscous forces in a fluid that is useful for predicting fluid flow in different situations. The function must have this header.
# def reynolds_number(hydraulic_diameter, fluid_velocity):
# In your function, use the following formula for calculating the Reynolds number.

# R = ρdv/μ
# where
# R is the Reynolds number
# ρ is the density of water (998.2 kilogram / meter3)
# d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
# v is the velocity of the water flowing through the pipe in meters / second
# μ is the dynamic viscosity of water (0.0010016 Pascal seconds)

def reynold_numbers(hydraulic_diameter, fluid_velocity):
    rho = 998.2
    dynamic_viscosity = 0.0010016
    return rho * hydraulic_diameter * fluid_velocity / dynamic_viscosity


#-----------------Week 06 - Step 5---------------#
# In your water_flow.py program write a function named pressure_loss_from_pipe_reduction that calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter. The function must have this header.
# def pressure_loss_from_pipe_reduction(larger_diameter,
#         fluid_velocity, reynolds_number, smaller_diameter):
# In your function, use the following two formulas for calculating pressure loss from a rounded reduction in a pipe’s diameter.

# k = (0.1 + 50) ((D/d)^4-1)
# P = (−kρv^2)/2000 
# where
# k is a constant computed by the first formula and used in the second formula
# R is the Reynolds number that corresponds to the pipe with the larger diameter
# D is the diameter of the larger pipe in meters
# d is the diameter of the smaller pipe in meters
# P is the lost pressure kilopascals
# ρ is the density of water (998.2 kilogram / meter3)
# v is the velocity of the water flowing through the larger diameter pipe in meters / second

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynold_number, smaller_diameter):
    rho = 998.2
    k = (0.1 + 50/reynold_number) * ((larger_diameter/smaller_diameter)**4 - 1)
    return -k * rho * fluid_velocity**2 / 2000

#-----------------Week 06 - Stretch 2---------------#
# The functions that you wrote for this assignment, calculate water pressure in kilopascals (kPa). In the United States, water pressure is usually expressed in pounds per square inch (psi). Write a function in your water_flow.py program that converts kPa to psi. Then at the bottom of your main function, add code that calls your conversion function and prints the final pressure value in both kPa and psi.

def kpa_to_psi(pressure_kpa):
  pressure_psi = pressure_kpa * 0.145038
  return pressure_psi

#-----------------Week 06 - Step 7---------------#
# Copy and paste the following code at the bottom of your water_flow.py program.
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynold_numbers(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

#-----------------Week 06 - Stretch 2---------------#
    # Convert kPa to psi and print the result
    pressure_psi = kpa_to_psi(pressure)
    print(f"Pressure at house: {pressure_psi:.2f} psi")


#-----------------Week 06 - Step 7---------------#
if __name__ == "__main__":
    main()