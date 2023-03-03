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
        This method presents the player with a question and waits for an
        answer from the player
        :return: String
        """
        return input(self._question.question + '\n')


    def check_answer(self, response=None):
        """
        This method checks the user provided response against the actual
        answer.
        :return: Boolean
        """
        response = response or self.get_user_response()
        is_correct = self._question.check_response(response)
        self._answerable = False

        if is_correct:
            print("Yas queen")
            self.unlock()
            return True
        else:
            print("Yikes. Not this time, bud.")
        return False

    def try_door(self):
        if self.locked and self.answerable:  # locked, active
            self.check_answer()

        return self.locked, self.answerable

if __name__ == '__main__':
    door = Door()
    answer = door.check_answer()
    print(answer)
