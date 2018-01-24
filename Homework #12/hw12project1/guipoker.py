# guipoker.py

from hw12project1.cdieview import ColorDieView
from graphics import *

from hw12project1.button import Button


class GraphicsInterface:
    def __init__(self):
        # Make Splash Window
        splash = GraphWin("Dice Poker", 600, 400)
        splash.setBackground("green3")

        # Make Banner
        banner = Text(Point(300, 30), "Python  Poker  Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(splash)

        # Make Welcome Message
        msg = Text(Point(300, 380), "Welcome to Poker!")
        msg.setSize(18)
        msg.draw(splash)

        # Make Lets Play Button
        playPokerButton = Button(splash, Point(300, 180), 160, 40, "Let's Play Poker!")
        playPokerButton.activate()
        quitPokerButton = Button(splash, Point(300, 280), 150, 40, "Quit Poker!")
        quitPokerButton.activate()

        # Waits until a choice is made
        while not playPokerButton.clicked(splash.getMouse()):
            if quitPokerButton.clicked(splash.getMouse()):
                sys.exit()

        # Proceeds to Main Program
        splash.close()

        # Make Window
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")

        # Make Banner
        banner = Text(Point(300, 30), "Python  Poker  Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)

        # Make Welcome Message
        self.msg = Text(Point(300, 380), "Welcome to the dice table.")
        self.msg.setSize(18)
        self.msg.draw(self.win)

        # Make Dice
        self.createDice(Point(300, 100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300, 170), 75, 30)

        # Make Roll Dice Button
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)

        # Make Score Button
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)

        # Make Quit Button
        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)

        # Make Money Text
        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def createDice(self, center, size):
        center.move(-3 * size, 0)
        self.dice = []
        for i in range(5):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5 * size, 0)

    def addDiceButtons(self, center, width, height):
        center.move(-3 * width, 0)
        for i in range(1, 6):
            label = "Die %d" % (i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5 * width, 0)

    def choose(self, choices):
        buttons = self.buttons
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        while 1:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()

    def setMoney(self, amt):
        self.money.setText("$%d" % (amt))

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def close(self):
        self.win.close()

    def showResult(self, msg, score):
        if score > 0:
            text = "%s! You win $%d" % (msg, score)
        else:
            text = "You rolled %s" % (msg)
        self.msg.setText(text)

    def drawHelp(self):
        help = GraphWin("Dice Poker", 300, 200)
        help.setBackground("red")

        # Make Banner
        banner = Text(Point(150, 30), "Poker Help!")
        banner.setSize(20)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(help)

        # Make Welcome Message
        p1 = "Five of a Kind     : $30\n"
        p2 = "Straight             : $20\n"
        p3 = "Four of a Kind    : $15\n"
        p4 = "Three of a Kind : $ 8\n"
        p5 = "Two Pairs         : $ 5\n"
        p6 = "Garbage           : $ 0"

        msg = Text(Point(150, 120), p1 + p2 + p3 + p4 + p5 + p6)
        msg.setSize(12)
        msg.draw(help)

    def chooseDice(self):
        choices = []
        while 1:
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score"])

            # Make Help Button
            helpButton = Button(self.win, Point(30, 375), 45, 30, "Help")
            helpButton.activate()

            if helpButton.clicked(self.win.getMouse()):
                self.drawHelp()

            if b[0] == "D":
                i = eval(b[4]) - 1
                if i in choices:
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:
                for d in self.dice:
                    d.setColor("black")
                if b == "Score":
                    return []
                elif choices != []:
                    return choices


from hw12project1.pokerapp import PokerApp

inter = GraphicsInterface()
app = PokerApp(inter)
app.run()
