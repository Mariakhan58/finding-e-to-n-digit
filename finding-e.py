
# This program is to calculate e
# to the user's desired number of digits
# after decimal


import math

print("Note: Please enter a number between 0 and 50.")
digits = input("How many values you desire after the decimal for e? ")
value = 1

while value:

    if int(digits) > 0 and int(digits) < 50:
        print("\nThe desired value of e: %.*f" % (int(digits), math.e))
        repeat = input("Do you want to run the program again? Press y for yes or n for no. ")
        if repeat == 'y' or repeat == 'Y':
            digits = input("How many values you desire after the decimal for e? ")
        elif repeat == 'n' or repeat == 'N':
            print("\nYou chose to exit the program. Good bye.")
            value = 0
        else:
            print("\nInvalid choice. Program terminated.")
            value = 0

    else:
        print("\nNumber out of range.")
        repeat = input("Do you want to run the program again? Press y for yes or n for no. ")
        if repeat == 'y' or repeat == 'Y':
            digits = input("How many values you desire after the decimal for e? ")
        elif repeat == 'n' or repeat == 'N':
            print("\nYou chose to exit the program. Good bye.")
            value = 0
        else:
            print("\nInvalid choice. Program terminated.")
            value = 0



