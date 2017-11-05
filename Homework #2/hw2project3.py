#! /usr/bin/python
# Exercise No.   2
# File Name:     hw2project3.py
# Programmer:    Kostyantyn Shumishyn
# Date:          August 28, 2017
#
# Problem Statement: A simple program to average two exam scores, illustrating the use of
# of multiple inputs.
#
#
# Overall Plan:
# 1. Introduces the function of the program
# 2. Prompt the user for number of scores to average
# 3. Prompt the user for each test that they have indicated will occur
# 4. Store the sum of the test scores
# 5. Divide the sum by the number of tests to get the average
# 6. Print out the Average Test Score for the user
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    print("This program computes the average of any number of test scores.")
    numTests = eval(input("How many tests do you want to average? "))

    totalScore = 0

    for i in range(0,numTests):
            print("Test #", i + 1)
            totalScore = totalScore + eval(input("Please enter Score:"))

    print("\nAverage Exam Score", totalScore/numTests)
main()

