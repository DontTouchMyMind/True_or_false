from typing import Callable


class Game:

    def __init__(self, file_path: str, end_of_game_event: Callable, allowed_mistakes: int):
        self.__file_path = file_path
        self.__allowed_mistakes = allowed_mistakes
        self.__end_of_game_event = end_of_game_event
        self.__mistakes_counter = 0
        self.__question = []
        self.__questions_counter = 0