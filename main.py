# Programmers: Donovan Raymond & Zain
# Course:  CS 151 06
# Due Date: 10/9/24
# Lab Assignment:Lab4 Mobile Subscription Fees
# Problem Statement: Write a program to determine how much a customer owes their mobile phone provider \n
# based on their subscription package and amount of data used.

# Data In:

# Data Out:
# Credits:


def calculate_bill():
    # Step 1: Prompt user for the package type and convert to lowercase
    package = input("Enter the package type (green, blue, purple): ").lower()

    # Step 2: Validate input
    while package not in ['green', 'blue', 'purple']:
        print("That is not an option")
        package = input("Enter the package type (green, blue, purple): ").lower()

    # Step 3: Set the values for package type
    if package == 'green':
        price = 49.99
        plan_gB = 2
        rate = 15
    elif package == 'blue':
        price = 70.00
        plan_gB = 4
        rate = 10
    elif package == 'purple':
        price = 99.95

    # Step 6: If package is green or blue, prompt for used_gB
    if package in ['green', 'blue']:
        used_gB = int(input("How many GBs did you use this month? "))

    # Step 8: ask user for number of months owed
    months = int(input("How many months do you owe? "))

    # Step 9: Calculate total based the package
    if package in ['green', 'blue']:
        total = (price + max(0, (used_gB - plan_gB) * rate)) * months
    else:  # package is purple
        total = price * months

    # Step 11: Check for coupon if package is green and total is more than 75
    if package == 'green' and total >= 75:
        coupon = input("Do you have a coupon? (yes/no): ").lower()
        if coupon == 'yes':
            total -= 25
        # The 'else' case is already covered by not changing the total

    # Step 12: Print the total amount owed
    print(f'The amount of money that you owe for the {package} plan is ${total:.2f}')


# Run the function to start the program
calculate_bill()
