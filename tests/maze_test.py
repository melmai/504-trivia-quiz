import unittest
from maze import Maze


class MazeTest(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(5)

    def test_initial_size(self):
        self.assertEqual(self.maze.size, 5)
        self.assertEqual(len(self.maze.rooms), 4)

    def test_entrance_exit_placement(self):
        self.assertEqual(self.maze.entrance, (0,0))
        self.assertEqual(self.maze.exit, (4,4))


if __name__ == '__main__':
    unittest.main()
