from brain_games.cli import welcome_user
import prompt


REQUIRED_CORRECT_ANSWERS = 3


def run(game):
    print("Welcome to the Brain Games!")
    print(game.EXPLANATION)
    print()
    name = welcome_user()
    number_of_correct_answers = 0
    while number_of_correct_answers < REQUIRED_CORRECT_ANSWERS:
        question, correct_answer = game.question_and_answer()
        print('\nQuestion: ' + question)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print("'{}' is wrong answer ;(. ".format(answer))
            print("Correct answer was '{}'.".format(correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
        number_of_correct_answers += 1
    print('Congratulations, {}!'.format(name))
