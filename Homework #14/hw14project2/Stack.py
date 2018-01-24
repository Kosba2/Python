# Homework No.14  Exercise No.2
# File Name:     hw14project2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 3, 2017
#
# Problem Statement: Creates a Stack Class


class Stack:

    # Constructs an Empty Stack Object
    def __init__(self):
        # List of Items
        self._a = []

    # Returns True if Stack is Empty, else False
    def isEmpty(self):
        return len(self._a) == 0

    # Pushes Object item onto the top of Stack
    def push(self, item):
        self._a += [item]

    # Pops the top object from Stack and returns it
    def pop(self):
        return self._a.pop()

    # Returns a String representation of Stack
    def __str__(self):
        s = ''
        for item in self._a:
            s = str(item) + ' ' + s

        return s