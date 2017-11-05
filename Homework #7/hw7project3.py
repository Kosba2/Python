#! /usr/bin/python
# Homework No.7  Exercise No.3
# File Name:     hw7project3.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 8, 2017
#
# Problem Statement: Lightly Error Checks Values, bit silly code, determines fine if the
# speed is in violation of speed limit, otherwise fluff messages
#
#
# Overall Plan:
# 1. Create a Function that determines whether speed limit was breached
# 2. Uses Try Catch block to error check user Input for non-numeric input
# 3. Uses function to determine if speeding or not
# 4. Uses secondary function to determine fine if speeding and scolds
#
# import the necessary python libraries


def checkSpeed(clockedSpeed, speedLimit):
    if clockedSpeed < 0:
        print("Please don't drive backwards...")
    elif clockedSpeed == 0:
        print("Don't stop, that's dangerous!")
    elif clockedSpeed <= speedLimit:
        print("Well done law abiding citizen!")
    else:
        print("BUSTED! Your fine is: $" + str(
            calculateSpeedingFine(clockedSpeed, speedLimit)))


def calculateSpeedingFine(clockedSpeed, speedLimit):
    FLAT_RATE = 50
    PENALTY_FEE = 200;
    SPEED_PENALTY_RATE = 5;

    overLimit = clockedSpeed - speedLimit
    amountDue = FLAT_RATE + (overLimit * SPEED_PENALTY_RATE)

    if clockedSpeed > 90:
        amountDue += PENALTY_FEE

    return round(amountDue, 2)


def main():
    validInput = False

    # Prompts for the user to enter a grade
    while not validInput:
        try:
            speedLimit = eval(input("Please enter the speed limit: "))
            clockedSpeed = eval(input("Please enter your clocked speed: "))
            validInput = True
        except:
            print("\n\nYou entered an invalid speed!\n")

    checkSpeed(clockedSpeed, speedLimit)


main()
