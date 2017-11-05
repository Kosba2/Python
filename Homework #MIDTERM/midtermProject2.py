#! /usr/bin/python
# Homework No.MIDTERM  Exercise No.2
# File Name:     midtermProject2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          October 15, 2017
#
# Problem Statement: Create the Caesar Cipher Encoder and Decoder
#
#
# Overall Plan:
# 1. Create Encode Method
# 2. Do exact opposite operation to Decode
# 3. Spend 3 hours troubleshooting silly error
# 4. Cry
# 5. Realize the error is stupid
# 6. No longer have the drive to type up worthwhile algorithm/plan
# 7. Take out frustration on algorithm anyways
# 8. Why are you still reading this
#
# import the necessary python libraries


# Encodes a given String with a given Key and returns it
def encodeString(toEncode, key):
    # Preps return value
    cipherText = ""

    # Loops through each character in String
    for ch in toEncode:

        # Double Checks that character is a character not a digit/punctuation
        if ch.isalpha():

            # Performs shift to check whether outside bounds
            stayInAlphabet = ord(ch) + key

            # If lowercase & outside bounds shift back
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26

            # If uppercase & outside bounds shift back
            elif ord(ch) < (ord('Z') + 1) and stayInAlphabet > ord('Z'):
                stayInAlphabet -= 26

            # Processed/Shifted Letter
            shiftedLetter = chr(stayInAlphabet)

            # Adds back to result String to be returned at end
            cipherText += shiftedLetter

    # Returns the Ciphered Text
    return cipherText


# Encodes a given String with a given Key and returns it
def decodeString(toDecode, key):
    # Preps return value
    decipherText = ""

    # Loops through each character in String
    for ch in toDecode:

        # Double Checks that character is a character not a digit/punctuation
        if ch.isalpha():

            # Performs shift to check whether outside bounds
            stayInAlphabet = ord(ch) - key

            # If lowercase & outside bounds shift forward
            if (ord(ch) >= ord('a')) and (ord(ch) <= ord('z')) and stayInAlphabet < ord('a'):
                stayInAlphabet += 26

            # If uppercase & outside bounds shift forward
            elif (ord(ch) >= ord('A')) and (ord(ch) <= ord('Z')) and stayInAlphabet < ord('A'):
                stayInAlphabet += 26

            # Processed/Shifted Letter
            shiftedLetter = chr(stayInAlphabet)

            # Adds back to result String to be returned at end
            decipherText += shiftedLetter

    # Returns Deciphered Text
    return decipherText


def main():

    # Shift Key to keep the translation back and forth the same for output's sake
    key = 8

    # Keyword for flexibility
    keyword = "Sourpuss"

    # Stores original
    decodedString = keyword
    encodedString = encodeString(decodedString, key)

    # Gives User feedback
    print("Was " + decodedString + ", is now: " + encodeString(decodedString, key))
    print("Was " + encodedString + ", is now: " + decodeString(encodedString, key))


main()
