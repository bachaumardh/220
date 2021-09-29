"""
Name: Hugo Bachaumard
traffic.py

Problem: Write a program that practices accumulations and nested loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    roads = eval(input("How many roads were surveyed?"))
    total = 0
    for i in range(1, roads+1):
        days = eval(input('How many days was road' + " " + str(i) + " " + 'surveyed?'))
        current_sum = 0
        for _ in range(1, days+1):
            cars = eval(input('How many cars traveled on day' + " " + str() + '?'))
            current_sum = current_sum + cars
        total = total + current_sum
        avr = current_sum/days
        avr = round(avr, 2)
        print("Road" + " " + str(i) + " " + "average vehicles per day: " + str(avr))
    print("Total number of vehicles traveled on all roads:", total)
    print("Average number of vehicles per road:", round((total/roads), 2))


if __name__ == '__main__':
    main()
