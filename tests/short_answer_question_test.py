import unittest
from short_answer_question import ShortAnswerQuestion


class ShortAnswerQuestionTest(unittest.TestCase):
    def setUp(self):
        self.saq = ShortAnswerQuestion.mock()

    def test_normalize(self):
        response = "diagonally"
        self.assertEqual(self.saq.normalize(response), "diagonally")

        response = "diagnally"
        self.assertNotEqual(self.saq.normalize(response), "diagonally")

        response = "  diagonally "
        self.assertEqual(self.saq.normalize(response), "diagonally")

        response = "DIAgonally"
        self.assertEqual(self.saq.normalize(response), "diagonally")

    def test_check_response(self):
        response = "diagonally"
        self.assertEqual(self.saq.check_response(response), True)

        response = "diagonal"
        self.assertEqual(self.saq.check_response(response), False)

        response = "diagonallly"
        self.assertEqual(self.saq.check_response(response), False)


if __name__ == '__main__':
    unittest.main()
