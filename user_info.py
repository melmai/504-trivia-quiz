import textwrap
import datetime
import time


class UserInfo:

    def __init__(self):
        pass

    @staticmethod
    def intro_art():
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

    @staticmethod
    def instructions(self):

        print("You wake up in a cold, dark room...")

        UserInfo.delay_text("Your head hurts. Everything is unfamiliar. "
                            "What is this place?")

        UserInfo.delay_text("There's something in your pocket.")

        UserInfo.delay_text("Keys? What are these for?")
        UserInfo.delay_text("You see a light...")
        UserInfo.delay_text("It's getting brighter.")
        UserInfo.delay_text("Oh god, it's blinding!")
        UserInfo.delay_text("Wh- what *is* this madness?!")
        UserInfo.delay_text("...")
        UserInfo.delay_text("...")
        UserInfo.delay_text("Welcome to Trivia Quiz!")
        UserInfo.delay_text("It's a trap. It's a game! It's a game-trap!")
        UserInfo.delay_text("""
        In order to leave this prison of fun, you must find your way to 
        the exit. Pick a locked door and answer a question to unlock it. Don't 
        worry, they are *all* locked. You know, for maximal FUN!
        """)
        UserInfo.delay_text("""
        Those keys you found will help you on your way to the exit. They 
        will unlock any door you find, even if you already answered a 
        question incorrectly. There are more keys to find as you make your 
        way through the rooms, but don't rely on them too much!
        """, 2)

    @staticmethod
    def menu(delayed=False):

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
            UserInfo.delay_text(menu)
        else:
            print(menu)

    @staticmethod
    def delay_text(text, delay=1):
        """
        This method prints a string of text without preceding white space
        after pausing execution for a period of time (default = 1s)
        :param text: String of text to print
        :param delay: Int representing time delay
        """
        time.sleep(delay)
        print(textwrap.dedent(text))

    @staticmethod
    def invalid():
        print('Sorry, that is not a valid response! Give it another try.')

    @staticmethod
    def correct():
        print("Yas queen")

    @staticmethod
    def incorrect():
        print("Yikes. Not this time, bud.")

    @staticmethod
    def no_door():
        print("Don't think you can move through walls...")

    @staticmethod
    def found_key(skeleton=False):
        if skeleton:
            print("Looks like you have a skeleton key. No door can stop you "
                  "now.")
        else:
            print("You found a key! You'll need it...")

    @staticmethod
    def win(name):
        print("*-----------------------------------*")
        print("You've reached the exit and WON THE GAME!")
        UserInfo.delay_text("...")
        UserInfo.delay_text("...this time...")
        UserInfo.delay_text(" ")

        print(f"Okay {name}, you've done it once. "
              f"But do you really think you can do it again?")

    @staticmethod
    def lose():
        print("Ouch, sorry. Taking that big L.")

    @staticmethod
    def restart():
        print("alright, let's go around again...")
        print("*-----------------------------------*")

    @staticmethod
    def quit():
        print("Had enough, huh?")

    @staticmethod
    def saved():
        print(f"Game has been saved at {datetime.datetime.now()}")
        print("""

            ┈┈┈┈┈┈▕▔╲
            ┈┈┈┈┈┈┈▏▕
            ┈┈┈┈┈┈┈▏▕▂▂▂
            ▂▂▂▂▂▂╱┈▕▂▂▂▏
            ▉▉▉▉▉┈┈┈▕▂▂▂▏
            ▉▉▉▉▉┈┈┈▕▂▂▂▏
            ▔▔▔▔▔▔╲▂▕▂▂▂""")

    @staticmethod
    def start_game(tried_loading=False, invalid=False):
        if not tried_loading:
            UserInfo.delay_text("Now starting new game.....", 2)
        elif invalid:
            UserInfo.delay_text("Hmmm...sorry but I dont recognize your input. I'll go ahead "
                "and start a new game ;)...", 2)
        else:
            UserInfo.delay_text("No saved game data found..starting new game")

    @staticmethod
    def loading():
        print("loading game...")

    @staticmethod
    def loaded(name, keys):
        print(
            f"Game loaded successfully! Welcome back "
            f"{name}. You have {keys} keys available!")

    @staticmethod
    def game_not_found():
        print(f"No saved game file found")

