from brain_games.cli import welcome_user
from random import randint
import prompt


def main():
    REQUIRED_CORRECT_ANSWERS = 3
    print("Welcome to the Brain Games!")
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = welcome_user()
    number_of_correct_answers = 0
    while (number_of_correct_answers < REQUIRED_CORRECT_ANSWERS):
        number = randint(0, 100)
        if (number % 2 == 0):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('\nQuestion: ' + str(number))
        answer = prompt.string('Your answer: ')
        if (answer == correct_answer):
            print('Correct!')
            number_of_correct_answers += 1
        else: 
            print ("'" + answer + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'.")
            print("Let's try again, " + name + "!'")
            return
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
