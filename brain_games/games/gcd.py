from random import randint


EXPLANATION = 'Find the greatest common divisor of given numbers.\n'


def question_and_answer():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = str(number_1) + ' ' + str(number_2)
    if (number_1 > number_2):
        bigger = number_1
        smaller = number_2
    else:
        bigger = number_2
        smaller = number_1
    answer = smaller
    while (answer > 0):
        if ((bigger % answer) == 0) and ((smaller % answer) == 0):
            break
        else:
            answer -= 1
    return [question, str(answer)]
