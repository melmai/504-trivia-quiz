import unittest
from multiple_choice_question import MultipleChoiceQuestion


class MultipleChoiceQuestionTest(unittest.TestCase):

    def setUp(self):
        self.mcq = MultipleChoiceQuestion.mock()

    def test_normalize(self):
        response = "femur"
        self.assertEqual(self.mcq.normalize(response), "femur")

        response = "FEMUR"
        self.assertEqual(self.mcq.normalize(response), "femur")

        response = "  Femur"
        self.assertEqual(self.mcq.normalize(response), "femur")

        response = "f"
        self.assertNotEqual(self.mcq.normalize(response), "femur")

        response = "feemr"
        self.assertNotEqual(self.mcq.normalize(response), "femur")

    def test_check_response(self):
        response = "femur"
        self.assertEqual(self.mcq.check_response(response), True)

        response = "tibia"
        self.assertEqual(self.mcq.check_response(response), False)

        response = "feemur"
        self.assertEqual(self.mcq.check_response(response), False)


if __name__ == '__main__':
    unittest.main()
