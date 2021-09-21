"""
Name: <Hugo Bachaumard>
interest.py

Problem: Showing ability to use python graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("6 Square Click", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(60, 60), Point(80, 80))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        botx = p.getX()+10
        boty = p.getY()+10
        topx = p.getX()-10
        topy = p.getY()-10

        # move amount is distance from center of circle to the
        # point where the user clicked

        shape2 = Rectangle(Point(topx, topy), Point(botx, boty))
        shape2.setOutline('red')
        shape2.setFill('red')
        shape2.draw(win)

    click5 = Text(Point(50, 20), "Click again to quit")
    click5.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width = 600
    height = 600
    win = GraphWin("Draw a rectangle.", width, height)
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click two points")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()

    drawing = Rectangle(p1, p2)
    drawing.setFill('yellow')
    drawing.setOutline('purple')
    drawing.draw(win)

    width = (p2.getX()) - (p1.getX())
    length = (p2.getY()) - (p1.getY())
    area = abs(length * width)
    perimeter = abs(2 * (length + width))
    area_text = Text(Point(300, 320), "Area is " + str(area))
    area_text.draw(win)
    perim_text = Text(Point(300, 300), "Perimeter is " + str(perimeter))
    perim_text.draw(win)

    instructions.setText("Click to end the program.")
    win.getMouse()
    win.close()


def circle():
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
    radius = (dx * dx + dy * dy)**0.5
    c = Circle(center, radius)
    c.setFill("purple")
    c.draw(win)
    radius_text = Text(Point(300, 320), "Radius is " + str(radius))
    radius_text.draw(win)
    instructions.setText("Click to end the program.")
    win.getMouse()
    win.close()


def pi2():

    n = eval(input("Enter the number of terms to sum."))
    x = 0
    for i in range(n):
        y = (-1) ** i / (2*i+1)
        x = x + y
    pi = x * 4
    print(pi)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
