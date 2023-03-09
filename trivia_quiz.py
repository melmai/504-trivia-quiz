import textwrap
import time
from maze import Maze
from player import Player
import pickle
import datetime
import sys

savefile = 'save.pkl'

class TriviaQuiz:
    def __init__(self):
        self._game_over = False
        self._win = False

        if self.load_start(savefile):
            self.main_game_loop()

        else:
            # self._print_intro_art()
            # self._print_instructions()
            self._player = self._create_player()
            self._difficulty = self._set_difficulty()
            self._maze = Maze(self._difficulty)
            self.main_game_loop()

    def save_game(self, savefile, maze, player):
        with open(savefile, 'wb') as file:
            pickle.dump({'maze': maze, 'player': player}, file)
            print(f"Game has been saved at {datetime.datetime.now()}")
            sys.exit()

    def load_game(self, savefile):
        try:
            with open(savefile, 'rb') as file:
                game_data = pickle.load(file)
                if game_data is not None:
                    self._maze = game_data['maze']
                    player_data = game_data['player']
                    self._player = Player(player_data._name)
                    self._player._keys = Player(player_data._keys)
                    print(f"Game loaded successfully! Welcome back {self._player._name}")
                    return self._maze
        except FileNotFoundError:
            print(f"No saved game file found")
            return False

    def load_start(self, savefile):
        loading = input("Input 1 if you are starting a new adventure, or input 2 if you are loading....")
        if loading == '1':
            print("Now starting new game.....")
            time.sleep(2)
            return None
        elif loading == '2':
            loaded_data = self.load_game(savefile)
            if loaded_data is None:
                print("No saved game data found..starting new game")
                time.sleep(1)
                return None
            else:
                print("loading game...")
                return loaded_data
        else:
            print("Hmmm...sorry but I dont recognize your input. I'll go ahead and start a new game...")
            time.sleep(2)
            return None


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
        self._print_delayed_text(self.get_menu())

    def get_menu(self):
        return textwrap.dedent("""
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
        player_name = input("What is your name adventurer? ").strip()
        return Player(player_name)

    def _set_difficulty(self):
        """
        This method gets input from the user to set the difficulty level (1-5)
        of the game.
        :return: Int
        """
        while True:
            number = input(
                f"Welcome {self._player._name}. Please enter a difficulty "
                f"level (1-3) ").strip()
            if int(number.isdigit()) and 1 <= int(number) <= 3:
                if number == '1':
                    return 4
                elif number == '2':
                    return 5
                elif number == '3':
                    return 6
            else:
                print("That's not a number between 1-3! Try again!")

    def user_choice(self):
        """
        Returns the player's next move
        :return: string
        """
        choice = input("Please enter your next action: ").lower().strip()

        move_commands = ["w", "a", "s", "d"]
        if choice in move_commands:
            self._maze.process_move(choice, self._player)

            if self._maze.at_exit():
                self._win = True

            if self._maze.at_exit() or (not self._player.keys and
                                        not self._maze.is_traversable()):
                self._game_over = True

        elif choice == 'i':
            self._player.check_inventory()

        elif choice == 'm':
            print(self.get_menu())

        elif choice == 'v':
            self._player.use_vp()
            self.user_choice()

        # TODO: elif choice == '1' # planning to use this for saving
        elif choice == '1':
            self.save_game(savefile, self._maze, self._player)

        elif choice == '5':
            self._maze.print_maze()

        elif choice == 'o':  # See entire maze for development
            self._maze.print_maze()

        elif choice == 'q':  # Auto-quit the game for development
            self._game_over = True

        elif choice == 'p':
            self.use_key()

        # TODO: elif choice == '8675309' # planning to maybe use this as a
        #  cheat to unlock all doors or bypass all
        #  questions for testing?

        else:
            print(f"Sorry {self._player.name}, that's not a valid command!")

    def main_game_loop(self):
        """
        This method contains the routing and logic for the Trivia Quiz main
        game loop. It will loop until the player
        wins or loses.
        :return: None
        """
        # TODO: Check if all the available doors are locked as a game-ending
        #  condition
        while not self._game_over:
            row, col = self._maze.get_location()
            self._maze.draw_location(row, col)

            if self._maze.get_current_room().key:
                print("You found a key! You'll need it...")
                self._player.add_key()
                self._maze.get_current_room().transfer_key()

            self.user_choice()

        if self._win:
            print("*-----------------------------------*")
            print("You've reached the exit and WON THE GAME!")
            self._print_delayed_text("...")
            self._print_delayed_text("...this time...")
            self._print_delayed_text(" ")
            self._maze.print_maze()

            print(f"Okay {self._player.name}, you've done it once. "
                  f"But do you really think you can do it again?")
        else:
            print("Ouch, sorry. Taking that big L.")

        choice = input("Play again? (Y/N) ").strip().lower()

        while choice != 'n' and choice != 'y':
            print('Sorry, that is not a valid response! Give it another try.')
            choice = input("Play again? (Y/N) ").strip().lower()

        if choice == 'y':
            print("alright, let\'s go around again...")
            print("*-----------------------------------*")
            new_game = TriviaQuiz()

    def use_key(self):
        """
        This method unlocks the active door if the Player has keys available.
        :return: True if door unlocks successfully, or False if door was
        already unlocked or player has no keys.
        """
        if self._player.keys:
            active_room = self._maze.get_current_room()
            unlocked = active_room.unlock_door()  # unlocks active door
            if not unlocked:
                print("Hmm the door isn't locked. Lucky me.")
            else:
                self._player.use_key()
            return unlocked
        else:
            print("Whoops, all out of keys! Better try something else...")
        return False


if __name__ == "__main__":
    tq = TriviaQuiz()

