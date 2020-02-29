from random import randint


EXPLANATION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 10
MIN_START = 1
MAX_START = 10


def question_and_answer():
    step = randint(MIN_STEP, MAX_STEP)
    start = randint(MIN_START, MAX_START)
    missing_index = randint(1, PROGRESSION_LENGTH)
    index = 1
    number = start
    question = ''
    while (index <= PROGRESSION_LENGTH):
        if (index == missing_index):
            answer = number
            new_member = '.. '
        else:
            new_member = str(number) + ' '
        question += new_member
        number += step
        index += 1
    return (question, str(answer))
