#! /usr/bin/python
# Homework No.4  Exercise No.3
# File Name:     hw4project3.py
# Programmer:    Kostyantyn Shumishyn
# Date:          September 17, 2017
#
# Problem Statement: Create a line with mouse clicks and display relevant info
#
#
# Overall Plan:
# 1. Prompts Instructions with text boxes
# 2. Creates and labels points, draws a line between them
# 3. Calculates Midpoint and draws a cyan circle and label there
# 4. Calculates the Slope and Length of the line
# 5. Display Slope and Length of the line to the user
#
# import the necessary python libraries
from graphics import *


def main():
    # Defines a Window
    win = GraphWin("My First Program!", 600, 400)

    # Provides Instructions
    instructions = Text(Point(240, 30), "Please Click on Two Points to draw Line Segment")
    instructions.draw(win)

    # Information
    slopeText = Text(Point(57, 60), "Slope = ")
    slopeText.draw(win)
    lengthText = Text(Point(61, 90), "Length = ")
    lengthText.draw(win)

    # Draws Line Segment
    firstPoint = win.getMouse()
    secondPoint = win.getMouse()
    lineSegment = Line(firstPoint, secondPoint)
    lineSegment.draw(win)

    # Calculations
    x1 = firstPoint.getX()
    x2 = secondPoint.getX()
    y1 = firstPoint.getY()
    y2 = secondPoint.getY()

    dx = x2 - x1
    dy = y2 - y1

    midX = (x2 + x1) / 2
    midY = (y2 + y1) / 2

    # Adjusts by Negative sign to account for Origin being NW instead of SW
    slope = -1 * (dy / dx)
    length = (dx ** 2 + dy ** 2) ** (1 / 2)

    # Draws Midpoint
    midpoint = Circle(Point(midX, midY), 3)
    midpoint.setFill("cyan")
    midpoint.setOutline("black")
    midpoint.draw(win)

    midpointText = Text(Point(midX, midY - 20), "Midpoint")
    midpointText.draw(win)

    # Draws Point Texts cause why not
    firstPointText = Text(Point(x1, y1 - 20), "P1")
    firstPointText.draw(win)

    secondPointText = Text(Point(x2, y2 - 20), "P2")
    secondPointText.draw(win)

    # Adjusts Data with numbers
    slopeAnswer = Text(Point(140, 60), round(slope, 2))
    slopeAnswer.draw(win)
    lengthAnswer = Text(Point(140, 90), round(length, 2))
    lengthAnswer.draw(win)

    # Waits for mouse click before closing program
    win.getMouse()
    win.close()


main()
