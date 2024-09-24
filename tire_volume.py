#-----------------WEEK 01 ASSIGNMENT---------------#
# Problem Statement
# The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the tireWidth of the tire in millimeters. The second number is the aspect ratio. The third number is the tireDiameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

# v = 
# π w2 aw a + 2,540 d
# 10,000,000,000
# v is the volume in liters,
# π is the constant PI, which is the ratio of the circumference of a circle divided by its tireDiameter (use math.pi),
# w is the tireWidth of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the tireDiameter of the wheel in inches.
# If you’re curious about how the above formula was derived, you can read the tire volume formula derivation.

# Assignment
# Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.

#-----------------WEEK 02 ASSIGNMENT---------------#

# Problem Statement
# Many companies wish to understand the needs and wants of their customers more deeply so the company can create products that fill those needs and wants. One way to understand customers more deeply is to record the values entered by customers while they are using a program and then to analyze those values. One common way to record values is for a program to store them in a file.

# Assignment
# The previous lesson’s prove milestone required you to write a program named tire_volume.py that computes the approximate volume of air inside a tire. Add code near the end of that program that does the following:

# Gets the current date from the computer’s operating system.
# Opens a text file named volumes.txt for appending.
# Appends to the end of the volumes.txt file one line of text that contains the following five values:
#   current date
#   tireWidth of the tire
#   aspect ratio of the tire
#   tireDiameter of the wheel
#   volume of the tire

# Stretch Goal
# Find tire prices for four or more tire sizes online. Add a set of if … elif … else statements in your program that use the tire tireWidth, tire aspect ratio, and wheel tireDiameter that the user enters to find a price and then print the price.
# After your program prints the tire volume to the terminal window, your program should ask the user if she wants to buy tires with the dimensions that she entered. If the user answers “yes”, your program should ask for her phone number and store her phone number in the volumes.txt file.

#Imports
#Week 01
import math
#Week 02
import datetime

#Gets the date and time (Week 02 Assignment)
currentDateAndTime = datetime.datetime.now()


#Promt user question for math (Week 01)
print("You will be given 3 variables to enter to help calculate the volume of your tire. Please answer the following questions: ")
tireWidth = int(input("Enter the width of the tire in mm: "))
aspectRatio = int(input("Enter the aspect ratio of the tire: "))
tireDiameter = int(input("Enter the diameter of the wheel in inches: "))

#Calculate the volume based on the numbers given by the user (Week 01)
volume = round((math.pi*pow(tireWidth, 2)*aspectRatio*(tireWidth*aspectRatio+2540*tireDiameter))/10000000000,2)



# print out the volume for the current user request (Week 01)
print(f"The aproxomate volume is {volume} liters")

#Formatting (Week 02 Assignment/Stretch)
print()

#Set phone number to 0, so we can only save to the file if there is data entered through an if (Week 02 Stretch)
phoneNumber = 0

#Prompting the user to see if they want new tires (Week 02 Stretch)
purchase = input("Are you interested in buying a new set of tires? (Y or N): ")
#Checking for the answer of the purchase input, continueing on if yes. No point otherwise (Week 02 Stretch)
if purchase == "y" or purchase == "Y" or purchase == "YES" or purchase == "Yes" or purchase == "yes" :
    #Creating price and setting to float (Week 02 Stretch)
    price = float(0)
    
    #Merge the data entered into a string (Week 02 Stretch)
    requestedTire = f"{tireWidth}/{aspectRatio}/{tireDiameter}"
    #185/50/14 tire pricing
    tireOne = "185/50/14"
    tireOnePrice = 245.97
    #205/60/15 tire pricing (Week 02 Stretch)
    tireTwo = "205/60/15"
    tireTwoPrice = 315.97
    #205/75/17 tire pricing (Week 02 Stretch)
    tireThree = "205/75/17"
    tireThreePrice= 373.26
    #85/50/14 tire pricing (Week 02 Stretch)
    tireFour = "85/50/14"
    tireFourPrice = 213.97

    #Declaring set of tires so we can use for if statements (Week 02 Stretch)
    setOfTires = int(0)

    #formatting (Week 02 Stretch)
    print()
    #Checking the entered data against the 4 tires entered here (Week 02 Stretch)
    if requestedTire == tireOne :
        print(f"The price of a single tire is ${tireOnePrice}")
        setOfTires = tireOnePrice * 4
        print(f"The price of 4 tires is: ${setOfTires}")
    elif requestedTire == tireTwo:
        print(f"The price of a single tire is ${tireTwoPrice}")
        setOfTires = tireTwoPrice * 4
        print(f"The price of 4 tires is: ${setOfTires}")
    elif requestedTire == tireThree:
        print(f"The price of a single tire is ${tireTwoPrice}")
        setOfTires = tireTwoPrice * 4
        print(f"The price of 4 tires is: ${setOfTires}")
    elif requestedTire == tireFour:
        print(f"The price of a single tire is ${tireTwoPrice}")
        setOfTires = tireTwoPrice * 4
        print(f"The price of 4 tires is: ${setOfTires}")
    #If there is nothing there, let the user know we dont have the price (Week 02 Stretch)
    else:
        print(f"We dont have the price for your tires ({requestedTire}) on demand")

    #Check to see if we know the price for the set of tires. Not outputting the text again as its  just above (Week 02 Stretch)
    if setOfTires == 0:
        #formattting (Week 02 Stretch)
        print()
        #Output the text asking for phone number if we need to give a quote (Week 02 Stretch)
        phoneNumber = input("Please enter your phone number (including area code) and our sales team will return your call with a quote shortly: ")
    #Let the user we know we will call them shortly to purchase (Week 02 Stretch)
    else:
        #formattting (Week 02 Stretch)
        print()
        #Output the text asking for phone number if we will return their call for a purchase (Week 02 Stretch)
        phoneNumber = input("Please enter your phone number (including area code) and our sales team will return your call to setup a purchase shortly: ")

#Output the information to the files (Week 02 Assignment)
try:
    with open("C:/Users/gidgi/Documents/Tristin's School/[CSE 111] Programming With Functions/Git/CSE-111/volumes.txt", mode="at") as volumes_file:
        #add blank line between this and next entry (Week 02 Assignment)
        print("",file = volumes_file)
        print(f"Current Date: {currentDateAndTime:%Y-%m-%d}", file = volumes_file)
        print(f"Width of the tire: {tireWidth}", file = volumes_file)
        print(f"Aspect ratio of the tire: {aspectRatio}", file = volumes_file)
        print(f"Diameter of the wheel: {tireDiameter}", file = volumes_file)
        print(f"Volume of the tire: {volume}", file = volumes_file)
        if phoneNumber != 0 :
             print(f"Phone number: {phoneNumber}", file = volumes_file)
        
except Exception as e:
        print(f"An error occurred: {e}") 