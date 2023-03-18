from question_factory import QuestionFactory
from user_info import UserInfo
from user_input import UserInput


class Door:
    def __init__(self, question=None):
        self.__is_locked = True
        self.__answerable = True

        if question:
            self.__question = question
        else:
            self.__question_factory = QuestionFactory()
            self.__question = self.__question_factory.generate_question()

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

    def check_answer(self, answer=None, is_correct=None):
        """
        This method checks the user provided response against the actual
        answer.
        """
        while is_correct is None:
            response = answer or UserInput.answer(self.__question)
            is_correct, right_answer = self.__question.check_response(response)
            if is_correct is None:
                UserInfo.invalid()

        # can't answer this question anymore
        self.__answerable = False

        if is_correct:
            UserInfo.correct()
            self.unlock()
        else:
            UserInfo.incorrect(right_answer)

    def try_door(self):
        """
        This method checks if door is unlocked and not disabled
        :return: Tuple that represents locked and answerable states of the door
        """
        if self.locked and self.answerable:  # locked, active
            self.check_answer()
        elif not self.answerable:  # we've been here before
            UserInfo.retry()

        return self.locked, self.answerable

    @staticmethod
    def mock(question_type):
        """
        This method creates a Door object for testing purposes
        :param question_type:
        :return: Door
        """
        question = QuestionFactory.mock(question_type)
        return Door(question)


if __name__ == "__main__":
    print(Door.mock("TrueFalse"))



