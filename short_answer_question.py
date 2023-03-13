from true_false_question import TrueFalseQuestion


class ShortAnswerQuestion(TrueFalseQuestion):
    def __init__(self, question, answer):
        self._question = question
        self._answer = answer

    def check_response(self, response):
        """
        This method checks the response of the user against the actual answer.
        :param response: String
        :return: Boolean
        """
        response = self.normalize(response)
        return response == self._answer

    def normalize(self, response):
        """
        This method formats the user's response for comparing against the
        answer.
        :param response: Original response from the user
        :return: Reformatted string
        """
        response = response.lower().strip
        return response
