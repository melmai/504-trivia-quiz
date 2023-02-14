from maze import Maze
from player import Player


class TriviaQuiz:
    def __init__(self):
        self.print_instructions()
        self._player = self._create_player()
        self._difficulty = self._set_difficulty()
        self._maze = Maze(self._difficulty)
        self._game_over = False

    def print_instructions(self):
        """This method introduces the rules and instructions for the player."""
        pass

    def _create_player(self):
        """
        This method gets input from the user to create a Player object.
        :return: Player object
        """
        return Player("Test")

    def _set_difficulty(self):
        """
        This method gets input from the user to set the difficulty level (1-5)
        of the game.
        :return: Int
        """
        return 0

    def check_win(self):
        """
        This method checks to see if the player is located in the exit room.
        :return: Boolean
        """
        pass
