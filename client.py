from game_result import GameResult


def end_of_game_handler(result: GameResult):
    print(f'Question asked: {result.questions_passed}. Mistakes made: {result.mistakes_made}')
    print('You are winner!' if result.won else 'You are loser!')
