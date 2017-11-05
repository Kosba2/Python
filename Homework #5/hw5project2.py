#! /usr/bin/python
# Homework No.5  Exercise No.2
# File Name:     hw5project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          September 24, 2017
#
# Problem Statement: Reads in a two column list of numbers, sums them then outputs
# that list
#
#
# Overall Plan:
# 1. Opens input and output Streams with Constant file names
# 2. Makes arrays early
# 3. Splits each column of numbers into its own list using input stream
# 4. Sums the numbers from each list into third list
# 5. Prints to final new file using output stream
# 6. Closes both Streams
#
# import the necessary python libraries


def main():
    # Constant File Name
    inFileName = "input.txt"
    outFileName = "output.txt"

    # Creates File Streams
    inFile = open(inFileName)
    outFile = open(outFileName, 'w')

    # Pre-emptively makes lists
    firstNumbers = []
    secondNumbers = []
    sumNumbers = []

    # Loops through all the lines being read in
    for line in inFile.readlines():
        # Splits each Line
        data = line.split()
        # Takes the first Index and puts it into first List
        firstNumbers.append(eval(data[0]))
        # Takes the second Index and puts it into second List
        secondNumbers.append(eval(data[1]))

    # Sums numbers from each list
    for index in range(len(firstNumbers)):
        summation = firstNumbers[index] + secondNumbers[index]
        sumNumbers.append(str(summation) + '\n')

    # Writes the Sum to a new Text File
    outFile.writelines(sumNumbers)

    # Closes Streams
    inFile.close()
    outFile.close()


main()
