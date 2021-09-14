"""
Name: Hugo Bachaumard
lab3.py

Problem: Create simple programs the use for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    print("This function will calculate your average grade.")
    grade = eval(input("Enter the amount of grades you wish to input."))
    total = 0
    for i in range(0, grade):
        grades = eval(input("Enter your grade on HW" + str(i)+':'))
        total = total + grades
    print("Your average grade is", total/grade)


def tip_jar():
    print("This function will calculate the total amount in the jar.")
    total = 0
    for i in range(0, 5):
        change = eval(input("How much did you donate?"))
        total = total + change
    print("Your total change is $", total)


def newton():
    print("This function will approximate the square root using Newton's method")
    number = eval(input('What is the number you are trying to square root?'))
    times = eval(input("How many times will you approve the approximation?"))
    approx = number/2
    approx = (0.5 * (approx + (number / approx)))
    for i in range(0, times):
        approx = (0.5 * (approx + (number / approx)))
    print("The square root of", number, "is about", approx)


def sequence():
    print("This function will show you a sequence of odd numbers.")
    terms = eval(input("What is the number of terms in a series?"))
    total = 1
    for i in range(2, terms+2):
        total = (i % 2)*2 + total
        print(total, end=" ")


def pi():
    print("This function will estimate the value of pi.")
    terms = eval(input("What is the number of terms in the series?"))
    estimate = 1
    mult = 2
    for i in range(terms):
        top = mult/(mult-1)
        bot = mult/(mult+1)
        estimate *= bot * top
        mult += 2
    print("The estimate of pi is", estimate * 2)



