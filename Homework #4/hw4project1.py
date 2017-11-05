#! /usr/bin/python
# Homework No.4  Exercise No.1
# File Name:     hw4project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          September 17, 2017
#
# Problem Statement: Draws a bunch of shapes to experiment with graphics
#
#
# Overall Plan:
# 1. Draws a bunch of points in the shape of triangle
# 2. Connects points with lines
# 3. Draws a Circle/Square/Sassy Text
# 4. Waits for mouse click to close window
#
# import the necessary python libraries
from graphics import *


def main():
    # Defines a Window
    win = GraphWin()

    # Makes 3 points in a triangular shape
    p1 = Point(50, 50)
    p2 = Point(150, 150)
    p3 = Point(50, 150)

    # Makes Lines out of 3 points, a triangle
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p1)

    # Draws the lines
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)

    # Draws a Circle
    circle = Circle(Point(80, 120), 50)
    circle.draw(win)

    # Draws a Square
    square = Rectangle(Point(10, 10), Point(70, 70))
    square.draw(win)

    # Sassy Text
    vanGogh = Text(Point(130, 40), "It's a Van Gogh")
    vanGogh.draw(win)

    # Waits for mouse click before closing program
    win.getMouse()
    win.close()


main()
