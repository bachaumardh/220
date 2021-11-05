from random import randint
from graphics import *


def get_random(move):
    return randint(-move, move)


def did_collide(circle_ball, circle_ball_2):
    center_1 = circle_ball.getCenter()
    x_1 = center_1.getX()
    y_1 = center_1.getY()
    center_2 = circle_ball_2.getCenter()
    x_2 = center_2.getX()
    y_2 = center_2.getY()
    center_distance = (((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)) ** 0.5
    radius = 20
    min_distance = radius*2
    if center_distance <= min_distance:
        return True
    else:
        return False


def hit_vertical(circle_ball, win):
    height = win.getHeight()
    width = win.getWidth()
    center = circle_ball.getCenter()
    x = center.getX()
    y = center.getY()
    radius = circle_ball.getRadius()
    ylow = radius
    yhigh = width - radius
    xlow = radius
    xhigh = height - radius
    if x <= ylow or x >= yhigh or y <= xlow or y >= xhigh:
        return True
    else:
        return False


def hit_horizontal(circle_ball, win):
    height = win.getHeight()
    width = win.getWidth()
    center = circle_ball.getCenter()
    x = center.getX()
    y = center.getY()
    radius = circle_ball.getRadius()
    ylow = radius
    yhigh = width - radius
    xlow = radius
    xhigh = height - radius
    if x <= ylow or x >= yhigh or y <= xlow or y >= xhigh:
        return True
    else:
        return False


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color
