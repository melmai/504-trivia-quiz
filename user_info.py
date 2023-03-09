import textwrap
import time

class UserInfo:

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
        self._print_delayed_text("""
        Well OK then. Now you know what your mission is. How do you want to 
        proceed?
        """, 2)

    def print_menu(self, delayed=False):

        menu = textwrap.dedent("""
        Available Actions
        *-----------------------------------*
        W - Move Up
        A - Move Left
        S - Move Down
        D - Move Right
        I - View inventory

        Press M to see your available options at any time.
        """)

        if delayed:
            self._print_delayed_text(menu)
        else:
            print(menu)

    def _print_delayed_text(self, text, delay=1):
        """
        This method prints a string of text without preceding white space
        after pausing execution for a period of time (default = 1s)
        :param text: String of text to print
        :param delay: Int representing time delay
        """
        time.sleep(delay)
        print(textwrap.dedent(text))

    def print_win(self, name):
        print("*-----------------------------------*")
        print("You've reached the exit and WON THE GAME!")
        self._print_delayed_text("...")
        self._print_delayed_text("...this time...")
        self._print_delayed_text(" ")

        print(f"Okay {name}, you've done it once. "
              f"But do you really think you can do it again?")

    def print_loss():
        print("Ouch, sorry. Taking that big L.")

    def print_restart(self):
        print("alright, let's go around again...")
        print("*-----------------------------------*")
