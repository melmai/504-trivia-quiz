import unittest
from trivia_quiz import TriviaQuiz


class TriviaQuizTest(unittest.TestCase):
    def setUp(self):
        self.tq = TriviaQuiz()


if __name__ == '__main__':
    unittest.main()
