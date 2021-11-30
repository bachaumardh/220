"""
Name: Hugo Bachaumard
algorithms.py
Problem: Develop while control structures

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def read_data(filename):
    file_read = open(filename, 'r')
    line = file_read.read()
    new_line = line.split()
    i = 0
    while i < len(new_line):
        new_line[i] = eval(new_line[i])
        i = i + 1
    return new_line


def is_in_linear(search_val, values):
    lines = values
    found = False
    i = 0
    while i < len(lines) and not found:
        if lines[i] == search_val:
            found = True
            return found
        i = i+1
    return found


def good_input():
    number = int(input('Enter a number from 1 to 10: '))
    while True:
        if 0 <= number <= 10:
            return number
        else:
            print("Wrong Number!")
            number = int(input('Try again, enter a number between 1 and 10'))


def num_digits():
    number = int(input('Enter a positive integer: '))
    while number > 0:
        pos = 0
        while number > 0:
            pos = pos+1
            new_num = number // 10
            number = new_num
        print('Your number has ' + str(pos) + " digits.")
        number = int(input('Enter a positive integer: '))


def hi_lo_game():
    number = randint(1, 100)
    i = 0
    not_correct = True
    while i < 7 and not_correct:
        guess = int(input("Guess the number: "))
        if guess == number:
            not_correct = False
            print("Correct, you won in ", i+1, "guesses")
        elif guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
    else:
        print("Sorry, you lose!. The number was ", number)


def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1
    found = False
    while low <= high and not found:
        middle = (high + low) // 2

        if values[middle] == search_val:
            found = True
        else:
            if search_val < values[middle]:
                high = middle - 1
            else:
                low = middle + 1
    return found


def selection_sort(values):
    for i in range(len(values)-1):
        index = i
        for j in range(i+1, len(values)-1):
            if values[j] < values[index]:
                index = j
        values[i], values[index] = values[index], values[i]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    width = (p2.getX()) - (p1.getX())
    length = (p2.getY()) - (p1.getY())
    area = abs(length * width)
    return area


def rect_sort(rectangles):
    for i in range(len(rectangles) - 1):
        index = i
        calc_area(rectangles[i])
        for j in range(i+1, len(rectangles)-1):
            if rectangles[j] < rectangles[index]:
                index = j
        rectangles[i], rectangles[index] = rectangles[index], rectangles[i]

