# Homework No. FINAL  Exercise No.2
# File Name:     finalProject2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 14, 2017
#
# Problem Statement: Creates a Dictionary of Names and gives feedback on them
#
#
# Overall Plan:
# 1. Scrapes Girl and Boy Name Text files and creates Lists and Counts
# 2. Stores Counts and Ranks as Instance Variables on Name Rank Object
# 3. Creates a Dictionary Matching Names to Name Ranks
# 4. Prompts user for Name Input and provides feedback by looking up in Dictionary.

from NameRank import NameRank


# Reads in Name List Text Files and returns a Tuple
def scrapeNameFile(fileName):
    # Creates an empty word list
    nameList = []
    countList = []

    # Reads in File
    with open(fileName, 'r') as file:
        # Removes all punctuation
        lines = file.readlines()

        for line in lines:
            # Splits Line into a list of Words
            lineList = line.split()

            # Adds Name and Count to corresponding lists
            nameList.append(lineList[0])
            countList.append(lineList[1])

    # Returns the list of Words from that File
    return nameList, countList


# Makes a Dictionary of Names to NameRanks
def createNameRank(nameList, countList):
    # Makes Dictionary ADT
    dictionary = {}

    # Builds Dictionary
    for i in range(0, len(countList)):
        dictionary[nameList[i]] = NameRank(i + 1, countList[i])

    # Returns the Dictionary
    return dictionary


def Main():
    # Reads in Girl List
    girlNameList, girlCountList = scrapeNameFile("girlnames.txt")

    # Makes Girl Dictionary
    girlDictionary = createNameRank(girlNameList, girlCountList)

    # Reads in Boy List
    boyNameList, boyCountList = scrapeNameFile("boynames.txt")

    # Makes Boy Dictionary
    boyDictionary = createNameRank(boyNameList, boyCountList)

    # Prompts user for Input of a name
    name = input("Please Enter a Name: ")

    # Gives Feedback for Girl name
    tempNameRank = girlDictionary.get(name)
    if tempNameRank is None:
        print(name + " is not ranked among the top 1000 girl names.")
    else:
        print(name + " is ranked " + str(
            tempNameRank.Rank) + " in popularity among girls with " + str(
            tempNameRank.Count) + " namings.")

    # Gives Feedback for Boy name
    tempNameRank = boyDictionary.get(name)
    if tempNameRank is None:
        print(name + " is not ranked among the top 1000 boy names.")
    else:
        print(name + " is ranked " + str(
            tempNameRank.Rank) + " in popularity among boys with " + str(
            tempNameRank.Count) + " namings.")


Main()
