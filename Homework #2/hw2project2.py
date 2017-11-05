#! /usr/bin/python
# Exercise No.   2
# File Name:     hw2project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          August 28, 2017
#
# Problem Statement: A program to convert Fahrenheit temperatures to Celsius
#
#
# Overall Plan:
# 1. Introduces the program where Fahrenheit is converted to Celsius
# 2. Prompt for an input of Fahrenheit temperature
# 3. Calculate Celsius temperature
# 4. Print out Celsius temperature
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("Hello!")
    print("The purpose of this program is to convert a given Fahrenheit Temperature")
    print("into Celsius.")

    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    print()

    celsius = 5*(fahrenheit - 32)/9
    print("The temperature is", celsius, "degrees celsius.")

main()

