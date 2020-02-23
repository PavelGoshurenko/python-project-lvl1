from brain_games.cli import welcome_user
import prompt


def run(game_name):
    if (game_name == "even"):
        from brain_games.games.even import question_and_answer
        from brain_games.games.even import EXPLANATION
    elif (game_name == "calc"):
        from brain_games.games.calc import question_and_answer
        from brain_games.games.calc import EXPLANATION
    elif (game_name == "gcd"):
        from brain_games.games.gcd import question_and_answer
        from brain_games.games.gcd import EXPLANATION
    elif (game_name == "progression"):
        from brain_games.games.progression import question_and_answer
        from brain_games.games.progression import EXPLANATION
    else:
        print('We don’t have such a game yet!')
        return
    REQUIRED_CORRECT_ANSWERS = 3
    print("Welcome to the Brain Games!")
    print(EXPLANATION)
    name = welcome_user()
    number_of_correct_answers = 0
    while (number_of_correct_answers < REQUIRED_CORRECT_ANSWERS):
        (question, correct_answer) = question_and_answer()
        print('\nQuestion: ' + question)
        answer = prompt.string('Your answer: ')
        if (answer == correct_answer):
            print('Correct!')
            number_of_correct_answers += 1
        else:
            print("'{}' is wrong answer ;(. ".format(answer))
            print("Correct answer was '{}'.".format(correct_answer))
            print("Let's try again, {}!".format(name))
            return
    print('Congratulations, ' + name + '!')
