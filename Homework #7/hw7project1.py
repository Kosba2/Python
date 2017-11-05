#! /usr/bin/python
# Homework No.7  Exercise No.1
# File Name:     hw7project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 8, 2017
#
# Problem Statement: Error Checks invalid Inputs for a Grade and returns Letter Grade
#
#
# Overall Plan:
# 1. Create a Function that determines Letter grade based on percentage grade
# 2. Uses Try Catch block to error check user Input, no specific exception, just scolds
#    the user for non-numerical inputs
# 3. Scolds the user anyways for getting bad grades
#
# import the necessary python libraries


def getLetterGrade(decimalGrade):
    if decimalGrade > 100:
        print("Grade Greater than 100%! ERRRRORRR")
    elif decimalGrade >= 90:
        print("Your grade is an A! So Smaht!")
    elif decimalGrade >= 80:
        print("Your grade is a B! Perty Smaht!")
    elif decimalGrade >= 70:
        print("Your grade is a C! Keep trying almost there!")
    elif decimalGrade >= 60:
        print("Your grade is a D! You could use practice...")
    elif decimalGrade >= 0:
        print("Your grade is an F. We need to talk.")
    else:
        print("How are you so bad")


def main():
    validInput = False

    # Prompts for the user to enter a grade
    while not validInput:
        try:
            decimalGrade = eval(input("Please enter your numeric Grade: "))
            getLetterGrade(decimalGrade)
            validInput = True
        except:
            print("\nYou entered an invalid value!")


main()
