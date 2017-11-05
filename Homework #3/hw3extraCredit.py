#! /usr/bin/python
# Homework No.3  Exercise No.4
# File Name:     hw3extraCredit.py
# Programmer:    Kostyantyn Shumishyn
# Date:          September 10, 2017
#
# Problem Statement: Calculate the Gregorian Epact in order to save Easter!
#
#
# Overall Plan:
# 1. Introduces the function of the program
# 2. Prompt for the current 4-digit year
# 3. Use the year to get the Century
# 4. Use the century in conjunction with the year to calculated the epact
# 5. Output what the epact for that year is.
#
# import the necessary python libraries


def main():
    print("This program will save Easter by calculating the Gregorian Epact!")

    # \n is the new line character
    year = eval(input("\nWhat 4-Digit year is it? "))

    # Calculates century
    century = year // 100

    # Calculates epact
    epact = int(8 + (century // 4) - century + (((8 * century) + 13) // 25) + 11*(year % 19)) % 30

    # Output
    print("\nIn the year", year, "the Gregorian Epact is", epact)


main()
