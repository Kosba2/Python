#! /usr/bin/python
# Exercise No.   2
# File Name:     hw2project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          August 28, 2017
#
# Problem Statement: A program to convert Celsius temperatures to Fahrenheit
#
#
# Overall Plan:
# 1. Introduces the program where Celsius is converted to Fahrenheit
# 2. Prompt for an input of Celsius temperature
# 3. Calculate Fahrenheit temperature
# 4. Print out Fahrenheit temperature
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("Hello!")
    print("The purpose of this program is to convert a given Celsius Temperature")
    print("into Fahrenheit.")

    celsius = eval(input("What is the Celsius temperature? "))
    print()

    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

