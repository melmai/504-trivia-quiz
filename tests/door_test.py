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
        self.tfd.check_answer("true")  # should be false
        self.assertEqual(self.tfd.locked, True)
        self.assertEqual(self.tfd.answerable, False)

    def test_correct_answer(self):
        self.tfd.check_answer("false")  # should be false
        self.assertEqual(self.tfd.locked, False)
        self.assertEqual(self.tfd.answerable, False)


if __name__ == '__main__':
    unittest.main()
