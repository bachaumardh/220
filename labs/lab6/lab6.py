"""
Name: <Hugo Bachaumard>
lab6.py

Problem: Showing ability to use python graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Please enter your name in first-last order, separated by a space.")
    n = name.split()
    n.reverse()
    print(n[0] + "," + " " + n[1])


def company_name():
    web = input("Please enter your websites URL.")
    c = web.split(".")
    print(c[1])


def initials():
    students = eval(input("How many names will be input?"))
    for i in range(1, students + 1):
        first = input('Enter the first name of student' + " " + str(i) + ":")
        last = input('Enter ' + str(first) + "'s last name:")
        print(str(first) + "'s initials are " + first[0] + last[0] + ".")


def names():
    name_list = input("Enter peoples names, separated by commas")
    first = name_list.split(", ")
    print("The initials are", end=" ")
    for i in range(len(first)):
        word = first[i].split(" ")
        first_name = word[0]
        last_name = word[1]
        q = first_name[0] + last_name[0]
        print(q, end=" ")


def thirds():
    amount = eval(input("How many sentences will be input?"))
    for i in range(amount):
        sentences = input("Please enter your sentence")
        for j in range(2, len(sentences), 3):
            word = sentences[j]
            print(word, end="")
        print()


def word_average():
    amount = eval(input("How many sentences will be input?"))
    for i in range(amount):
        sentences = input("Please enter your sentence")
        total = sentences.split()
        words_sum = 0
        words = 0
        for j in range(len(total)):
            words = len(total[j])
            words_sum += words
        print(words_sum/len(total))

def pig_latin():
    sentence = input("Enter a sentence")
    words = sentence.split()
    new_statement = " "
    for i in range(len(words)):
        new_statement += i[1]+i[0]+'ay'
        new_statement.lower()
        print(new_statement)


def main():
    pig_latin()
    #word_average()
    #thirds()
    #names()
    #initials()
    #company_name()
    #name_reverse()
    # add other function calls here


main()
