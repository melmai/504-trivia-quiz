import unittest
from door import Door


class DoorTest(unittest.TestCase):

    def setUp(self):
        self.door = Door()

    def test_create(self):
        self.assertEqual(self.door.locked, True)
        self.assertEqual(self.door.answerable, True)

    def test_wrong_answer(self):
        self.door.check_answer("true")  # should be false
        self.assertEqual(self.door.locked, True)
        self.assertEqual(self.door.answerable, False)

    def test_correct_answer(self):
        self.door.check_answer("false")  # should be false
        self.assertEqual(self.door.locked, False)
        self.assertEqual(self.door.answerable, False)


if __name__ == '__main__':
    unittest.main()
