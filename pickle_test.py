import trivia_quiz
from maze import Maze
from player import Player
from trivia_quiz import TriviaQuiz
import unittest
import sys
import pickle
t = TriviaQuiz

testsave = 'test_save.pickle'
class save_test(unittest.TestCase):
    def test_save(self):
        """This method tests the ability to pickle a maze and player """
        testsave = 'test_save.pickle'
        maze = Maze(2)
        player = Player("testman", keys=15)
        t.save_game(testsave, maze, player)

    def test_load(self):
        """This method tests the ability to load a game and that the attributes are correct """

        testsave = 'test_save.pickle'
        with open (testsave, 'rb') as f:
            save_data = pickle.load(f)

        expected_size = 2
        expected_name = "testman"
        expected_keys = 15
        self.assertEqual(save_data['maze'].size, expected_size)
        self.assertEqual(save_data['player'].name, expected_name)
        self.assertEqual(save_data['player'].keys, expected_keys)

