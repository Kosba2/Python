# Homework No.13  Exercise No.3
# File Name:     hw13project3.py
# Programmer:    Kostyantyn Shumishyn
# Date:          November 26, 2017
#
# Problem Statement: Creates a Recursive Base Conversion Algorithm
#
#
# Overall Plan:
# 1. Create a Function to convert a number to a different base
# 2. Prompts user for Base and Number
# 3. Returns the base converted number


def baseConversion(num, base):
    remainder = num % base
    # Base Case
    if num <= 1:
        return str(num)
    # Recursive Case
    else:
        return str(baseConversion(num // base, base)) + str(remainder)


def main():
    # Prompts user for Number and Base
    number = eval(input("What number do you wish to convert? : "))
    base = eval(input("What base do you wish to convert to? : "))

    # Prints the number in new base
    print(str(number) + " is " + baseConversion(number, base) + " in base " + str(base))


main()
