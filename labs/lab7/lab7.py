"""
Name: Hugo Bachaumard
lab7.py

Problem: Showing ability to use arguments and return values.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def cash_conversion():
    dollar = int(input("Please input an integer"))
    dollar_format = "$"+"{:.2f}".format(dollar)
    print(dollar_format)


def encode():
    message = input("Enter the message to be encoded.")
    key = int(input("Enter integer key value."))
    encryption = ""
    for i in message:
        message_index = ord(i) + key
        encryption = encryption + chr(message_index)
    print(encryption)


def sphere_area(radius):
    return 4*3.14159 * radius**2


def sphere_volume(radius):
    return (4/3)*3.14159 * radius ** 3


def sum_n(integer):
    sum_1 = 0
    for i in range(1, integer+1):
        sum_1 += i
    return sum_1


def sum_n_cubes(integer):
    sum_cubes = 0
    for i in range(1, integer+1):
        sum_cubes += i**3
    return sum_cubes


def encode_better():
    message = input("Enter the message to be encoded.")
    key = input("Enter the key.")
    encryption = ""
    for i in range(len(message)):
        shift = ord(key[i]) + ord(message[i])-97
        encryption = encryption + chr(shift)
    print(encryption)


def main():
    cash_conversion()
    encode()
    #sphere_area()
    #sphere_volume()
    #sum_n()
    #sum_n_cubes()
    encode_better()


main()
