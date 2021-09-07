import math
"""
Name: Hugo Bachaumard
lab2.py
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def sum_of_threes():
    upper_bound = eval(input("Enter the upper bound"))
    total_sum = 0
    for i in range(0, upper_bound + 1, 3):
        total_sum += i
    print(total_sum)


def multiplication_table():
    for row in range(1, 11):
        print(row, end=" ")
        for col in range(1, 11):
            print(row*col, end=" ")
        print()


def triangle_area():
    a = eval(input("Enter a"))
    b = eval(input("Enter b"))
    c = eval(input("Enter c"))
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)


def sum_squares():
    upper_bound = eval(input("Enter the upper bound"))
    lower_bound = eval(input("Enter the lower bound"))
    total = 0
    for i in range(lower_bound, upper_bound+1):
        total = total + i**2
    print(total)


def power():
    base = eval(input("Enter the base"))
    exponent = eval(input("Enter the exponent"))
    total = 1
    for i in range(exponent):
        total = total * base
    print(base, "^", exponent, "=", total)
