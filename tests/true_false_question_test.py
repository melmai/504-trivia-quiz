import unittest
from true_false_question import TrueFalseQuestion


class TrueFalseQuestionTest(unittest.TestCase):
    def setUp(self):
        self.tfq = TrueFalseQuestion.mock()

    def test_get_question(self):
        self.assertEqual(self.tfq.question,
                         "5 is the binary number '10' expressed as a decimal.")

    def test_get_answer(self):
        self.assertEqual(self.tfq.answer, False)

    def test_normalize(self):
        response = "t"
        self.assertEqual(self.tfq.normalize(response), True)

        response = "T"
        self.assertEqual(self.tfq.normalize(response), True)

        response = "TrUe  "
        self.assertEqual(self.tfq.normalize(response), True)

        response = "f"
        self.assertEqual(self.tfq.normalize(response), False)

        response = "FALSE"
        self.assertEqual(self.tfq.normalize(response), False)

        response = "  FalSe"
        self.assertEqual(self.tfq.normalize(response), False)

        response = "thisisnotagoodanswer"  # bad answers
        self.assertEqual(self.tfq.normalize(response), None)

    def test_check_answer(self):
        response = "True"
        self.assertEqual(self.tfq.check_response(response), False)

        response = "t"
        self.assertEqual(self.tfq.check_response(response), False)

        response = "False"
        self.assertEqual(self.tfq.check_response(response), True)

        response = "F"
        self.assertEqual(self.tfq.check_response(response), True)

        response = "nonsense"
        self.assertEqual(self.tfq.check_response(response), None)


if __name__ == "__main__":
    unittest.main()
