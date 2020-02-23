from random import randint


EXPLANATION = 'What number is missing in the progression?\n'


def question_and_answer():
    PROGRESSION_LENGTH = 10
    MIN_STEP = 1
    MAX_STEP = 10
    MIN_START = 1
    MAX_START = 10
    step = randint(MIN_STEP, MAX_STEP)
    start = randint(MIN_START, MAX_START)
    missing_index = randint(1, PROGRESSION_LENGTH)
    index = 1
    number = start
    question = ''
    while (index <= PROGRESSION_LENGTH):
        if (index == missing_index):
            answer = number
            question = question + '.. '
        else:
            question = question + str(number) + ' '
        number += step
        index += 1
    return (question, str(answer))
