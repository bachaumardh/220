"""
Name: Hugo Bachaumard
bumper.py

Problem: Write a program that practices decision statements in Python graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import time
from random import randint
from graphics import GraphWin, Point, Circle
from modular import get_random_color, hit_horizontal, hit_vertical, did_collide, get_random


DELAY = .005


def ballbounce():
    width = 600
    height = 600
    radius = 20
    win = GraphWin("Bumper Cars!", width, height)
    p_1 = Point(randint(20, 580), randint(20, 580))
    circle_1 = Circle(p_1, radius)
    circle_1.setFill(get_random_color())
    circle_1.draw(win)
    p_2 = Point(randint(20, 580), randint(20, 580))
    circle_2 = Circle(p_2, radius)
    circle_2.setFill(get_random_color())
    circle_2.draw(win)
    value = 10
    d_x = get_random(value)
    d_y = get_random(value)
    d_x_2 = get_random(value)
    d_y_2 = get_random(value)
    for _ in range(1000):
        circle_1.move(d_x, d_y)
        circle_2.move(d_x_2, d_y_2)
        if hit_horizontal(circle_1, win):
            d_x = -d_x
        if hit_vertical(circle_1, win):
            d_y = -d_y
        if hit_horizontal(circle_2, win):
            d_x_2 = -d_x_2
        if hit_vertical(circle_2, win):
            d_y_2 = -d_y_2
        if did_collide(circle_1, circle_2):
            d_x = -d_x
            d_y = -d_y
            d_x_2 = -d_x_2
            d_y_2 = -d_y_2
        time.sleep(DELAY)


ballbounce()
