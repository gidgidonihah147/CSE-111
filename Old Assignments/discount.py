# Purpose§
# Improve your understanding of calling built-in Python functions and calling functions and methods that are in a standard Python module.

# Problem Statement
# You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.

# Assignment
# Work as a team to write a Python program named discount.py that gets a customer’s subtotal as input and gets the current day of the week from your computer’s operating system. Your program must not ask the user to enter the day of the week. Instead, it must get the day of the week from your computer’s operating system.

# If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

# Core Requirements
# Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your computer’s operating system.
# Your program correctly computes and prints the discount amount if applicable.
# Your program correctly computes and prints the sales tax amount and the total amount due.
# Stretch Challenges
# If your team finishes the core requirements in less than an hour, complete one or more of these stretch challenges. Note that the stretch challenges are optional.

# Add code to your program that the computer will execute if today is Tuesday or Wednesday and the customer is not purchasing enough to receive the discount. This added code should compute and print the difference between $50 and the subtotal which is the additional amount the customer would need to purchase in order to receive the discount.
# Near the beginning of your program replace the code that asks the user for the subtotal with a loop that repeatedly asks the user for a price and a quantity and computes the subtotal. This loop should repeat until the user enters "0" for the price.
#Imports to make things simpler
import math
import datetime

subtotal = 0

print("Enter the price and quantity for each item. Enter a 0 to get the totals")
price = 1
while price != 0:
    price = float(input("Please enter the price: "))
    if price != 0:
        quantity = int(input("Please enter the quantity: "))
        subtotal += price * quantity

subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal:.2f}")
print()

#Determining the day of the week it is to see if it needs a discount
current_date_and_time = datetime.datetime.now()
day_of_week = current_date_and_time.weekday()

#Input of the subtotal, and calculation of the tax and total amount
#retailAmount = float(input("Please enter the subtotal: $"))
retailAmount = subtotal
salesTax = round(float(retailAmount*0.06),2)
total = round(float(salesTax+retailAmount),2)

#Discount calculations
discountRetail = round(retailAmount*.9,2)
discountedSalesTax = round(float(discountRetail*0.06),2)
discountAmount = round(retailAmount*.1,2)
discountTotal = round(float(discountedSalesTax + discountRetail),2)

discountAllowed = int(50)

#Determin the amount that is needed until they would get the discount. Nothing more is needed because we are already checking to see if the total is greater than the discount
amountTillDiscount = discountAllowed - retailAmount


#To see if the day of the week is Tuesday or Wednesday
if day_of_week == 1 or day_of_week == 2: 
    #Determine if the discount is to be given
    if retailAmount >= discountAllowed: 
        #output the discounted texts
        print(f"Discount amount: ${discountAmount}")
        print(f"Sales tax amount: ${discountedSalesTax}")
        print(f"Total: ${discountTotal}")
    else: 
        #output the regular amounts
        print(f"In order to get the a 10% discount, you would need to add ${amountTillDiscount}")
        print(f"Sales tax amount: ${salesTax}")
        print(f"Total: ${total}")
else:
    print(f"Sales tax amount: ${salesTax}")
    print(f"Total: ${total}")

