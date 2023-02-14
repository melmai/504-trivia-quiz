from true_false_question import TrueFalseQuestion


class MultipleChoiceQuestion(TrueFalseQuestion):
    def __init__(self):
        super().__init__()
        choices: []

    def check_response(self, response):
        """
        This method checks the response of the user against the actual answer.
        :param response: String
        :return: Boolean
        """
        pass

    def normalize(self, response):
        """
        This method formats the user's response for comparing against the
        answer.
        :param response: Original response from the user
        :return: Reformatted string
        """
        pass
