"""
Name: Hugo Bachaumard
hw9.py

Problem: Write a class for a three door game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import Point, Rectangle, Text


class Button:
    def __init__(self, win, position, width, height, label):
        w, h = width / 2.0, height / 2.0
        x, y = position.getX(), position.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.door = Rectangle(p1, p2)
        self.door.setFill("white")
        self.door.draw(win)
        self.label = Text(position, label)
        self.label.draw(win)
        self.winner = False

    def is_clicked(self, point):
        return self.xmin <= point.getX() <= self.xmax and self.ymin <= point.getY() <= self.ymax

    def winning_button(self):
        self.winner = True

    def color_button(self):
        if self.winner:
            self.door.setFill("green")
            return True
        else:
            self.door.setFill("red")
            return False
