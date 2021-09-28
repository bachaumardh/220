"""
Name: <Hugo Bachaumard>
lab5.py

Problem: Showing ability to use python graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def distance(p1, p2):
    dist = ((p2.getX() - p1.getX())**2 + ((p2.getY() - p1.getY())**2))**0.5
    return dist


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click three points")
    instructions.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    tri = Polygon(p1, p2, p3)
    tri.setFill('cyan')
    tri.setOutline('green')
    tri.draw(win)
    perimeter = (distance(p1, p2) + distance(p2, p3) + distance(p3, p1))/2
    area = (perimeter*(perimeter-distance(p1, p2))*(perimeter-distance(p2, p3))*(perimeter-distance(p3, p1)))**0.5

    perim_text = Text(Point(300, 300), "Perimeter is " + str(perimeter))
    perim_text.draw(win)
    area_text = Text(Point(300, 320), "Area is " + str(area))
    area_text.draw(win)

    instructions.setText("Click to end the program.")
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)
    # Create text box

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_input = Entry(Point(win_width / 2, win_height / 2 + 40), 3)
    red_input.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_input = Entry(Point(win_width / 2, win_height / 2 + 70), 3)
    green_input.draw(win)
    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_input = Entry(Point(win_width / 2, win_height / 2 + 100), 3)
    blue_input.draw(win)
    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    #get inputs for color
    for i in range(0, 5):
        win.getMouse()
        red = red_input.getText()
        blue = blue_input.getText()
        green = green_input.getText()
        color = color_rgb(int(red), int(green), int(blue))
        shape.setFill(color)

    inst.setText("Click to end the program.")
    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input("Enter a string")
    first_char = string[0]
    print(first_char)
    last_char_index = len(string) - 1
    last_char = string[last_char_index]
    print(last_char)
    pos_2_5 = string[1:5]
    print(pos_2_5)
    conc = first_char + last_char
    print(conc)
    for i in range(0, 10):
        print(string[0:3])
    for i in range(len(string)):
        print(string[i])
    print(len(string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0]+values[2]
    print(x)
    x = (5*values[1])
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[2] + values[0] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def main():
    distance()
    triangle()
    color_shape()
    process_list()
    process_string()
    target()

    pass


main()
