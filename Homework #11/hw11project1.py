#! /usr/bin/python
# Homework No.11  Exercise No.1
# File Name:     hw11project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          November 12, 2017
#
# Problem Statement: Counts number of Keywords in a file
#
# Overall Plan:
# 1. Reads in keywords from file
# 2. Prompts for file to count keywords on
# 3. Prompts whether to exclude comments
# 4. Reads in each line and splits it into String list
# 5. Looks at each string in list and checks whether it's a keyword
# 6. Prints out number of keywords.
#
# import the necessary python libraries

# Successfully removing Comments if desired, but can't figure out what the special case
# is that I'm failing to count some keywords, could have something to do with multiple
# keywords on one line, or multiple copies of the same keyword on one line, not sure
# unfortunately.

def main():
    # Defines List for Keywords
    keywordList = []

    # Keeps track of number of Keywords
    numKeywords = 0

    # Reads into list the Python Keywords from File
    with open('keywords.txt') as f:
        for line in f:
            line = line.strip('\n')
            keywordList.append(line)

    # Tests List
    # print(keywordList)

    # Prompts user for Name of File to Scan for Keywords
    fileName = input("Please enter the name (w/ extension) of file whose Python "
                     "keywords you wish to count.\nFilename : ")

    # Scans the named file for every keyword
    try:
        with open(fileName, 'r') as g:

            # Prompts for Excluding Comments
            excludeComments = (input("Exclude Comments, (y/n): ", ))

            if excludeComments.lower().startswith("y"):
                exclude = True
            else:
                exclude = False

            for line in g:
                lineList = line.split()

                # Processing Loop
                for keyword in keywordList:
                    # Case one, exclude comments
                    if keyword in lineList and exclude and not lineList[0].startswith(
                            "#"):
                        numKeywords += 1

                    # Case two, include comments
                    if keyword in lineList and not exclude:
                        numKeywords += 1

        print("Your file contained " + str(numKeywords) + " keywords.")

    except:
        print("Input Filename was invalid. Exiting program.")


main()
