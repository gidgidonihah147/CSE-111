#-----------------WEEK 09 ASSIGNMENT---------------#
# Problem Statement
# A local grocery store subscribes to an online service that enables its customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.

# Assignment
# During this milestone, you will write half of a Python program named receipt.py that prints to the terminal window a receipt for a customer’s grocery order. Specifically, by the end of this milestone, your program must contain at least these two functions:

# main
# read_dictionary
# and must read and process these two CSV files:

# The products.csv file is a catalog of all the products that the grocery store sells.
# The request.csv file contains the items ordered by a customer.

#-----------------Week 09 - Step 1---------------#
# Download both of these files: products.csv and request.csv and save them in the same folder where you will save your Python program.

#-----------------Week 09 - Step 2---------------#
# Open the products.csv file in VS Code and examine it. Notice that each row in this file contains three values separated by commas: a product number, a product name, and a retail price. Also, notice that each product number in the products.csv file is unique. This means that your program can read the products.csv file into a dictionary and use the product numbers as keys in the dictionary.

#-----------------Week 09 - Step 3---------------#
# In VS Code, create a new file and save it as receipt.py in the same folder where you saved the products.csv and request.csv files.

#-----------------Week 09 - Step 4---------------#
# In receipt.py, write a function named read_dictionary that will open a CSV file for reading and use a csv.reader to read each row and populate a compound dictionary with the contents of the products.csv file. The read_dictionary function must have this header and documentation string:

# def read_dictionary(filename, key_column_index):
#     """Read the contents of a CSV file into a compound
#     dictionary and return the dictionary.

#     Parameters
#         filename: the name of the CSV file to read.
#         key_column_index: the index of the column
#             to use as the keys in the dictionary.
#     Return: a compound dictionary that contains
#         the contents of the CSV file.
#     """
# Recall that each item in a dictionary has a key and a value. Each item in the products dictionary must have a product number as the key and a list with the product number, product name, and price as the value as shown in the following table.

# Products
# Key	Value
# "D150"	["D150", "1 gallon milk", 2.85]
# "D083"	["D083", "1 cup yogurt", 0.75]
# "D215"	["D215", "1 lb cheddar cheese", 3.35]
# "P019"	["P019", "iceberg lettuce", 1.15]
# "P020"	["P020", "green leaf lettuce", 1.79]
# "P021"	["P021", "butterhead lettuce", 1.83]
# "P025"	["P025", "8 oz arugula", 2.19]
# "P143"	["P143", "1 lb baby carrots", 1.39]
# "W231"	["W231", "32 oz granola", 3.21]
# "W112"	["W112", "wheat bread", 2.55]
# "C013"	["C013", "twix candy bar", 0.85]
# "H001"	["H001", "8 rolls toilet tissue", 6.45]
# "H014"	["H014", "facial tissue", 2.49]
# "H020"	["H020", "aluminum foil", 2.39]
# "H021"	["H021", "12 oz dish soap", 3.19]
# "H025"	["H025", "toilet cleaner", 4.50]

#-----------------WEEK 10 ASSIGNMENT---------------#
# Problem Statement§
# A local grocery store subscribes to an online service that enables its customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.

# Assignment
# During the prove milestone for the previous lesson, you wrote the part of this program that reads and processes two CSV files, one named products.csv that contains a catalog of products and one named request.csv that contains a customer’s order. During this prove assignment, you will add code to finish printing a receipt and to handle any exceptions that might occur while your program is running. Specifically, your program must do the following:

# Print the store name at the top of the receipt.
# Print the list of ordered items.
# Sum and print the number of ordered items.
# Sum and print the subtotal due.
# Compute and print the sales tax amount. Use 6% as the sales tax rate.
# Compute and print the total amount due.
# Print a thank you message.
# Get the current date and time from your computer’s operating system and print the current date and time.
# Include a try block and except blocks to handle FileNotFoundError and KeyError.

import csv
import random
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:

            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary

#-----------------Week 09 - Step 5---------------#
# Open the request.csv file in VS Code and examine it. Notice that each row contains only two values, a product number and a quantity. Notice also that product number D083 appears twice in the file. It appears twice because the customer who created the order in the request.csv file added four yogurts to his order and then later added three more yogurts to his order. Because product numbers may appear multiple times in the request.csv file, your program must not read the contents of request.csv into a dictionary.

#-----------------Week 09 - Step 6---------------#
# In your receipt.py program, write another function named main that does the following:
# Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
# Prints the products_dict.
# Opens the request.csv file for reading.
# Skips the first line of the request.csv file because the first line contains column headings.
# Uses a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
# Use the requested product number to find the corresponding item in the products_dict.
# Print the product name, requested quantity, and product price.
# Because product number D083 appears twice in the request.csv file, your program must not read the request.csv file into a dictionary. Recall that each key in a dictionary is unique. If your program reads the request.csv file into a dictionary, when your program reads line 3 of the request.csv file, your program will put a request for four yogurts into the dictionary. Then when your program reads line 6 of the request.csv file, your program will replace the request for four yogurts with a request for three yogurts. In other words, if your program reads the request.csv file into a dictionary, your program will think that the customer ordered only three yogurts instead of the seven (4 + 3) that he ordered. Therefore, your program must not read the request.csv file into a dictionary but should instead read and process each row similar to example 3 in the preparation content for this lesson.
def main():
    try:
        products_dict = read_dictionary("products.csv", 0)
        if products_dict is None:
            return  # Exit if there was an error reading the file

        print("\nMy Store!\n")  # Print the store name

        # Open the request.csv file for reading.
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next (reader)


            total_items = 0
            subtotal = 0

            print("Requested Items")
            for row_list in reader:
                product_number = row_list[0]
                quantity = int(row_list[1])

                # Use the requested product number to find the corresponding item in the products_dict.
                if product_number in products_dict:
                    product = products_dict[product_number]
                    product_name = product[1]
                    product_price = float(product[2])


                    # Calculate item total and add to subtotal
                    item_total = quantity * product_price
                    subtotal += item_total

                    # Print the product name, requested quantity, and product price.
                    print(f"{product_name}: {quantity} @ ${product_price:.2f} = ${item_total:.2f}")

                    total_items += quantity
                else:
                    print(f"Error: Product number '{product_number}' not found in products.csv.")

            # Calculate sales tax and total
            sales_tax_rate = 0.06
            sales_tax = subtotal * sales_tax_rate
            total = subtotal + sales_tax

            # Print the receipt summary
            print(f"\nNumber of Items: {total_items}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${sales_tax:.2f}")
            print(f"Total: ${total:.2f}")

            # Print a thank you message and current date and time
            current_date_and_time = datetime.now()
            print("\nThank you for shopping at my store!")
            print(f"{current_date_and_time:%a %b %e %H:%M:%S %Y}")

                        # --- Stretch Goals ---

            # Survey invitation
            print("\nComplete our online survey and receive 10% off your next purchase:")
            print("https://www.mystore.com/survey")

            # Coupon for a random ordered item
            with open("request.csv", "rt") as request_file:
                reader = csv.reader(request_file)
                next(reader)
                ordered_items = list(reader)
            random_item = random.choice(ordered_items)
            print("\nCoupon for your next purchase:")
            print(f"Product: {random_item[0]}")
            print("Discount: 15% off")

            # Return by date (7 days from now)
            return_by_date = current_date_and_time + timedelta(days=7)
            print(f"\nReturn by date: {return_by_date:%a %b %e %H:%M:%S %Y}")

            # Days until New Year's Sale
            new_years_day = datetime(current_date_and_time.year + 1, 1, 1)
            days_until_new_years = (new_years_day - current_date_and_time).days
            print(f"\nDays until New Year's Sale: {days_until_new_years}")

            # Discount on Tuesdays and Wednesdays
            if current_date_and_time.weekday() in [1, 2]:  # 1 is Tuesday, 2 is Wednesday
                discount = 0.10  # 10% discount
                print("\nSpecial discount applied: 10%")
            # Discount before 11:00 a.m.
            elif current_date_and_time.hour < 11:
                discount = 0.10  # 10% discount
                print("\nMorning discount applied: 10%")

    except KeyError as e:
        print(f"Error: Invalid key '{e}' in dictionary lookup.")

#-----------------Week 09 - Step 7---------------#
# At the bottom of your receipt.py file, add a call to the main function. Be certain to protect the call to main with an if statement as taught in the preparation content for lesson 5.
if __name__ == "__main__":
    main()