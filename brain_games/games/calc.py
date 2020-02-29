from random import randint, choice
from operator import add, sub, mul


EXPLANATION = 'What is the result of the expression?'


def question_and_answer():
    operator, symbol = choice(((add, '+'), (sub, '-'), (mul, '*')))
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = str(number_1) + symbol + str(number_2)
    answer = str(operator(number_1, number_2))
    return (question, answer)
