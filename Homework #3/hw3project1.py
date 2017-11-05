#! /usr/bin/python
# Exercise No.   3
# File Name:     hw3project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          September 10, 2017
#
# Problem Statement: Calculate cost per square inch of a circular pizza.
#
#
# Overall Plan:
# 1. Introduces the function of the program
# 2. Prompt the user for the diameter and the price of the pizza
# 3. Find the area of the Pizza using the pi constant
# 4. Divide the Price of the Pizza by its Area to get cost per square inch
# 5. Output the cost per square inch
#
#
# import the necessary python libraries
import math


def main():
    print("This program computes the cost per square inch of your Pizza")

    # \n is the new line character
    diameterPizza = eval(input("\nWhat's the diameter in inches of your pizza? "))
    pricePizza = eval(input("\nHow much did that pizza cost you? "))

    radiusPizza = diameterPizza / 2
    pi = math.pi

    # foo**n is foo to the n power
    areaPizza = pi * (radiusPizza ** 2)

    costPerSquareInch = pricePizza / areaPizza

    print("\nCost of the Pizza is $", round(costPerSquareInch, 2), "per square inch.")


main()
