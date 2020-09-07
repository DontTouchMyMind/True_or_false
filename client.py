from game import Game
from game_result import GameResult
from game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f'Question asked: {result.questions_passed}. Mistakes made: {result.mistakes_made}')
    print('You are winner!' if result.won else 'You are loser!')


game = Game('data/Questions.csv', end_of_game_handler, allowed_mistakes=3)

while game.game_status == GameStatus.IN_PROGRESS:

    question = game.get_next_questions()
    print("Do you believe in the next statement?")

    print(question.text)

    answer = input() == 'y'

    if question.is_true == answer:
        print('You are right!')
    else:
        print('You are wrong!')
        print(question.explanation)

    game.give_answer(answer)
