import sys

'''
Date: 11/15/2019
Project 1: Rental Car

Script will collect rental information from customer to determine
amount due for the type and duration of the car rental.
'''

''' Determine car rental type so the amount due can be calculated. '''

# Take in string input and use to determine which information is needed to calculate amount due
# Demonstrate the use of if - else statements
rentalCode = (input("(B)udget, (D)aily, or (W)eekly rental?\n"))
rentalCode = rentalCode.upper()

if rentalCode != 'W':
    rentalPeriod = int(input("Number of Days Rented:\n"))
else:
    rentalPeriod = int(input("Number of Weeks Rented:\n"))

''' Determine base charge for the car rental. '''

# Rental Rates
# Assign numerical "Float" values to variables
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00
baseCharge = 0.00

# Use string input to determine base charge for the car rental
if rentalCode.upper() == 'B':
    baseCharge = int(rentalPeriod) * budgetCharge

if rentalCode.upper() == 'D':
    baseCharge = int(rentalPeriod) * dailyCharge

if rentalCode.upper() == 'W':
    baseCharge = int(rentalPeriod) * weeklyCharge

''' Collect mileage information for rental period. '''

# Specify that input variable is an INT variable
odoStart = int(input("Starting Odometer Reading:\n"))
odoEnd = int(input("Ending Odometer Reading:\n"))
totalMiles = odoEnd - odoStart

''' Calculate amount due for car rental. '''

# Demonstrated setting string input as a float variable rather than a string
# Demonstrated the use of if - elif - else

averageDayMiles = int(totalMiles) / float(rentalPeriod)
averageWeekMiles = int(totalMiles) / float(rentalPeriod)

if rentalCode.upper() == "B":
    mileCharge = totalMiles * 0.25
    amtDue = mileCharge + baseCharge

if rentalCode.upper() == "D" and averageDayMiles > 100:
    extraMiles = averageDayMiles - 100
    mileCharge = extraMiles * 0.25
    amtDue = mileCharge + baseCharge

if rentalCode.upper() == "D" and averageDayMiles <= 100:
    extraMiles = 0
    mileCharge = extraMiles * 0.25
    amtDue = mileCharge + baseCharge

if rentalCode.upper() == "W" and averageWeekMiles > 900:
    mileCharge = 100.00 * float(rentalPeriod)
    amtDue = mileCharge + baseCharge

if rentalCode.upper() == "W" and averageWeekMiles <= 900:
    mileCharge = 0.00
    amtDue = mileCharge + baseCharge

''' Summary string for car rental variables and total amount due. '''

# Demonstrated the use of formatting string output
print("Rental Summary")
print("Rental Code:", rentalCode.upper())
print("Rental Period:", rentalPeriod)
print("Starting Odometer:", odoStart)
print("Ending Odometer:", odoEnd)
print("Miles Driven:", totalMiles)
print("Amount Due: ${0:.2f}".format(amtDue))