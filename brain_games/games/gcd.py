from random import randint


EXPLANATION = 'Find the greatest common divisor of given numbers.'


def find_gcd(number_1, number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    return number_1


def question_and_answer():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = str(number_1) + ' ' + str(number_2)
    answer = find_gcd(number_1, number_2)
    return (question, str(answer))
