#! /usr/bin/python
# Homework No.MIDTERM  Exercise No.3
# File Name:     midtermProject3.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 15, 2017
#
# Problem Statement: Creates a connect the dot game where each point has a number and
# connects to the next point. SEE COMMENT ABOVE MAIN!
#
#
# Overall Plan:
# 1. Creates a list pre-emptively
# 2. While the list is less than the max amount of dots, keep looping
# 3. Each loop, click to get a point, store point into array for counting
# 4. Each loop, draw a circle at the point and draw a line to the previous point but only
#    when there IS a previous point to connect to.
#
# import the necessary python libraries
from graphics import *


##########################################################################################
# THE INSTRUCTIONS DIDN'T SPECIFY WHETHER THE LINES SHOULD CONNECT, BUT ALSO DIDN'T      #
# SPECIFY THAT THEY SHOULDN'T CONNECT. LONG STORY SHORT, THEY WERE VERY AMBIGUOUS. SO I  #
# MADE THEM CONNECT EVEN THOUGH IT DIDN'T SAY TO, CAUSE WELL, BETTER SHOW THAT I CAN DO  #
# SOMETHING THAN NOT I SUPPOSE? HONESTLY THE INSTRUCTIONS SEEMED WAY TOO EASY SO IF I    #
# DID OR DIDN'T DO SOMETHING, IT'S NOT THAT I COULDN'T, WASN'T SURE WHAT ELSE TO DO.     #
##########################################################################################
def main():
    # Defines a Window
    win = GraphWin("My First Program!", 600, 600)

    listClicks = []
    maxDots = 100;

    while len(listClicks) < maxDots:
        # Creates a Temporary Point for ease of reference
        tempPoint = win.getMouse()

        # Stores Point into List to use as counter
        listClicks.append(tempPoint)

        # Draws a Point for Connect the Dot
        dot = Circle(tempPoint, 3)
        dot.setFill("cyan")
        dot.setOutline("black")
        dot.draw(win)

        # Draws the Sequence Number
        midpointText = Text(tempPoint, len(listClicks))
        midpointText.draw(win)

        # Draws a Line Between Dots
        if len(listClicks) > 1:
            lineSegment = Line(previousPoint, tempPoint)
            lineSegment.draw(win)

        # Stores the Previous Point for next line's usage
        previousPoint = tempPoint

    # Waits for mouse click before closing program
    win.getMouse()
    win.close()


main()
