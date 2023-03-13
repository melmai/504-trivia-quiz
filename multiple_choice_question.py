from true_false_question import TrueFalseQuestion


class MultipleChoiceQuestion(TrueFalseQuestion):
    def __init__(self, question, choices, answer):
        self._question = question
        self._choices = choices
        self._answer = answer

    def __str__(self):
        return f'{self._question} {self._choices}'

    def check_response(self, response):
        """
        This method checks the response of the user against the actual answer.
        :param response: String
        :return: Boolean
        """
        response = self.normalize(response)
        return response if response is None else response == self._answer

    def normalize(self, response):
        """
        This method formats the user's response for comparing against the
        answer.
        :param response: Original response from the user
        :return: Reformatted string
        """
        response = response.lower().strip
        return response
