#! /usr/bin/python
# Homework No.6  Exercise No.1
# File Name:     hw6project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 1, 2017
#
# Problem Statement: Create functions that returns Surface Area and Volume of a Sphere
#
#
# Overall Plan:
# 1. Creates Functions for Volume and Surface Area
# 2. Prompts for Radius
# 3. Uses Radius with Functions to find Volume and Surface Area
# 4. Returns information to user
#
# import the necessary python libraries
import math


def sphereSurfaceArea(radius):
    pi = math.pi
    surfaceArea = 4 * pi * (radius ** 2)
    return surfaceArea


def sphereVolume(radius):
    pi = math.pi
    volume = 4 / 3 * pi * (radius ** 3)
    return volume


def main():
    # Prompts for the user to enter a radius
    radius = eval(input("Please enter the radius of your sphere!\n"))
    print("\nYour Surface area is " + str(round(sphereSurfaceArea(radius), 2)))
    print("\nYour Volume is " + str(round(sphereVolume(radius), 2)))


main()
