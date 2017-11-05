#! /usr/bin/python
# Homework No.7  Exercise No.2
# File Name:     hw7project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 8, 2017
#
# Problem Statement: Error Checks input for a child's gender and height
#
#
# Overall Plan:
# 1. Create a Function that uses Gender to determine which formula to use, then passes
#    along the height of Mother and Father to the correct functions
# 2. Error Checks EVERYTHING
# 3. Prints Height of Child in Inches and in Feet & Inches
#
# import the necessary python libraries


def chooseHeightCalculation(gender, heightMother, heightFather):
    if gender == "male" or gender == "Male" or gender == "m" or gender == "M":
        return maleChildAdultHeight(heightMother, heightFather)
    elif gender == "female" or gender == "Female" or gender == "f" or gender == "F":
        return femaleChildAdultHeight(heightMother, heightFather)
    # Returns 0 If invalid Input is provided, causing invalid Input
    else:
        return 0


def femaleChildAdultHeight(heightMother, heightFather):
    return ((heightFather * 12 / 13) + heightMother) / 2


def maleChildAdultHeight(heightMother, heightFather):
    return ((heightMother * 13 / 12) + heightFather) / 2


def main():
    validInput = False

    # Prompts for the user to enter a grade
    while not validInput:
        try:
            childGender = input("Please enter Gender of Child:\n")
            heightMother = eval(input("Please enter Height of Mother (in inches):\n"))
            heightFather = eval(input("Please enter Height of Father (in inches):\n"))
            heightOfChildInches = round(
                chooseHeightCalculation(childGender, heightMother, heightFather), 0)
            if heightOfChildInches != 0:
                validInput = True
            else:
                print("\n\nYou goofed entering Gender! Try again!\n")

        except:
            print("\nYou goofed entering Heights! Try again!")

    print("Your child will be " + str(heightOfChildInches) + " inches tall! How tall!")

    heightOfChildFeet = round(heightOfChildInches // 12, 0)
    heightOfChildInches = round(heightOfChildInches % 12, 0)

    print("\nThat's " + str(heightOfChildFeet) + " feet & " + str(
        heightOfChildInches) + " inches!")


main()
