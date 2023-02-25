from question_factory import QuestionFactory


class Door:
    def __init__(self):
        self._is_locked = True
        self._question = QuestionFactory.generate_question()
        self._answerable = True

    @property
    def locked(self):
        return self._is_locked

    @locked.setter
    def locked(self, is_locked):
        self._is_locked = is_locked

    @property
    def answerable(self):
        return self._answerable

    @answerable.setter
    def answerable(self, answerable):
        self._answerable = answerable

    def unlock(self):
        """
        This method removes the barrier that prevents movement to the
        next room.
        """
        self._is_locked = False

    def get_user_response(self):
        """
        This method presents the player with a question and either unlocks
        the door or disables the door in response
        """
        user_response = input(self._question.question)
        is_correct = self.check_answer(user_response)

        if is_correct:
            print("Yas queen")
            self.unlock()
        else:
            print("Yikes. Not this time, bud.")
            self._answerable = False

    def check_answer(self, response):
        """
        This method checks the user provided response against the actual
        answer.
        :param response: String provided by user
        :return: Boolean
        """
        return self._question(response)

    def mock(self, question_type):
        if question_type == "tf_question":
            QuestionFactory.
