#! /usr/bin/python
# Homework No.MIDTERM  Exercise No.1
# File Name:     midtermProject1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 15, 2017
#
# Problem Statement: Given a list of numbers, provide statistical information about them
#
#
# Overall Plan:
# 1. Read the numerical Data from an input.txt text file into a list
# 2. Find the sample mean of the list
# 3. Sort the list
# 4. Find the median of the list
# 5. Find the sample standard deviation of list
# 6. Provide information to user
# 7. Handles Division by Zero in all cases
#
# import the necessary python libraries


# Reads numbers from file, each number separated by spaces
def readNumbersFromFile():
    # Constant File Name
    inFileName = "input.txt"

    # Create File Streams
    inFile = open(inFileName)

    # Creates Lists to Store numbers
    sortedList = []

    # Adds each String number into list as a numeric
    for number in inFile.readlines():
        # Appends number to list
        sortedList.append(eval(number))

    # Closes Self as Courtesy, even though TECHNICALLY unnecessary in this method
    inFile.close()

    # Sorts List in numerical order
    sortedList.sort()

    # Returns List for Manipulation
    return sortedList


# Finds mean of a list
def findMeanOfList(anyList):
    # Initializes Mean to be used in summation
    mean = 0
    numTerms = len(anyList)

    # Handles Division by 0
    if numTerms == 0:
        numTerms = 1

    # Sums values in list
    for number in anyList:
        mean += number

    # Averages them
    mean /= numTerms

    # Returns Mean
    return mean


# Finds the Median of a SORTED List of numbers
def findMedianOfList(sortedList):
    # Handles empty List
    if len(sortedList) == 0:
        return 0

    # If Odd just take Middle Number
    elif len(sortedList) % 2 == 1:
        # Returns the Odd Median
        return sortedList[len(sortedList) // 2]

    # If Even find mean of two Middle Numbers
    else:
        # Adds the Middle two numbers then divides by 2
        averageMedian = 0
        averageMedian += sortedList[len(sortedList) // 2]
        averageMedian += sortedList[(len(sortedList) // 2) - 1]
        averageMedian /= 2

        # Returns the Even Median
        return averageMedian


# Finds the SAMPLE Standard Deviation of a List of numbers
def findSDOfList(anyList):
    # Prepares the necessary components of formula
    mean = findMeanOfList(anyList)
    numTerms = len(anyList)
    rmsSum = 0

    # Handles division by 0
    if (numTerms - 1) == 0:
        numTerms = 2

    # Sums up the Root Mean Square of Sample Data
    for number in anyList:
        rmsSum += ((number - mean) ** 2)

    # Solves for the Sample Standard Deviation
    standardDeviation = (rmsSum / (numTerms - 1)) ** (1 / 2)

    # Returns the Sample Standard Deviation
    return standardDeviation


def main():
    # List of Sorted Data read from file
    sortedData = readNumbersFromFile()

    # Finds Mean of List
    meanData = findMeanOfList(sortedData)

    # Finds Median of Sorted List
    medianData = findMedianOfList(sortedData)

    # Standard Deviation
    sdData = findSDOfList(sortedData)

    # Gives Feedback to user
    print("Your Data is as follows; ")
    print(sortedData)
    print("\nThe Mean is " + str(round(meanData, 2)))
    print("The Median is " + str(round(medianData, 2)))
    print("The Standard Deviation is " + str(round(sdData, 2)))
    print(
        "The 2 S.D. Range is " + str(round(meanData - 2 * sdData, 2)) + " through " + str(
            round(meanData + 2 * sdData, 2)))


main()
