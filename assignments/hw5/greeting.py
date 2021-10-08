"""
Name: Hugo Bachaumard
greeting.py

Problem: Write a program that practices the author's graphics package.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import time
from graphics import (GraphWin, Point, Text, Circle, Polygon, Line)


def valentine():
    win_width = 500
    win_height = 500
    win = GraphWin("Happy Valentine's Day!", win_width, win_height)
    win.setBackground("purple")
    shape = Circle(Point(win_width / 3, win_height / 2 - 30), 90)
    shape_2 = Circle(Point(2*win_width / 3, win_height / 2 - 30), 90)
    tri = Polygon(Point(110, win_height / 2+40), Point(390, win_height / 2+40),
                  Point(win_width / 2, 420))
    middle = Circle(Point(win_width / 2, win_height / 2), 60)
    middle.draw(win)
    middle.setFill("red")
    tri.setOutline("red")
    tri.draw(win)
    tri.setFill("red")
    shape_2.setFill("red")
    shape.setFill("red")
    shape.setOutline("red")
    shape_2.setOutline("red")
    shape_2.draw(win)
    shape.draw(win)
    time.sleep(1)
    happy = Text(Point(win_width / 8, 40), "HAPPY")
    happy.setTextColor("magenta")
    happy.setSize(36)
    happy.setStyle("bold")
    happy.draw(win)
    time.sleep(1)
    txt = Text(Point(win_width / 2, 40), "VALENTINES")
    txt.setTextColor("magenta")
    txt.setSize(36)
    txt.setStyle("bold")
    txt.draw(win)
    time.sleep(1)
    day = Text(Point(win_width*7 / 8, 40), "DAY !!")
    day.setTextColor("magenta")
    day.setSize(36)
    day.setStyle("bold")
    day.draw(win)
    time.sleep(1)
    arrow = Line(Point(0, 500), Point(150, 350))
    arrow.setArrow("last")
    arrow.setFill("white")
    arrow.setWidth(10)
    arrow.draw(win)
    arrow.move(-100, 100)
    for i in range(200):
        time.sleep(0.001)
        arrow.move(1, -1)
    arrow.undraw()
    pierce = Line(Point(0, 500), Point(150, 350))
    pierce.setFill("white")
    pierce.setWidth(10)
    pierce.move(100, -100)
    pierce.draw(win)
    pierce.undraw()
    for i in range(40):
        pierce1 = Line(Point(0+i, 500-i), Point(150, 350))
        pierce1.setWidth(10)
        pierce1.move(100, -100)
        pierce1.setFill("white")
        pierce1.draw(win)
        time.sleep(0.001)
        pierce1.undraw()
    pierce1.draw(win)
    for i in range(60):
        tip = Line(Point(0, 250), Point(30+i, 220-i))
        tip.setWidth(10)
        tip.setFill("white")
        tip.setArrow("last")
        tip.move(350, -80)
        tip.draw(win)
        tip.undraw()
    tip.draw(win)
    happy.undraw()
    day.undraw()
    txt.undraw()
    for i in range(6):
        blink = Text(Point(win_width / 2, 40), "HAPPY VALENTINES DAY!!")
        blink.setTextColor("magenta")
        blink.setSize(36)
        blink.setStyle("bold")
        blink.draw(win)
        time.sleep(1)
        blink.undraw()
        time.sleep(1)
    inst_pt = Point(win_width / 2, win_height - 10)
    instructions = Text(inst_pt, "Click anywhere to close")
    instructions.setSize(20)
    instructions.setTextColor("white")
    instructions.draw(win)
    win.getMouse()
    win.close()


valentine()
