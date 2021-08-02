"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

dir(random)


def score_status(score):
    if score < 0:
        print("Invalid score")
    elif score > 100:
        print("Invalid score")
    elif score > 90:
        print('Excellent')
    elif score < 50:
        print("Bad")
    elif score > 50:
        print("Passable")


def main():
    score = float(input("Enter score: "))
    score_status(score)
    generate_score()


def generate_score():
    print(random.randrange(100))


main()
