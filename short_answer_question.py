from true_false_question import TrueFalseQuestion


class ShortAnswerQuestion(TrueFalseQuestion):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def check_response(self, response):
        """
        This method checks the response of the user against the actual answer.
        :param response: String
        :return: Boolean
        """
        response = self.normalize(response)
        if response == str(self.answer):
            return True
        else:
            return False

    def normalize(self, response):
        """
        This method formats the user's response for comparing against the
        answer.
        :param response: Original response from the user
        :return: Reformatted string
        """
        response = str(response.lower().strip())
        return response

    @staticmethod
    def mock():
        """
        Creates an instance of the ShortAnswerQuestion with known values for
        testing purposes.
        :return: ShortAnswerQuestion
        """
        question = "Short answer: In chess, what direction can a bishop move?"
        answer = "diagonally"
        return ShortAnswerQuestion(question, answer)
