from random import randint


EXPLANATION = 'Answer "yes" if number even otherwise answer "no".\n'


def question_and_answer():
    question = randint(0, 100)
    if (question % 2 == 0):
        answer = 'yes'
    else:
        answer = 'no'
    return (str(question), answer)
