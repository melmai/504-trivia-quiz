from maze import Maze
from player import Player
from trivia_quiz import TriviaQuiz
import unittest
import pickle


class SaveTest(unittest.TestCase):

    def setUp(self):
        self.trivia_quiz = TriviaQuiz()
        self.save_file = 'test_save.pickle'

    def test_save(self):
        """This method tests the ability to pickle a maze and player """
        maze = Maze(2)
        player = Player("testman", keys=15)
        self.trivia_quiz.__save_game(self.save_file, maze, player)

    def test_load(self):
        """This method tests the ability to load a game and that the attributes
        are correct """

        with open(self.save_file, 'rb') as f:
            save_data = pickle.load(f)

        expected_size = 2
        expected_name = "testman"
        expected_keys = 15
        self.assertEqual(save_data['maze'].size, expected_size)
        self.assertEqual(save_data['player'].name, expected_name)
        self.assertEqual(save_data['player'].keys, expected_keys)
