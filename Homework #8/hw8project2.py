#! /usr/bin/python
# Homework No.8  Exercise No.2
# File Name:     hw8project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 22, 2017
#
# Problem Statement: Takes in a GIF or PPM and converts to gray scale
#
# import the necessary python libraries
from graphics import *

def main():

    # Takes in Input of a File Name
    infileName = input("File name: ")

    # Creates Window and a Centered Image
    window = GraphWin("Gray Scale Converter", 800, 600)
    tempImage = Image(Point(0, 0), infileName)
    myImage = Image(Point(tempImage.getWidth() / 2, tempImage.getHeight() / 2), infileName)
    myImage.draw(window)

    # Waits for Mouse Click before converting to gray scale
    window.getMouse()

    # Takes each pixel and turns it gray scale
    for row in range (0, myImage.getHeight()):
        for column in range(0, myImage.getWidth()):
            r, g, b = myImage.getPixel(column, row)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            myImage.setPixel(column, row, color_rgb(brightness, brightness, brightness))
            window.update()

    # Prompts for Save Name
    outfileName = input("Save to: ")
    myImage.save(outfileName)

    # Waits to close
    window.getMouse()
    window.close()

main()
