# Homework No.14  Exercise No.2
# File Name:     echo_client.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 3, 2017
#
# Problem Statement: Create a Client Class

# Imports
import socket


def Main():
    # Host is this Machine
    host = '127.0.0.1'

    # Random Non-Privileged Port
    port = 12345

    # Creates new Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connects Host and Port
    s.connect((host, port))

    # Gets Message from the User
    message = input("Enter String or \"Q\" to quit -> ")

    # Quit Case
    while message.lower() != 'q':
        s.send(message.encode('utf-8'))
        data = s. recv(1024).decode('utf-8')
        print("Received from the Server: " + data + "\n")
        message = input("Enter String or \"Q\" to quit -> ")

    # Closes Socket
    s.close()


if __name__ == '__main__':
    Main()
