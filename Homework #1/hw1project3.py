#! /usr/bin/python
# Exercise No.   1
# File Name:     hw1project3.py
# Programmer:    Kostyantyn Shumishyn
# Date:          August 21, 2017
#
# Problem Statement: Ask the user to enter a QB's Pass Completions and
# the number of Pass Attempts and use that information to calculate
# the QB's pass completion percentage and output it for them.
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for Pass Completion
# 3. Prompt the user for Pass Attempts
# 4. Calculate the Percent Completion
# 4. Print the Percent Completion to the user
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("Hello!")
    print("I will compute completion percentage of your Quarterback!")

    # Variables are declared dynamically no need to pre-define
    print("Please enter the QB's Pass Completions : ")
    passCompletions = eval(input())
    print("Please enter the QB's Pass Attempts : ")
    passAttempts = eval(input())

    # Calculates Output
    completionPercent = (passCompletions / passAttempts ) * 100

    # Outputs desired information
    print("Completion Percentage = ", completionPercent, "%")


main()

