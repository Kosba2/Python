#! /usr/bin/python
# Exercise No.   3
# File Name:     hw3project3.py
# Programmer:    Kostyantyn Shumishyn
# Date:          September 10, 2017
#
# Problem Statement: Given a Triangle formed by a ladder against a house, determine the
# required height of a ladder to reach a certain height of the house using a given angle
# and trigonometric identities such as sin is opposite over hypotenuse
#
#
# Overall Plan:
# 1. Introduces the function of the program
# 2. Prompt the user for the height desired to reach
# 3. Prompt the user for angle at which ladder will be placed, then convert to radians
# 4. Use trigonometric identity where sin(angle) is opposite side divided by hypotenuse
# 5. Make sure you are not dividing by 0 and angle isn't facing ladder away from house
# 6. Return result to user
#
# import the necessary python libraries
import math


def main():
    print("This program computes height of ladder required using height desired & angle")

    # \n is the new line character
    sideA = eval(input("\nHow high (in meters) up do you want ladder to reach? "))
    theta = eval(input("\nAt what angle (degrees) do you want the ladder places? "))

    pi = math.pi

    # Converts Degrees to Radians
    theta = (theta * pi) / 180

    # Makes sure you are putting the ladder against the house still
    if theta > pi:
        print("Where are you pointing that ladder?")

    # Makes sure you are not dividing by 0 by checking for instances where sin(x) = 0
    elif theta % pi != 0:
        sideC = sideA / math.sin(theta)
        print("\nThe ladder must be", round(sideC, 2), "meters tall.")

    # Calls out instances where ladder is flat on floor and useless
    else:
        print("WHY IS THE LADDER FLAT ON THE FLOOR!")


main()
