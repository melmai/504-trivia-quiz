import unittest
from player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player("Tom")

    def test_player_name_initialization(self):
        self.assertEqual(self.player.name, "Tom")

    def test_check_initial_inventory(self):
        self.assertEqual(self.player.keys, 2)

    def test_add_key(self):
        """
        Tests the add_key() method, which should increment the
        number of keys in the player's inventory.
        """
        # single add
        self.player.add_key()
        self.assertEqual(self.player.keys, 3)

        # multiple add
        self.player.add_key()
        self.player.add_key()
        self.player.add_key()
        self.assertEqual(self.player.keys, 6)

    def test_use_key(self):
        """
        Tests the use_key() method, which should
        decrement the number of keys in the player's inventory.
        """

        self.player.use_key()  # remove 1 key
        self.assertEqual(self.player.keys, 1)

        self.player.use_key()  # should be 0 keys
        self.assertEqual(self.player.keys, 0)

        self.player.use_key()  # should not go below 0
        self.assertEqual(self.player.keys, 0)

    def test_check_inventory(self):
        self.assertEqual(self.player.check_inventory(), 2)
        self.player.use_key()
        self.assertEqual(self.player.check_inventory(), 1)


if __name__ == "__main__":
    unittest.main()
