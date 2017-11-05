#! /usr/bin/python
# Exercise No.   1
# File Name:     MyFirstProgram.py
# Programmer:    Kostyantyn Shumishyn
# Date:          August 21, 2017
#
# Problem Statement: Ask the user to enter two numbers, calculate the sum of 
# these two numbers, and display the sum to the screen
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for three integers
# 3. Calculate the sum of the integers
# 4. Calculate the product of the integers
# 4. Print the sum & product of the integers to the screen
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("Hello!")
    print("I can add and multiple three number for you")

    # Variables are declared dynamically no need to pre-define
    print("Enter one whole numbers(Ex. 52):")
    num1 = eval(input())
    print("Enter another whole numbers(Ex. 41):")
    num2 = eval(input())
    print("Enter a third whole number please(Ex. 28):")
    num3 = eval(input())

    percentage = (num1 / num2 ) * 100
    print("Percentage = ", percentage)

    #Here is the processing that is needed
    summation = num1 + num2 + num3
    product = num1 * num2 * num3

    # Output the results
    print("The sum of the three numbers is", summation)
    print("The product of the three numbers is", product)


main()

