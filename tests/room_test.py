import unittest
from room import Room
from door import Door

class RoomTest(unittest.TestCase):

    def test_room_with_key(self):
        room_with_key = Room(100)
        self.assertTrue(room_with_key.key)

    def test_room_without_key(self):
        room_without_key = Room(0)
        self.assertFalse(room_without_key.key)

    def test_set_door(self):
        room = Room(50)
        self.assertEqual(room.get_door("north"), False)
        self.assertEqual(room.get_door("south"), False)
        self.assertEqual(room.get_door("east"), False)
        self.assertEqual(room.get_door("west"), False)

        room.set_door("north")

        self.assertIsInstance(room.get_door("north"), Door)
        self.assertEqual(room.get_door("south"), False)
        self.assertEqual(room.get_door("east"), False)
        self.assertEqual(room.get_door("west"), False)

    def test_unlock_door(self):
        room = Room(50)
        room.set_door("north")
        room.set_active_door("north")
        self.assertTrue(room.active_door.locked)
        room.unlock_door()
        self.assertFalse(room.active_door.locked)


if __name__ == '__main__':
    unittest.main()
