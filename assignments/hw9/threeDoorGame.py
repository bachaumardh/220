"""
Name: Hugo Bachaumard
threeDoorGame.py

Problem: Write a class for a three door game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from button import Button
from random import randrange
from graphics import GraphWin, Point, Text


def main():
    win = GraphWin("Three Button Game", 800, 600)
    win.setCoords(0, 0, 4, 2)
    quit_button = Button(win, Point(3.5, .3), .6, .3, "Quit")
    button1 = Button(win, Point(1, 1), .5, .5, "Door 1")
    button2 = Button(win, Point(2, 1), .5, .5, "Door 2")
    button3 = Button(win, Point(3, 1), .5, .5, "Door 3")
    title = Text(Point(2, 1.5), "CLICK TO CHOOSE A SECRET DOOR")
    title.draw(win)
    w = randrange(1, 4)
    if w == 1:
        button1.winning_button()
        winner = "Door 1"
    elif w == 2:
        button2.winning_button()
        winner = "Door 2"
    else:
        button3.winning_button()
        winner = "Door 3"

    pt = win.getMouse()
    title.undraw()

    while not quit_button.is_clicked(pt):

        if button1.is_clicked(pt):
            click = button1.color_button()

            if click:
                result = Text(Point(2, 1.5), "YOU WIN!!")
                result.setFill("green")
                result.setStyle("bold")
                end = Text(Point(2, .3), "CLICK QUIT TO CLOSE")
                end.setFill("black")
                end.draw(win)
                result.draw(win)

            else:
                result = Text(Point(2, 1.5), "YOU LOSE!!")
                result.setFill("red")
                result.setStyle("bold")
                result.draw(win)
                end = Text(Point(2, .3), "The secret door was " + winner)
                end.setFill("black")
                end.draw(win)

        if button2.is_clicked(pt):
            click = button2.color_button()

            if click:
                result = Text(Point(2, 1.5), "YOU WIN!!")
                result.setFill("green")
                result.setStyle("bold")
                result.draw(win)
                end = Text(Point(2, .3), "CLICK QUIT TO CLOSE")
                end.setFill("black")
                end.draw(win)

            else:
                result = Text(Point(2, 1.5), "YOU LOSE!!")
                result.setFill("red")
                result.setStyle("bold")
                result.draw(win)
                end = Text(Point(2, .3), "The secret door was "+winner)
                end.setFill("black")
                end.draw(win)

        if button3.is_clicked(pt):
            click = button3.color_button()

            if click:
                result = Text(Point(2, 1.5), "YOU WIN!!")
                result.setFill("green")
                result.setStyle("bold")
                result.draw(win)
                end = Text(Point(2, .3), "CLICK QUIT TO CLOSE")
                end.setFill("black")
                end.draw(win)

            else:
                result = Text(Point(2, 1.5), "YOU LOSE!!")
                result.setFill("red")
                result.setStyle("bold")
                result.draw(win)
                end = Text(Point(2, .3), "The secret door was " + winner)
                end.setFill("black")
                end.draw(win)

        pt = win.getMouse()

    win.close()


main()
