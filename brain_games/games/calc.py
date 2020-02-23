from random import randint


EXPLANATION = 'What is the result of the expression?\n'


def question_and_answer():
    operator = randint(1, 3)  # 1 = + | 2 = - | 3 = *
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    if (operator == 1):
        question = str(number_1) + ' + ' + str(number_2)
        answer = str(number_1 + number_2)
    elif (operator == 2):
        question = str(number_1) + ' - ' + str(number_2)
        answer = str(number_1 - number_2)
    else:
        question = str(number_1) + ' * ' + str(number_2)
        answer = str(number_1 * number_2)
    return (question, answer)
