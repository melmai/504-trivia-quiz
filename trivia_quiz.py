import time
import textwrap
from save_game import save_game
from maze import Maze
from player import Player


class TriviaQuiz:
    def __init__(self):
        # self._print_intro_art()
        # self._print_instructions()
        self._player = self._create_player()
        self._difficulty = self._set_difficulty()

        self._maze = Maze(self._difficulty)
        # self._game_over = False

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
        player_name = input("What is your name adventurer? ")



        return Player(player_name)

    def _set_difficulty(self):
        """
        This method gets input from the user to set the difficulty level (1-5)
        of the game.
        :return: Int
        """
        while True:
            number = input(f"Welcome {self._player._name}. Please enter a difficulty level (1-5) ")
            if int(number.isdigit()) and 1 <= int(number) <= 5:
                return number
            else:
                print("That's not a number between 1-5! Try again!")

    def check_win(self):
        """
        This method checks to see if the player is located in the exit room.
        :return: Boolean
        """

        return self.maze._location == self.maze._exit

    def user_choice(self):
        """
        Returns the player's next move
        :return: string
        """
        choice = input("Please enter your next action: ")
        final_choice = choice.lower()
        if final_choice == 'w':
            self.player.move('north')

        elif final_choice == 'a':
            self.player.move('west')

        elif final_choice == 's':
            self.player.move('south')

        elif final_choice == 'd':
            self.player.move('east')

        elif final_choice == 'i':
            self.player.check_inventory()

        # elif choice.lower() == 'm' # this is for available options

        elif choice.lower() == '1':
            save_game()


        # elif choice.lower() == '8675309' # planning to maybe use this as a cheat to unlock all doors or bypass all
        # questions for testing?

        else:
            print(f"Sorry {self._player._name}, that's not a valid command!")



if __name__ == "__main__":
    tq = TriviaQuiz()

