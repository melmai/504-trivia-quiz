class TrueFalseQuestion:
    def __init__(self, question, answer, comment):
        self._question = question
        self._answer = answer
        self._comment = comment

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer

    @property
    def comment(self):
        return self._comment

    def normalize(self, response):
        """
        This method standardizes the user's response to compare against the
        correct answer.
        :param response:
        :return:
        """
        response = response.lower().strip()
        if response == "t" or response == "true":
            return True
        elif response == "f" or response == "false":
            return False
        else:
            return None

    def check_response(self, response):
        """
        This method checks the user's response to determine if it is correct
        :param response: user's response
        :return: Boolean
        """
        return self.normalize(response) == self._answer

    def mock(self):
        self._question = "5 is the binary number '10' expressed as a decimal"
        self._answer = False
        self._comment = "2"
