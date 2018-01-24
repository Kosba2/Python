# cdieview.py
#   Implementation of a DieView with changeable forground color
#   Illustrates inheritance

from hw12project1.dieview2 import DieView


class ColorDieView(DieView):
    def setValue(self, value):
        self.value = value  # remember this value
        DieView.setValue(self, value)  # call setValue from parent class

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)
