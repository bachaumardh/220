"""
Name: Hugo Bachaumard
vigenere.py

Problem: Write a program that practices string data and function development.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *


def main():
    win_width = 600
    win_height = 300
    win = GraphWin("Vigenere", win_width, win_height)
    message_pt = Point(win_width / 8, win_height / 6)
    message_text = Text(message_pt, "Message to code")
    message_text.draw(win)
    message_input = Entry(Point(340, win_height / 6), 60)
    message_input.draw(win)
    key_pt = Point(win_width / 8, win_height / 3)
    key_text = Text(key_pt, "Enter Keyword")
    key_text.draw(win)
    key_input = Entry(Point(340, win_height / 3), 60)
    key_input.draw(win)
    button = Text(Point(win_width / 2, win_height / 2), "Encode")
    button.draw(win)
    r_button = Rectangle(Point(260, 130), Point(340, 170))
    r_button.setOutline("Black")
    r_button.draw(win)
    win.getMouse()
    message = message_input.getText()
    keyword = key_input.getText()
    message = message.replace(" ", "")
    keyword = keyword.replace(" ", "")
    message = message.upper()
    keyword = keyword.upper()
    win.getMouse()
    button.undraw()
    r_button.undraw()
    keyword = [ord(i) for i in keyword]
    message = [ord(i) for i in message]
    encryption = ""
    for i in range(len(message)):
        shift = (message[i] + keyword[i % len(keyword)]) % 26
        encryption += chr(shift + 65)
    code_text = Text(Point(win_width / 2, win_height / 2), encryption)
    code_text.draw(win)
    win.getMouse()
    win.close()


def code(message, keyword):
    message = message.replace(" ", "")
    keyword = keyword.replace(" ", "")
    message = message.upper()
    keyword = keyword.upper()
    keyword = [ord(i) for i in keyword]
    message = [ord(i) for i in message]
    encryption = ""
    for i in range(len(message)):
        shift = (message[i] + keyword[i % len(keyword)]) % 26
        encryption += chr(shift + 65)
    return encryption


main()
