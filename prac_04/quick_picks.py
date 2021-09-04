"""
CP1404/CP5632 Practical - Suggested Solution
Quick pick program
"""

import random

MIN = 1
MAX = 45
COLUMNS = 6


def main():

    num_quick_picks = int(input("How many quick picks? "))
    while num_quick_picks < 0:
        print("That makes no sense!")
        num_quick_picks = int(input("How many quick picks? "))

    quick_picks = []
    for i in range(num_quick_picks):
        for num in range(COLUMNS):
            number = random.randint(MIN, MAX)
            while number in quick_picks:
                number = random.randint(MIN, MAX)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))