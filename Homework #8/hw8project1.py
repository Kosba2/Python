#! /usr/bin/python
# Homework No.8  Exercise No.1
# File Name:     hw8project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 22, 2017
#
# Problem Statement: Outputs the nth Fibonacci sequence number
#
#
# Overall Plan:
# 1. Finds the Nth Fibonacci number with error checking for incorrect input
# 2. Has the option of Iterative Solution or Recursive
# 2b.Recursive is a lot more readable, lets be honest
#
# import the necessary python libraries


# Because Overhead is fun
def fibonacciRecur(nthTerm):
    if nthTerm == 0:
        return 0
    if nthTerm == 1 or nthTerm == 2:
        return 1
    elif nthTerm > 2:
        return fibonacciRecur(nthTerm - 2) + fibonacciRecur(nthTerm - 1)


# Because why keep things simple
def fibonacciIter(nthTerm):
    resultTerm, assistTerm = 0, 1
    for i in range(0, nthTerm):
        # Just learned Tuples and their behavior is interesting
        resultTerm, assistTerm = assistTerm, resultTerm + assistTerm
    return resultTerm


def main():
    validInput = False

    # Prompts for the user to enter a valid number
    while not validInput:
        try:
            n = eval(input("Please enter which Fibonacci Term you desire: "))
            termIter = fibonacciIter(n)
            termRecur = fibonacciRecur(n)
            validInput = True
        except:
            print("\n\nYou entered a non-integer value!")

    # Prints result to user
    print("Your Recursive Fibonacci term is " + str(termRecur))
    print("Your Iterative Fibonacci term is " + str(termIter))


main()
