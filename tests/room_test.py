import unittest
from room import Room
from door import Door


class RoomTest(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 1)
        self.room.key = True

    def test_set_door(self):
        self.assertEqual(self.room.get_door("north"), False)
        self.assertEqual(self.room.get_door("south"), False)
        self.assertEqual(self.room.get_door("east"), False)
        self.assertEqual(self.room.get_door("west"), False)

        self.room.set_door("north")

        self.assertIsInstance(self.room.get_door("north"), Door)
        self.assertEqual(self.room.get_door("south"), False)
        self.assertEqual(self.room.get_door("east"), False)
        self.assertEqual(self.room.get_door("west"), False)

    def test_unlock_door(self):
        self.room.set_door("north")
        self.room.set_active_door("north")
        self.assertTrue(self.room.active_door.locked)
        self.room.unlock_door()
        self.assertFalse(self.room.active_door.locked)

    def test_transfer_key(self):
        self.room.key = True
        self.assertTrue(self.room.key)
        self.room.transfer_key()
        self.assertFalse(self.room.key)

    def test_get_door(self):
        self.assertFalse(self.room.get_door("south"))
        self.room.set_door("south")
        self.assertIsInstance(self.room.get_door("south"), Door)


if __name__ == '__main__':
    unittest.main()
