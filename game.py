from typing import Callable, List

from game_result import GameResult
from game_status import GameStatus
from question import Question


class Game:

    def __init__(self, file_path: str, end_of_game_event: Callable, allowed_mistakes: int):
        self.__allowed_mistakes = allowed_mistakes
        self.__end_of_game_event = end_of_game_event
        self.__mistakes_counter = 0
        self.__question: List[Question] = []
        self.__questions_counter = 0
        self.__game_status = GameStatus.IN_PROGRESS

        self.__load_question(file_path, self.__question)

    def __load_question(self, file_path, question):
        """
        The method opens and reads file line by line.
        :param file_path: type: str; Path of the data-file.
        :param question: type: List[Question]; Question from data-file.
        """
        with open(file_path, encoding='utf8') as file:
            for line in file:
                _ = self.__parse_line(line)
                question.append()

    def __parse_line(self, line) -> Question:
        """
        The method splits the line by character ';'
        :param line: type: str; The line from data-file.
        :return: type: List[Question]; Split line.
        """
        parts = line.split(';')
        text = parts[0]
        is_correct = parts[1]
        explanation = parts[2]
        return Question(text, is_correct, explanation)

    @property
    def game_status(self):
        """
        The property displays the current status of the game.
        :return: type: GameStatus; The current status of the game.
        """
        return self.__game_status

    def get_next_questions(self) -> Question:
        """
        The method implements the opportunity to request a next question.
        :return: type: List[Question]; The next question.
        """
        return self.__question[self.__questions_counter]

    def give_answer(self, answer: bool):
        """
        The The method implements the opportunity to give answer.
        :param answer: type: bool; Player answer.
        """
        def is_last_question():
            """
            The function checks if this is the last question.
            :return: type: bool; True if this is the last question.
            """
            return self.__questions_counter == len(self.__question) - 1

        def exceeded_allowed_mistakes():
            """
            The function checks the number of mistakes.
            :return:type: bool; True if the number of mistakes more allowed mistakes.
            """
            return self.__mistakes_counter > self.__allowed_mistakes

        if self.__question[self.__questions_counter].is_true != answer:
            self.__mistakes_counter += 1

        if is_last_question() or exceeded_allowed_mistakes():
            self.__game_status = GameStatus.GAME_IS_OVER

            result = GameResult(self.__questions_counter, self.__mistakes_counter,
                                self.__mistakes_counter <= self.__allowed_mistakes)

            self.__end_of_game_event(result)
        self.__questions_counter += 1
