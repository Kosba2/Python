# Homework No.14  Exercise No.2
# File Name:     echo_server.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 3, 2017
#
# Problem Statement: Create a Server Class

# Imports
import socket
from hw14project2.Stack import *


# Reverses a String using an Implemented Stack Class cause why not
def reverseString(myString):
    # Creates Stack and Result String
    stringStack = Stack()
    resultString = ''

    # Adds each char to Stack
    for character in myString:
        stringStack.push(character)

    # While the Stack isn't empty, keep popping characters, now coming out in reverse
    while not stringStack.isEmpty():
        resultString += stringStack.pop()

    # Return reversed String
    return resultString


def Main():
    # Host is this Machine
    host = '127.0.0.1'

    # Random Non-Privileged Port
    port = 12345

    # Creates new Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binds Host and Port to Socket
    s.bind((host, port))

    # Listens for only 1 Connection at a time
    s.listen(1)

    # Receives a Connection Socket and an Address
    connection, address = s.accept()

    # Gives Feedback of Connection
    print('\nConnection from: ', str(address) + "\n")

    # While talking to client
    while True:
        # Data received from Client
        data = connection.recv(1024).decode('utf-8')

        # If the connection is closed by client
        if not data:
            break

        # Prints feedback to user
        # print("Data from connected user: " + data)
        data = reverseString(data)
        # print("Sending: " + data + "\n")
        connection.send(data.encode('utf-8'))

    # Closes Socket
    connection.close()


if __name__ == '__main__':
    Main()
