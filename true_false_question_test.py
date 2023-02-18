import unittest
from true_false_question import TrueFalseQuestion


class TrueFalseQuestionTest(unittest.TestCase):
    def setUp(self):
        question = "5 is the binary number '10' expressed as a decimal."
        answer = False
        comment = "The binary number '10' represents 2 in decimal."
        self.tfq = TrueFalseQuestion(question, answer, comment)

    def test_get_question(self):
        self.assertEqual(self.tfq.question,
                         "5 is the binary number '10' expressed as a decimal.")

    def test_get_answer(self):
        self.assertEqual(self.tfq.answer, False)

    def test_check_answer(self):
        pass

    def test_normalize(self):
        pass


if __name__ == "__main__":
    unittest.main()