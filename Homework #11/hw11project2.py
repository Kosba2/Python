#! /usr/bin/python
# Homework No.11  Exercise No.2
# File Name:     hw11project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          November 12, 2017
#
# Problem Statement: Uses a dictionary to fetch the correct card image to display for the
# user.
#
# Overall Plan:
# 1. Keep list of suit images
# 2. Create Canvas
# 3. Make UI Elements
# 4. Depending on Text draw image, else complains
# 5. Exits when Quit button is pressed
#
# import the necessary python libraries
from graphics import *
from button import Button


def main():
    # Reads in images to List
    suitList = ["club.ppm", "spade.ppm", "heart.ppm", "diamond.ppm"]

    # Defines a Window
    win = GraphWin("Child Height Calculator", 600, 400)
    win.setBackground("darkgreen")

    # Draw the Instructions
    instructionSuit = Text(Point(100, 40), "Please enter Suit: ")
    instructionSuit.draw(win)

    # Draw the Entry Boxes
    entrySuit = Entry(Point(100, 70), 8)
    entrySuit.draw(win)

    # Makes Process Button
    processButton = Button(win, Point(100, 220), 80, 20, "Draw")
    processButton.activate()

    # Makes Quit Button
    quitButton = Button(win, Point(100, 290), 80, 20, "Quit")
    quitButton.activate()

    # Primary Loop
    while not quitButton.clicked(win.getMouse()):
        try:
            if processButton.clicked(win.getMouse()):
                suit = entrySuit.getText().lower()

                # Draws outline of the card
                cardOutline = Rectangle(Point(230, 50), Point(440, 360))
                cardOutline.setFill("white")
                cardOutline.draw(win)

                if suit.startswith("club"):
                    # Draw Club
                    tempImage = Image(Point(332, 200), suitList[0])

                elif suit.startswith("spade"):
                    # Draw Spade
                    tempImage = Image(Point(332, 200), suitList[1])

                elif suit.startswith("heart"):
                    # Draw Heart
                    tempImage = Image(Point(332, 200), suitList[2])

                elif suit.startswith("diamond"):
                    # Draw Diamond
                    tempImage = Image(Point(332, 200), suitList[3])

                tempImage.draw(win)

        except:
            print("Please Enter valid Suit Name!")


main()
