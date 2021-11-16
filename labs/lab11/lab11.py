"""
Name: Hugo Bachaumard
lab10.py

Problem: Use decision and repetition structures to solve a problem

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import random


def read():
    file = 'wordlist.txt'
    word_list = open(file, 'r')
    word_list = word_list.read().splitlines()
    return word_list


def pick():
    word_pick = read()
    random_number = random.randint(0, len(word_pick)-1)
    word_pick = word_pick[random_number]
    return word_pick


def guess():
    word = pick()
    shown_word = ["_"] * len(word)
    xinput = ""
    allowed_guesses = 7
    letter_number = 0
    right_guesses = 0
    guessed_letters = []

    while xinput != "END" and allowed_guesses != 0:
        print("The secret word is " + str(shown_word))
        print("Number of guesses left: " + str(allowed_guesses))
        xinput = input("Your guess: ")

        while letter_number < len(word):
            if word[letter_number] == xinput:
                shown_word[letter_number] = xinput
                right_guesses += 1

            letter_number += 1

        if xinput not in word:
            print("This character is not present in the name.")
            allowed_guesses -= 1

        letter_number = 0

        if right_guesses == len(word):
            print("Winner! The word was " + word)
            break

        if allowed_guesses == 0:
            print("You are out of guesses. Game over! The word was " + word)


def hangman():
    guess()


def main():
    hangman()


main()

