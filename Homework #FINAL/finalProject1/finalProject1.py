# Homework No. FINAL  Exercise No.1
# File Name:     finalProject1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 14, 2017
#
# Problem Statement: Create a Spell Checker using a provided dictionary.
#
#
# Overall Plan:
# 1. Reads in each file filtering out excess punctuation, making lists of words
# 2. Compares spell-check word list words to the dictionary word list
# 3. Prints out the words if they are not in the dictionary

from graphics import *
from button import Button


def extractWords(inputString):
    # Imports all Ascii Letters
    from string import ascii_letters

    # Returns only the words
    return "".join([ch for ch in inputString if ch in (ascii_letters + "'" + " " + "\n")])


def scrapeFileForWords(fileName):
    # Creates an empty word list
    wordList = []

    # Reads in File
    with open(fileName, 'r') as file:
        # Removes all punctuation
        line = extractWords(file.read())

        # Splits Line into a list of Words
        lineList = str.split(line)

        # Takes each word and adds it to Word List
        for word in lineList:
            wordList.append(word)

    # Returns the list of Words from that File
    return wordList


# Binary Search for Strings
def binarySearchString(wordList, key):
    # Start & End
    start = 0
    end = len(wordList) - 1

    # Continues until Start and End Pass Each other
    while start <= end:
        middle = (start + end) // 2
        midpoint = wordList[middle]
        if midpoint > key:
            end = middle - 1
        elif midpoint < key:
            start = middle + 1
        else:
            return midpoint


# Method to Output Words not present in Dictionary
def outputMistakes(spellCheckList, dictionaryList):
    # Boolean for utility
    foundMistake = False

    # For every word in Spell-check List
    for spellWord in spellCheckList:
        # Stores the spell-word if found
        key = binarySearchString(dictionaryList, spellWord)

        # Notes if any mistake was found
        if key is None:
            print(spellWord)
            foundMistake = True

    # Gives Boolean Feedback of Found Mistakes
    return foundMistake


# noinspection PyBroadException
def Main():
    # Defines default Window Width and Height
    WIDTH = 600
    HEIGHT = 400

    # Makes the Window for the Spellchecker
    spellWin = GraphWin("Spell Checker", WIDTH, HEIGHT)
    spellWin.setBackground("darkred")

    # Draws the Instructions
    genInstruction = Text(Point(WIDTH / 2, 40), "Instructions")
    genInstruction.draw(spellWin)
    genInstructions = Text(Point(WIDTH / 2, 70), "Enter File Names then press Spell Check Button.")
    genInstructions.draw(spellWin)
    fileEntryInstruction = Text(Point(.25 * WIDTH, HEIGHT / 2 - 30), "Spell-checked File")
    fileEntryInstruction.draw(spellWin)
    dictionaryEntryInstruction = Text(Point(.75 * WIDTH, HEIGHT / 2 - 30), "Dictionary File")
    dictionaryEntryInstruction.draw(spellWin)

    # Draws the File Entry Box
    entryToCheck = Entry(Point(.25 * WIDTH, HEIGHT / 2), 16)
    entryToCheck.draw(spellWin)
    entryToCheck.setText("spellCheckFile.txt")

    # Draws the Dictionary Entry Box
    entryDictionary = Entry(Point(.75 * WIDTH, HEIGHT / 2), 16)
    entryDictionary.draw(spellWin)
    entryDictionary.setText("dictionary.txt")

    # Makes Process Button
    checkFileButton = Button(spellWin, Point(WIDTH / 2, 260), 180, 20, "Check File Spelling")
    checkFileButton.activate()

    # Makes Quit Button
    quitButton = Button(spellWin, Point(WIDTH / 2, 290), 80, 20, "Quit")
    quitButton.activate()

    # Primary Loop - Truly an abuse of human potential
    while True:
        try:
            # Stores the click Location
            click = spellWin.getMouse()

            # If clicked the Process Button
            if checkFileButton.clicked(click):
                try:
                    # Reads in Words from File to Spell-check
                    spellCheckList = scrapeFileForWords(entryToCheck.getText())

                    # Reads in Words from Dictionary
                    dictionaryList = scrapeFileForWords(entryDictionary.getText())

                    # Compares files
                    print("Checking File for spelling mistakes...\n")
                    foundMistake = outputMistakes(spellCheckList, dictionaryList)

                    # Gives feedback on mistakes
                    if foundMistake:
                        print("The above words were not in the dictionary.\n")
                    else:
                        print("No spelling mistakes were found! Congratulations.\n")

                    # States finished checking
                    print("Checking for spelling mistakes Complete.\n\n\n\n")

                except:
                    print("One of the file names was invalid.")

            # If clicked the Quit Button
            elif quitButton.clicked(click):
                print("Exiting Program...")
                break

        except:
            print("Exiting Program...")
            break


Main()
