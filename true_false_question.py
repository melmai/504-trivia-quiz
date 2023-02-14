class TrueFalseQuestion:
    def __init__(self):
        self._question = None
        self._answer = None

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer
