from question_factory import QuestionFactory
class Door:
    def __init__(self):
        self._is_locked = True
        self._question = QuestionFactory.generate_question()

    def unlock(self):
        """
        This method removes the barrier that prevents movement to the
        next room.
        """
        self._is_locked = False

    def check_answer(self, response):
        """
        This method checks the user provided response against the actual
        answer.
        :param response: String provided by user
        :return: Boolean
        """
        return
