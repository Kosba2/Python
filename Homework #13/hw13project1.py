# Homework No.13  Exercise No.1
# File Name:     hw13project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          November 26, 2017
#
# Problem Statement: Create and tests Binary and Linear Search Algorithms
#
#
# Overall Plan:
# 1. Create Helper Functions to assist the testing of each search algorithm
# 2. Create Test Function that accepts a list length and gives feedback on run times
# 3. Test run times on varying list lengths

import time
from random import *


# Linear Search Function
def linearSearch(key, numList):
    for i in range(len(numList)):
        # Key was found
        if numList[i] == key:
            return i

    # Key was not found
    return -1


# Binary Search Function
def binarySearch(key, numList):
    # Binary Variables
    low = 0
    high = len(numList) - 1

    # Continues until Low and High intersect
    while low <= high:
        # Gets Position of Middle Term
        mid = (low + high) // 2
        item = numList[mid]

        # Case: Found
        if item == key:
            return mid

        # Case: Key is Lower
        elif item > key:
            high = mid - 1

        # Case: Key is Higher
        else:
            low = mid + 1

    # End Case, never found Key
    return -1


# Creates a List of random numbers on interval of [0, ceiling]
def generateRandList(ceiling, listSize):
    # Creates List to return
    numList = []

    # Creates the correct number of terms
    for i in range(listSize):
        # Appends a random number between 0 and Ceiling
        numList.append(randint(0, ceiling))

    # Returns the list of random numbers
    return numList


# Creates a simple List of numbers
def generateList(listSize):
    # Creates List to return
    numList = []

    # Creates the correct number of terms
    for i in range(listSize):
        # Appends Linearly up to listSize
        numList.append(i)

    # Returns the list of random numbers
    return numList


def compareBinaryAndLinearSearch(lengthList):
    # Creates a list of integers between 0 & 1000000 of length lengthList
    randomNumberList = generateList(lengthList)

    # Verifies list Length
    print('List is ' + str(len(randomNumberList)) + ' numbers long')

    # Sorts List for both
    randomNumberList.sort()

    # Runs Binary Search and stores time it took to find key
    binTime = time.perf_counter()
    # Searches for a term outside the scope of the list
    binarySearch(lengthList + 1, randomNumberList)
    binTime = time.perf_counter() - binTime
    print('Binary Search took ' + str(binTime) + ' seconds.')

    # Runs Linear Search and stores time it took to find key
    linTime = time.perf_counter()
    # Searches for a term outside the scope of the list
    linearSearch(lengthList + 1, randomNumberList)
    linTime = time.perf_counter() - linTime
    print('Linear Search took ' + str(linTime) + ' seconds.')
    print()


def main():
    # Tests List of 1,000 Terms
    compareBinaryAndLinearSearch(1000)

    # Tests List of 10,000 Terms
    compareBinaryAndLinearSearch(10000)

    # Tests List of 100,000 Terms
    compareBinaryAndLinearSearch(100000)

    # Tests List of 10,000,000 Terms, cause why not
    compareBinaryAndLinearSearch(10000000)

main()
