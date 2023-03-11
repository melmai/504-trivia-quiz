from maze import Maze
from player import Player
from user_info import UserInfo


class TriviaQuizTwo:
    def __init__(self, player, difficulty):
        self._game_over = False
        # self._info = UserInfo()

        self._player = player
        self._difficulty = difficulty

        self._maze = Maze(self._difficulty)
