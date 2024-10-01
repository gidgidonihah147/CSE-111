#-----------------WEEK 03 ASSIGNMENT---------------#
# Purpose
# Check your understanding of writing your own functions with parameters and then calling those functions with arguments.

# Problem Statement
# Many vehicle owners record the fuel efficiency of their vehicles as a way to track the health of the vehicle. If the fuel efficiency of a vehicle suddenly drops, there is probably something wrong with the engine or drive train of the vehicle. In the United States, fuel efficiency for gasoline powered vehicles is calculated as miles per gallon. In most other countries, fuel efficiency is calculated as liters per 100 kilometers.

# The formula for computing fuel efficiency in miles per gallon is the following:

# mpg = 
# end − start
# gallons
# where start and end are both odometer values in miles and gallons is a fuel amount in U.S. gallons.

# The formula for converting miles per gallon to liters per 100 kilometers is the following:

# lp100k = 
# 235.215
# mpg
# Assignment
# Write a Python program that asks the user for three numbers:

# A starting odometer value in miles
# An ending odometer value in miles
# An amount of fuel in gallons
# Your program must calculate and print fuel efficiency in both miles per gallon and liters per 100 kilometers. Your program must have three functions named as follows:

# main
# miles_per_gallon
# lp100k_from_mpg
# All user input and printing must be in the main function. In other words, the miles_per_gallon and lp100k_from_mpg functions must not call the the input or print functions.





def main():
    # Get an odometer value in U.S. miles from the user.
    odometerStart = float(input("Please enter a starting odometer value in miles: "))
    print ()
    # Get another odometer value in U.S. miles from the user.
    odometerEnd = float(input("Please enter a ending odometer value in miles: "))
    # Get a fuel amount in U.S. gallons from the user.
    gallons = float(input("Please enter the amount of fuel used in gallons: "))
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = float(miles_per_gallon(odometerStart, odometerEnd, gallons))
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    # Display the results for the user to see.
    print(f"Your MPG is {mpg}, and your lp100k is {lp100k}")
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    #figure out the miles from the odometer amounts entered by the user
    miles = end_miles - start_miles
    #Figure out the mpg Miles entered / gallons entered
    mpg = round(miles/amount_gallons,2)
    #return the mpg calculated to main for use elsewhere
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    #conversion to km. Googled to get the ratio
    km = round(235.2145/mpg,2)
    #return km to main for use elsewehere
    return km


# Call the main function so that
# this program will start executing.
main()