import time
import textwrap
from maze import Maze
from player import Player


class TriviaQuiz:
    def __init__(self):
        # self._print_intro_art()
        # self._print_instructions()
        self._player = self._create_player()
        self._difficulty = self._set_difficulty()
        self._maze = Maze(self._difficulty)
        self._game_over = False

    def _print_intro_art(self):
        """This method introduces the rules and instructions for the player."""
        print("""
        \\                           /
         \\                         /
          \\                       /
           ]                     [    ,'|
           ]                     [   /  |
           ]___               ___[ ,'   |
           ]  ]\\             /[  [ |:   |
           ]  ] \\           / [  [ |:   |
           ]  ]  ]         [  [  [ |:   |
           ]  ]  ]__     __[  [  [ |:   |
           ]  ]  ] ]\\ _ /[ [  [  [ |:   |
           ]  ]  ] ] (#) [ [  [  [ :===='
           ]  ]  ]_].nHn.[_[  [  [
           ]  ]  ]  HHHHH. [  [  [
           ]  ] /   `HH("N  \\ [  [
           ]__]/     HHH  "  \\[__[
           ]         NNN         [
           ]         N/"         [
           ]         N H         [
          /          N            \\
         /           q,            \\
        /                           \\
        """)

    def _print_instructions(self):
        print("You wake up in a cold, dark room...")
        self._print_delayed_text("Your head hurts. Everything is unfamiliar. "
                                 "What is this place?")
        self._print_delayed_text("There's something in your pocket.")
        self._print_delayed_text("Keys? What are these for?")
        self._print_delayed_text("You see a light...")
        self._print_delayed_text("It's getting brighter.")
        self._print_delayed_text("Oh god, it's blinding!")
        self._print_delayed_text("Wh- what *is* this madness?!")
        self._print_delayed_text("...")
        self._print_delayed_text("...")
        self._print_delayed_text("Welcome to Trivia Quiz!")
        self._print_delayed_text("It's a trap. It's a game! It's a game-trap!")
        self._print_delayed_text("""
        In order to leave this prison of fun, you must find your way to 
        the exit. Pick a locked door and answer a question to unlock it. Don't 
        worry, they are *all* locked. You know, for maximal FUN!
        """)
        self._print_delayed_text("""
        Those keys you found will help you on your way to the exit. They 
        will unlock any door you find, even if you already answered a 
        question incorrectly. There are more keys to find as you make your 
        way through the rooms, but don't rely on them too much!
        """, 2)
        self._print_delayed_text("""
        Well OK then. Now you know what your mission is. How do you want to 
        proceed?
        """, 2)
        self._print_delayed_text("""
        Available Actions
        *-----------------------------------*
        W - Move Up
        A - Move Left
        S - Move Down
        D - Move Right
        I - View inventory
        
        Press M to see your available options at any time.
        """)

    def _print_delayed_text(self, text, delay=1):
        """
        This method prints a string of text without preceding white space
        after pausing execution for a period of time (default = 1s)
        :param text: String of text to print
        :param delay: Int representing time delay
        """
        time.sleep(delay)
        print(textwrap.dedent(text))

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
        return 4 # Just setting this as 4 for now, will need changed to accept player input

    def check_win(self):
        """
        This method checks to see if the player is located in the exit room.
        :return: Boolean
        """
        pass

    def main_game_loop(self):
        """
        This method contains the routing and logic for the Trivia Quiz game loop
        :return: None
        """
        # Loop until Player wins or loses
        while not self._game_over:
            # Show Current Room
            row, col = self._maze.get_location()
            self._maze.draw_location(row, col)

            # Accept Player Action
            # If key == w, a, s, d: call move(x,y)
                # ~~~ Do the Question Routing ~~~
                # If move is True: Continue onward to the next iteration of the loop!
                # If move is False: bounce back, get new input
            # If key == i: show inventory
            # If key == m: show key options
            # If key == k (or something else we decide): call print_maze()

            # Check Game Status
            # If check_win is True OR if there are no viable directions to move,
            #   update self.game_over to True to end the game loop


if __name__ == "__main__":
    tq = TriviaQuiz()