import unittest
from door import Door


class DoorTest(unittest.TestCase):

    def setUp(self):
        self.tfd = Door.mock("TrueFalse")
        self.mcd = Door.mock("MultipleChoice")
        self.sad = Door.mock("ShortAnswer")

    def test_create_door(self):
        # true/false
        self.assertEqual(self.tfd.locked, True)
        self.assertEqual(self.tfd.answerable, True)

        # multiple choice
        self.assertEqual(self.mcd.locked, True)
        self.assertEqual(self.mcd.answerable, True)

        # short answer
        self.assertEqual(self.sad.locked, True)
        self.assertEqual(self.sad.answerable, True)

    def test_wrong_answer(self):
        # true/false
        self.tfd.check_answer("true")  # should be false
        self.assertEqual(self.tfd.locked, True)
        self.assertEqual(self.tfd.answerable, False)

        # multiple choice
        self.mcd.check_answer("humerus")
        self.assertEqual(self.mcd.locked, True)
        self.assertEqual(self.mcd.answerable, False)

        # short answer
        self.sad.check_answer("straight")
        self.assertEqual(self.sad.locked, True)
        self.assertEqual(self.sad.answerable, False)

    def test_correct_answer(self):
        # true/false
        self.tfd.check_answer("false")  # false
        self.assertEqual(self.tfd.locked, False)
        self.assertEqual(self.tfd.answerable, False)

        # multiple choice
        self.mcd.check_answer("femur")  # femur
        self.assertEqual(self.mcd.locked, False)
        self.assertEqual(self.mcd.answerable, False)

        # short answer
        self.sad.check_answer("diagonally")  # diagonally
        self.assertEqual(self.sad.locked, False)
        self.assertEqual(self.sad.answerable, False)


if __name__ == '__main__':
    unittest.main()
