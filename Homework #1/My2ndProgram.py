#! /usr/bin/python
# Exercise No.   1
# File Name:     My2ndProgram.py
# Programmer:    Kostyantyn Shumishyn
# Date:          August 21, 2017
#
# Problem Statement: Trace a Chaos Problem from the Book and record
# the results when .15 is inputted.
#
#
# Overall Plan:
# 1. Print an initial message introducing the program
# 2. Prompt for an input between 0 and 1
# 3. Loop 10 times applying the chaos function to X and
#    store it back into X.
# 4. Prints out the values of X each loop
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Prints a Introductory Message
    print("This program illustrates a chaotic function")

    #Variable is determined with input
    x = eval(input("Enter a number between 0 and 1: "))

    #Loops 10 times storing X's new value back into itself
    #printing the value of X each repetition.
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)

main()

