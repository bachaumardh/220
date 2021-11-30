"""
Name: Hugo Bachaumard
lab13.py
Problem: Develop while control structures

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from algorithms import *


def trade_alert(filename):
    file = read_data(filename)
    file.insert(0, 0)
    print(file)
    for i in range(1, len(file)-1):
        if file[i] > 830:
            print('Wow! The trading volume was exceeding 830 at ', i, 'seconds')
        elif file[i] == 500:
            print('Attention, trading volume was exactly 500 at ', i, 'seconds')
    file.close()

