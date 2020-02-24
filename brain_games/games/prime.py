from random import randint


EXPLANATION = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def is_prime(number):
    if number < 2:
        return False
    index = 2
    while (index < (number / 2 + 1)):
        if ((number % index == 0)):
            return False
        index += 1
    return True


def question_and_answer():
    question = randint(1, 100)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return (str(question), answer)
