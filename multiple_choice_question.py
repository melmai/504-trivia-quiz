from true_false_question import TrueFalseQuestion


class MultipleChoiceQuestion(TrueFalseQuestion):
    def __init__(self, question, choices, answer):
        super().__init__(question, answer)
        self.__choices = choices

    def __str__(self):
        return f'Multiple Choice: {self._question}\nChoices: {self.__choices}'

    @property
    def choices(self):
        return self.__choices

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
        response = response.lower().strip()
        return response

    @staticmethod
    def mock():
        """
        This method creates an instance of the MultipleChoiceQuestion with known values for testing purposes.
        :return: MultipleChoiceQuestion
        """
        question = "What's the largest bone in the human body?"
        choices = "Femur, Humerus, Tibia, Sacrum"
        answer = "femur"
        return MultipleChoiceQuestion(question, choices, answer)


if __name__ == "__main__":
    mcq = MultipleChoiceQuestion.mock()
    print(mcq)
    print(mcq.answer)
