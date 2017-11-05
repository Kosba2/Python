#! /usr/bin/python
# Exercise No.   3
# File Name:     hw3project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          September 10, 2017
#
# Problem Statement: Takes two whole number integers and creates a quotient of the two,
# also returns the remainder.
#
#
# Overall Plan:
# 1. Introduces the function of the program
# 2. Prompt the user for an input of a dividend and a divisor
# 3. Calculate, using whole numbers (rounded if not), the quotient and remainder
# 4. Output the Quotient and Remainder
#
#
# import the necessary python libraries


def main():
    print("This program computes the quotient and remainder of a division operation")
    print("NON-INTEGER VALUES WILL BE ROUNDED, THIS IS A DESIGN DECISION")

    # \n is the new line character
    dividend = eval(input("\nWhat number do you wish to divide? "))
    divisor = eval(input("\nHow much do you wish to divide by? "))

    dividend = int(round(dividend))
    divisor = int(round(divisor))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print("\nThe Division of", dividend, "by", divisor, "results in", quotient, "R",
          remainder)


main()
