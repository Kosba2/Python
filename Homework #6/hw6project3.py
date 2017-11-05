#! /usr/bin/python
# Homework No.6  Exercise No.2
# File Name:     hw6project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 1, 2017
#
# Problem Statement: Prints the Lyrics for 10 verses of The Ants go Marching
#
#
# Overall Plan:
# 1. Defines function for converting number to string
# 2. Defines function to get rhyme for verse number
# 3. Uses above functions to create a Verse Function
# 4. Loops 10 times to print 10 verses of song
#
# import the necessary python libraries


def numToString(integer):
    number = ""
    if integer == 1:
        number = "one"
    elif integer == 2:
        number = "two"
    elif integer == 3:
        number = "three"
    elif integer == 4:
        number = "four"
    elif integer == 5:
        number = "five"
    elif integer == 6:
        number = "six"
    elif integer == 7:
        number = "seven"
    elif integer == 8:
        number = "eight"
    elif integer == 9:
        number = "nine"
    elif integer == 10:
        number = "ten"

    return number


def getRhyme(integer):
    rhyme = ""
    if integer == 1:
        rhyme = "have some fun"
    elif integer == 2:
        rhyme = "sneeze ACHOO"
    elif integer == 3:
        rhyme = "climb a tree"
    elif integer == 4:
        rhyme = "close the door"
    elif integer == 5:
        rhyme = "dance the jive"
    elif integer == 6:
        rhyme = "get Pick Up Stix"
    elif integer == 7:
        rhyme = "pray on Earth to Heaven"
    elif integer == 8:
        rhyme = "apologize for being late"
    elif integer == 9:
        rhyme = "drink some wine"
    elif integer == 10:
        rhyme = "point out the giant hen"

    return rhyme


def antsChorus(verse):
    verseString = numToString(verse)
    rhymeString = getRhyme(verse)
    print(
        "The ants go marching " + verseString + " by " + verseString + ", hurrah, hurrah")
    print(
        "The ants go marching " + verseString + " by " + verseString + ", hurrah, hurrah")

    print("The ants go marching " + verseString + " by " + verseString + ",")
    print("The little one stops to " + rhymeString)

    print("And they all go marching down to the ground")

    if verse != 10:
        print("To get out of the rain, BOOM! BOOM! BOOM!")
    else:
        print("To get out of the rain.")

def main():
    # Loops 10 verses, sort of hardcoded for 10th verse to be final
    for verse in range(10):
        antsChorus(verse + 1)
        print()


main()
