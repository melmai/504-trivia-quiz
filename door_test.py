import unittest
from door import Door


class DoorTest(unittest.TestCase):

    def setUp(self):
        self.door = Door()

    def test_create(self):
        self.assertEqual(self.door.locked, True)
        self.assertEqual(self.door.answerable, True)

    def test_wrong_answer(self):
        self.door.get_user_response()




if __name__ == '__main__':
    unittest.main()
