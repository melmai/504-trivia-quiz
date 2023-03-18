import unittest
from maze import Maze
from player import Player
from room import Room


class MazeTest(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(3, test_mode=True)
        self.player = Player('Test')
        self.player.dev = True

    def test_initial_size(self):
        self.assertEqual(self.maze.size, 3)
        self.assertEqual(len(self.maze.rooms), 3)

    def test_entrance_exit_placement(self):
        self.assertEqual(self.maze.entrance, (0, 0))
        self.assertEqual(self.maze.exit, (2, 2))

    def test_get_location(self):
        self.assertEqual(self.maze.get_location(), (0, 0))

    def test_move(self):
        self.maze.process_move('d', self.player)
        self.assertEqual(self.maze.get_location(), (0, 1))

        self.maze.process_move('s', self.player)
        self.assertEqual(self.maze.get_location(), (1, 1))

        self.maze.process_move('w', self.player)
        self.assertEqual(self.maze.get_location(), (0, 1))

        self.maze.process_move('a', self.player)
        self.assertEqual(self.maze.get_location(), (0, 0))

    def test_is_valid_room(self):
        self.assertEqual(self.maze.is_valid_room(1, 1), True)
        self.assertEqual(self.maze.is_valid_room(16, 16), False)
        self.assertEqual(self.maze.is_valid_room(-1, -1), False)
        self.assertEqual(self.maze.is_valid_room(0, 0), True)
        self.assertEqual(self.maze.is_valid_room(2, 2), True)
        self.assertEqual(self.maze.is_valid_room(3, 3), False)

    def test_get_current_room(self):
        self.assertTrue(isinstance(self.maze.get_current_room(), Room))

    def test_is_traversable(self):
        self.assertTrue(self.maze.is_traversable(0, 0))


if __name__ == '__main__':
    unittest.main()
