from typing import Callable, List

from game_status import GameStatus
from question import Question


class Game:

    def __init__(self, file_path: str, end_of_game_event: Callable, allowed_mistakes: int):
        self.__file_path = file_path
        self.__allowed_mistakes = allowed_mistakes
        self.__end_of_game_event = end_of_game_event
        self.__mistakes_counter = 0
        self.__question: List[Question] = []
        self.__questions_counter = 0
        self.__game_status = GameStatus.IN_PROGRESS

        self.__load_question(file_path, self.__question)

    def __load_question(self, file_path, question):
        with open(file_path, encoding='utf8') as file:
            for line in file:
                _ = self.__parse_line(line)
                question.append()

    def __parse_line(self, line):
        parts = line.split(';')
        text = parts[0]
        is_correct = parts[1]
        explanation = parts[2]
        return Question(text, is_correct, explanation)

    @property
    def game_status(self):
        return self.__game_status

    def get_next_questions(self) -> Question:
        return self.__question[self.__questions_counter]

    def give_answer(self, answer: bool):
        if self.__question[self.__questions_counter].is_true != answer:
            self.__mistakes_counter += 1
    