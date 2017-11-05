#! /usr/bin/python
# Homework No.5  Exercise No.1
# File Name:     hw5project1.py
# Programmer:    Kostyantyn Shumishyn
# Date:          September 24, 2017
#
# Problem Statement: Takes a phrase and turns it into an Acronym
#
#
# Overall Plan:
# 1. Prompts the user for a phrase
# 2. Capitalizes the first letter of each word, then splits into a list of words
# 3. Takes the first letter of each word and concatenates into String with a dot
# 4. Prints out the Acronym
#
# import the necessary python libraries


def main():
    # Prompts the user for a Phrase
    phrase = input("Please input a phrase to turn into Acronym (no punctuation)\n")

    # Stores the List of Strings
    phraseList = phrase.title().split()

    # Pre-emptively creates variable to store Acronym
    acronym = ""

    # Loops through all the first letters of each word
    for token in phraseList:
        firstLetter = token[0]
        acronym += firstLetter + "."

    print(acronym)


main()
