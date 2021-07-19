#!/usr/bin/env python3

import random


DESCRIPTION = 'Answer "yes" if given number is even, otherwise answer "no".'

FIRST, END = 1, 100


def get_question():
    number = random.randint(FIRST, END)
    return number


def is_even(number):
    return False if number % 2 else True


def get_round():
    number = get_question()
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, str(number)
