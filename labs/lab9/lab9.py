"""
Name: Hugo Bachaumard
lab9.py

Problem: Showing ability to write functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def main():
    # add other function calls here
    pass


def addTens(nums):
    nums = nums
    nums_2 = [i+10 for i in nums]


def squareEach(nums):
    nums = nums
    nums_2 = [i**2 for i in nums]


def sumList(nums):
    sum_1 = sum(nums)
    return sum_1


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])


def writeSumOfSquares():
    file = input("Enter the name of an input file with at least two numbers on each line: ")
    infile = open(file, 'r')
    write = "sum_out.txt"
    outfile = open(write, 'w')
    file_1 = infile.readlines()
    for i in file_1:
        new_file = i.split()
        toNumbers(new_file)
        squareEach(new_file)
        final = sumList(new_file)
        outfile.write("Sum of squares = " + str(final) + "\n")


def starter():
    weight = float(input("Enter the wrestler's weight: "))
    numWins = int(input("Enter the wrestler's number of wins: "))
    if 150 <= weight < 160 and numWins >= 5:
        return "Earned a starting position!"
    elif weight > 199 or numWins > 20:
        return "Earned a starting position!"
    else:
        return "Did not earn a starting position."


def leapYear(year):
    if year % 4 == 0 and year % 100 != 0 and year % 4 == 0:
        return True
    return False


def circleOverlap():
    width = 600
    height = 600
    win = GraphWin("Draw a circle.", width, height)
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click two points")
    instructions.draw(win)
    center = win.getMouse()
    point = win.getMouse()
    dx = point.getX() - center.getX()
    dy = point.getY() - center.getY()
    radius = (dx * dx + dy * dy) ** 0.5
    c = Circle(center, radius)
    c.setFill("purple")
    c.draw(win)
    instructions.undraw()
    instructions_2 = Text(inst_pt, "Click two more points")
    instructions_2.draw(win)
    center_2 = win.getMouse()
    point_2 = win.getMouse()
    dx_2 = point_2.getX() - center_2.getX()
    dy_2 = point_2.getY() - center_2.getY()
    radius_2 = (dx_2 * dx_2 + dy_2 * dy_2) ** 0.5
    c_2 = Circle(center_2, radius_2)
    c_2.setFill("red")
    c_2.draw(win)
    min_distance = radius + radius_2
    center_distance = (((center_2.getX()-center.getX())**2) + ((center_2.getY()-center.getY())**2)) ** 0.5
    if center_distance < min_distance:
        instructions_2.setText("The circles overlap.")
    else:
        instructions_2.setText("The circles do not overlap.")
    inst_point = Point(width / 2, height - 30)
    instructions_close = Text(inst_point, "Click again to close")
    instructions_close.draw(win)
    win.getMouse()
    win.close()
