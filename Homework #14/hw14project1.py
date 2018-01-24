# Homework No.14  Exercise No.1
# File Name:     hw14project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 2, 2017
#
# Problem Statement: Create and tests Sort, SelectionSort and MergeSort Functions
#
#
# Overall Plan:
# 1. Creates Selection Sort and Merge Sort Method
# 2. Compares Run Times at different lengths
# 3. Prints Feedback
# 4. Wait 4 1/3 hours because if n = 5000 and runs for 163 seconds at an O(N^2) runtime
#    then that means 10N would be 10^2 longer run time, or 163*100 seconds or 4.333 hours.
# 5. THANKS PROFESSOR.

import time
from random import *


# Selection Sort Function
def selectionSort(listToSort):
    # Stores length of List
    lengthList = len(listToSort)

    # For every position in the list
    for bottom in range(lengthList - 1):
        # Find the smallest item in list
        mp = bottom

        # Look at each position and find smallest
        for i in range(bottom + 1, lengthList):
            if listToSort[i] < listToSort[mp]:
                mp = i

        # Performs the swap with Tuple
        listToSort[bottom], listToSort[mp] = listToSort[mp], listToSort[bottom]


# Helper Function to Merge Sort
def recursiveMergeSort(left, right):
    # If either list reaches the end, append remaining list appropriately
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0

    # Loops until it has processed both lists
    while len(result) < len(left) + len(right):
        # Sorts left < right
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        # Sorts right >= left
        else:
            result.append(right[j])
            j += 1

        # Exit Case
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    # Default Return Case
    return result


# Main/Base Case Method call
def mergeSort(listToSort):
    # Default Case for non-lists
    if len(listToSort) < 2:
        return listToSort

    # Recursive Case
    middle = len(listToSort) // 2
    left = mergeSort(listToSort[:middle])
    right = mergeSort(listToSort[middle:])

    # Delegates smaller tasks to Helper
    return recursiveMergeSort(left, right)


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
    for i in range(listSize, 0, -1):
        # Appends Linearly up to listSize
        numList.append(i)

    # Returns the list of random numbers
    return numList


def compareSorts(lengthList):
    # Creates a list of integers between 0 & 1000000 of length lengthList
    randomNumberListA = generateList(lengthList)
    randomNumberListB = generateList(lengthList)
    randomNumberListC = generateList(lengthList)

    # Verifies list Length
    print('Lists are ' + str(len(randomNumberListA)) + ' numbers long')

    # Runs Regular Sort
    regSortTime = time.perf_counter()
    randomNumberListA.sort()
    regSortTime = time.perf_counter() - regSortTime
    print('Regular Sort Function took ' + str(regSortTime) + ' seconds.')

    # Runs MergeSort
    mergeSortTime = time.perf_counter()
    mergeSort(randomNumberListC)
    mergeSortTime = time.perf_counter() - mergeSortTime
    print('Merge Sort Function took ' + str(mergeSortTime) + ' seconds.')

    # Runs Selection Sort
    selectionSortTime = time.perf_counter()
    selectionSort(randomNumberListB)
    selectionSortTime = time.perf_counter() - selectionSortTime
    print('Selection Sort Function took ' + str(selectionSortTime) + ' seconds.')
    print()


def main():
    # Tests List of 5,000 Terms
    compareSorts(5000)

    # Tests List of 50,000 Terms
    compareSorts(50000)

    # Tests List of 500,000 Terms
    compareSorts(500000)


main()
