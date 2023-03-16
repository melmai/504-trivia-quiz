from question_factory import QuestionFactory
from user_info import UserInfo


class Door:
    def __init__(self):
        self.__is_locked = True
        self.__question = QuestionFactory.generate_question()
        self.__answerable = True
        self.__info = UserInfo()

    @property
    def locked(self):
        return self.__is_locked

    @locked.setter
    def locked(self, is_locked):
        self.__is_locked = is_locked

    @property
    def answerable(self):
        return self.__answerable

    @answerable.setter
    def answerable(self, answerable):
        self.__answerable = answerable

    def unlock(self):
        """
        This method removes the barrier that prevents movement to the
        next room.
        """
        self.__is_locked = False

    def __get_user_response(self):
        """
        This method presents the player with a question and waits for an
        answer from the player
        :return: String
        """
        return input(self.__question.question + '\n')

    def check_answer(self):
        """
        This method checks the user provided response against the actual
        answer.
        """
        is_correct = None

        while is_correct is None:
            response = self.__get_user_response()
            is_correct = self.__question.check_response(response)
            if is_correct is None:
                self.__info.print_invalid_input()

        self.__answerable = False

        if is_correct:
            self.__info.print_correct_response()
            self.unlock()
        else:
            self.__info.print_incorrect_response()

    def try_door(self):
        """
        This method checks if door is unlocked and not disabled
        :return: Tuple that represents locked and answerable states of the door
        """
        if self.locked and self.answerable:  # locked, active
            self.check_answer()

        return self.locked, self.answerable

