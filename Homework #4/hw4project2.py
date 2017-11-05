#! /usr/bin/python
# Homework No.4  Exercise No.2
# File Name:     hw4project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          September 17, 2017
#
# Problem Statement: Draws a bunch of shapes to experiment with graphics
#
#
# Overall Plan:
# 1. Creates Entry Boxes with Instructions
# 2. Waits for Mouse Click to Calculate the Sum/Product of numbers
# 3. Evaluates value of Entry boxes' values then calculates Sum/Product
# 4. Creates Text boxes with correct answers as text.
#
# import the necessary python libraries
from graphics import *


def main():
    # Defines a Window
    win = GraphWin("My First Program!", 600, 400)

    # Draws Interface
    Text(Point(135, 30), "Please Enter First Number").draw(win)
    Text(Point(148, 100), "Please Enter Second Number").draw(win)
    Text(Point(135, 170), "Please Enter Third Number").draw(win)

    # Boxes to Type into
    firstNumberBox = Entry(Point(130, 55), 20)
    secondNumberBox = Entry(Point(130, 125), 20)
    thirdNumberBox = Entry(Point(130, 195), 20)

    # Draws Entry Boxes
    firstNumberBox.draw(win)
    secondNumberBox.draw(win)
    thirdNumberBox.draw(win)

    # Preps Output Boxes
    outputSummation = Text(Point(105, 300), "Sum of Numbers = ")
    outputProduct = Text(Point(118, 350), "Product of Numbers = ")
    outputSummation.draw(win)
    outputProduct.draw(win)

    # Preps Button
    button = Text(Point(200, 250), "CALCULATE")
    button.draw(win)

    # Waits for CALCULATE click
    win.getMouse()
    summation = eval(firstNumberBox.getText()) + eval(secondNumberBox.getText()) + eval(thirdNumberBox.getText())
    product = eval(firstNumberBox.getText()) * eval(secondNumberBox.getText()) * eval(thirdNumberBox.getText())

    # Prints Results
    sumAnswer = Text(Point(300, 300), summation)
    productAnswer = Text(Point(300, 350), product)
    sumAnswer.draw(win)
    productAnswer.draw(win)

    # Waits for mouse click before closing program
    win.getMouse()
    win.close()


main()
