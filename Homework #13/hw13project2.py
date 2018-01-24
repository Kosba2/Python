# Homework No.13  Exercise No.2
# File Name:     hw13project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          November 26, 2017
#
# Problem Statement: Creates the Recursive Palindrome Definition
#
#
# Overall Plan:
# 1. Create a Function to Clean String
# 2. Create a Function to Recursively check whether a substring is a Palindrome
# 3. Prompt user for Input of a String
# 4. Provides Feedback on whether it is a Palindrome

import re


# Removes all non-alphabetic characters
def cleanPalindrome(palindrome):
    return re.sub("[^a-zA-Z]+", "", palindrome).lower()


# Recursive Palindrome Method
def recursivePalindrome(cleanText):
    # Base Case
    if len(cleanText) < 2:
        return True
    # Substring first and last Are Equal
    elif cleanText[0] == cleanText[len(cleanText) - 1]:
        return recursivePalindrome(cleanText[1:len(cleanText) - 1])
    # Substring first and last Not Equal
    else:
        return False


def main():
    # Prompts user for Input of a Sentence
    sentence = input("Please enter Palindrome to check: ")

    # Cleans Palindrome of all special characters
    cleanSentence = cleanPalindrome(sentence).lower()

    # Calls Recursive Palindrome Method
    isPalindrome = recursivePalindrome(cleanSentence)

    # If it is a Palindrome
    if isPalindrome:
        print('"' + sentence + '" is a palindrome!')
    # If it is not a Palindrome
    else:
        print('"' + sentence + '" is not a palindrome!')


main()
