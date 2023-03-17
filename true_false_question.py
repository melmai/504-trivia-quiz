class TrueFalseQuestion:
    def __init__(self, question, answer):
        self._question = question
        self._answer = answer

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer

    def __str__(self):
        return f"{self._question}"

    def normalize(self, response):
        """
        This method standardizes the user's response to compare against the
        correct answer.
        :param response:
        :return:
        """
        response = str(response.lower().strip())
        if response == "t" or response == "true":
            response = "true"
        elif response == "f" or response == "false":
            response = "false"
        return response

        # if response == "t" or response == "true":
        #     return True
        # elif response == "f" or response == "false":
        #     return False
        # else:  # invalid input
        #     return None

    def check_response(self, response):
        """
        This method checks the user's response to determine if it is correct
        :param response: user's response
        :return: Boolean or None if input is invalid
        """
        response = self.normalize(response)
        if response == str(self._answer):
            return True
        else:
            return False
        # return response if response is None else response == self._answer
