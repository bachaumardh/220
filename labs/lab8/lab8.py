"""
Name: Hugo Bachaumard
lab8.py

Problem: Showing ability to write functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import *


def number_words(in_file_name, out_file_name):
    outfile = open(out_file_name, 'w')
    infile = open(in_file_name, 'r')
    wal = infile.readlines()
    wal = wal[0].split() + wal[1].split()
    for i in range(len(wal)):
        lines = str(1+i) + " " + (wal[i]) + "\n"
        outfile.write(lines)
    outfile.close()
    infile.close()


def hourly_wages(in_file_name, out_file_name):
    outfile = open(out_file_name, 'w')
    infile = open(in_file_name, 'r')
    wage = infile.readlines()
    wage = wage[0].split() + wage[1].split()
    increase_1 = (float(wage[2]) + 1.65) * float(wage[3])
    increase_2 = (float(wage[6]) + 1.65) * float(wage[7])
    outfile.write(wage[0] + " " + wage[1] + " " + "$" + str(increase_1) + "\n")
    outfile.write(wage[4] + " " + wage[5] + " " + "$" + str(increase_2) + "\n")
    outfile.close()
    infile.close()


def calc_check_sum(isbn):
    total = 0
    for i in range(len(isbn)):
        n = isbn[i]
        num = int(n)
        total += (10 - i) * num
    print("Checksum =" + " " + str(total))


def send_message(file, friend):
    friend = friend + ".txt"
    outfile = open(friend, 'w')
    infile = open(file, 'r')
    letter = infile.read()
    outfile.write(letter)
    infile.close()
    outfile.close()


def send_safe_message(file, friend, key):
    friend = friend + ".txt"
    outfile = open(friend, 'w')
    infile = open(file, 'r')
    letter = infile.read()
    message = encode(letter, key)
    outfile.write(message)
    infile.close()
    outfile.close()


def send_uncrackable_message(file, friend, pad):
    friend = friend + ".txt"
    outfile = open(friend, 'w')
    third = open(pad, 'r')
    infile = open(file, 'r')
    pad_1 = third.read()
    letter = infile.read()
    message = encode_better(letter, pad_1)
    outfile.write(message)
    infile.close()
    outfile.close()


def main():
    hourly_wages("hourly_wages.txt", "Wages.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "bob")
    send_safe_message("secret_message.txt", "alice", "1")
    send_uncrackable_message("safest_message.txt", "rick", "pad.txt")
main()
