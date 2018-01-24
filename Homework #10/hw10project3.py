#! /usr/bin/python
# Homework No.10  Exercise No.1
# File Name:     hw10project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          November 10, 2017
#
# Problem Statement: Error Checks input for a child's gender and height w/ GUI
#
# Overall Plan:
# 1. Create a Function that uses Gender to determine which formula to use, then passes
#    along the height of Mother and Father to the correct functions
# 2. Error Checks EVERYTHING
# 3. Prints Height of Child in Inches and in Feet & Inches
# 4. Uses the newly created Button class to create buttons for new GUI
#
# import the necessary python libraries
from graphics import *
from button import Button
from cbutton import CButton


##
# Inexplicably, the program takes several clicks to calculate, Python issue?
##

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
    # Defines a Window
    win = GraphWin("Child Height Calculator", 600, 400)
    win.setBackground("darkgreen")

    # Draw the Instructions
    instruction = Text(Point(285, 100), "Please enter (in inches): ")
    instructionA = Text(Point(160, 140), "Mother's Height")
    instructionB = Text(Point(400, 140), "Father's Height")
    # Enable Instructions
    instruction.draw(win)
    instructionA.draw(win)
    instructionB.draw(win)

    # Draw the Entry Boxes
    motherEntry = Entry(Point(165, 170), 8)
    fatherEntry = Entry(Point(405, 170), 8)
    # Enables the Entry Boxes
    motherEntry.draw(win)
    fatherEntry.draw(win)

    # Draws the Buttons
    maleCalculateButton = Button(win, Point(165, 200), 160, 20, "Male Calculate")
    maleCalculateButton.activate()
    femaleCalculateButton = Button(win, Point(405, 200), 160, 20, "Female Calculate")
    femaleCalculateButton.activate()
    quitButton = CButton(win, Point(300, 330), 30, "Quit")
    quitButton.activate()

    # Draws the Output Box
    outputBoxA = Text(Point(300, 230), "Child Height (in): ")
    outputBoxB = Text(Point(300, 260), "Child Height (ft): ")
    # Enables the Output Box
    outputBoxA.draw(win)
    outputBoxB.draw(win)

    while not quitButton.clicked(win.getMouse()):
        try:
            if maleCalculateButton.clicked(win.getMouse()):
                temp = chooseHeightCalculation("male", int(motherEntry.getText()),
                                               int(fatherEntry.getText()))
                outputBoxA.setText("Child Height (in): " + str(round(temp, 2)))
                outputBoxB.setText("Child Height (ft): " + str(round(temp / 12, 2)))

            elif femaleCalculateButton.clicked(win.getMouse()):
                temp = chooseHeightCalculation("female", int(motherEntry.getText()),
                                               int(fatherEntry.getText()))
                outputBoxA.setText("Child Height (in): " + str(round(temp, 2)))
                outputBoxB.setText("Child Height (ft): " + str(round(temp / 12, 2)))


        except:
            print("Please Enter Numbers into Data before Proceeding")


main()
