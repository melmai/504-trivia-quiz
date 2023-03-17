import trivia_quiz
from maze import Maze
from player import Player
from trivia_quiz import TriviaQuiz
import unittest
import sys

t = TriviaQuiz


class save_test(unittest.TestCase):
    def test_save(self):
        testsave = 'test_save.pickle'
        maze = Maze(2)
        player = Player("testman", keys=15)
        t.save_game(testsave, maze, player)

