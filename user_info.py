import textwrap
import time


class UserInfo:

    def __init__(self):
        pass

    @staticmethod
    def print_intro_art():
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

    def intro_art(self):
        return textwrap.dedent("""
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

    def print_instructions(self):

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

    def print_menu(self, delayed=False):

        menu = textwrap.dedent("""
        Available Actions
        *-----------------------------------*
        [w] Move Up
        [a] Move Left
        [s] Move Down
        [d] Move Right
        [i] View inventory
        [1] Save game
        [q] Quit

        Press [m] to see your options.
        """)

        if delayed:
            self._print_delayed_text(menu)
        else:
            print(menu)

    def menu(self):
        return textwrap.dedent("""
        Available Actions
        *-----------------------------------*
        [w] Move Up
        [a] Move Left
        [s] Move Down
        [d] Move Right
        [i] View inventory
        [1] Save game
        [q] Quit

        Press [m] to see your options.
        """)

    @staticmethod
    def _print_delayed_text(text, delay=1):
        """
        This method prints a string of text without preceding white space
        after pausing execution for a period of time (default = 1s)
        :param text: String of text to print
        :param delay: Int representing time delay
        """
        time.sleep(delay)
        print(textwrap.dedent(text))

    def print_invalid_command(self, name):
        print(f"Sorry {name}, that's not a valid command!")

    @staticmethod
    def print_invalid_input():
        print('Sorry, that is not a valid response! Give it another try.')

    def print_correct_response(self):
        print("Yas queen")

    def print_incorrect_response(self):
        print("Yikes. Not this time, bud.")

    @staticmethod
    def found_key(skeleton=False):
        if skeleton:
            print("Looks like you have a skeleton key. No door can stop you "
                  "now.")
        else:
            print("You found a key! You'll need it...")

    def print_win(self, name):
        print("*-----------------------------------*")
        print("You've reached the exit and WON THE GAME!")
        self._print_delayed_text("...")
        self._print_delayed_text("...this time...")
        self._print_delayed_text(" ")

        print(f"Okay {name}, you've done it once. "
              f"But do you really think you can do it again?")

    @staticmethod
    def print_loss():
        print("Ouch, sorry. Taking that big L.")

    @staticmethod
    def print_restart():
        print("alright, let's go around again...")
        print("*-----------------------------------*")


