#! /usr/bin/python
# Homework No.6  Exercise No.2
# File Name:     hw6project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 1, 2017
#
# Problem Statement: Creates a function that accepts a list of numbers and returns sum of
# the numbers in that list
#
#
# Overall Plan:
# 1. Creates a function for summing numbers from a list of numbers
# 2. Prompts user for numbers until they input 0
# 3. Put list through function and outputs the Sum of those numbers
#
# import the necessary python libraries


def sumLists(numList):
    sum = 0
    for numbers in numList:
        sum += numbers
    return sum


def main():
    # Prompts for the user to enter a radius
    keepGoing = True
    numberList = []

    while keepGoing:
        number = eval(input("Please enter number or enter \"0\" to stop "))

        if number == 0:
            keepGoing = False

        else:
            numberList.append(number)

    print(
        "\nThe sum of the numbers you entered is " + str(round(sumLists(numberList), 2)))


main()
