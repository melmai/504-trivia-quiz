import textwrap
import datetime
import time


class UserInfo:

    @staticmethod
    def intro_art():
        """This method prints out the art that displays on new game
        instantiation."""
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
    def intro_text():
        """
        This method prints flavor text for the user at the start of the game
        """
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
    def menu():
        """
        Prints out the available actions for the player during the game loop
        """
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
        """
        Prints feedback for user when their input is not valid
        """
        print('Sorry, that is not a valid response! Give it another try.')

    @staticmethod
    def correct():
        """
        Prints feedback for user when their input is correct
        """
        print("Yas queen")

    @staticmethod
    def incorrect():
        """
        Prints feedback for user when their input is not correct
        """
        print("Yikes. Not this time, bud.")

    @staticmethod
    def no_door():
        """
        Prints feedback for user when there is no door to interact with in
        their chosen direction
        """
        print("Don't think I can move through walls...")

    @staticmethod
    def retry():
        """
        Prints feedback for user when they attempt a door that is unanswerable
        """
        print("This place is familiar. Have I been here before?")

    @staticmethod
    def found_key(skeleton=False):
        """
        Prints feedback for user when they pick up a key in the maze
        :param skeleton: boolean representing singular or persistent access
        """
        if skeleton:
            print("Looks like I have a skeleton key. No door can stop me "
                  "now.")
        else:
            print("Ooh a key! I'll need it...")

    @staticmethod
    def decline_key():
        """
        Prints feedback for user when they decline to use a key
        """
        print("Guess I'll have to find another way.")

    @staticmethod
    def no_key():
        """
        Prints feedback for user when they exhaust their key supply
        """
        print("Uh oh, the way is blocked and there are no keys at my "
              "disposal.")

    @staticmethod
    def win(name):
        """
        Prints feedback for user when they have won the game
        """
        print("*-----------------------------------*")
        print("You've reached the exit and WON THE GAME!")
        UserInfo.delay_text("...")
        UserInfo.delay_text("...this time...")
        UserInfo.delay_text(" ")

        print(f"Okay {name}, you've done it once. "
              f"But do you really think you can do it again?")

    @staticmethod
    def lose():
        """
        Prints feedback for user when they have lost the game
        """
        print("Ouch. Taking that big L.")

    @staticmethod
    def restart():
        """
        Prints feedback for user when the user decides to restart the game
        """
        print("Alright, let's go around again...")
        print("*-----------------------------------*")

    @staticmethod
    def quit():
        """
        Prints feedback for user when they opt to quit the game
        """
        print("Had enough, huh?")

    @staticmethod
    def saved():
        """
        Prints feedback for user when their save is successful
        """
        print(f"Game has been saved at {datetime.datetime.now()}")
        print(textwrap.dedent(
            """

                ⣀⣠⠤⠶⠖⠒⠒⠲⠶⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⢀⡴⠋⠁⠀⣀⣤⠤⠴⠶⠦⠤⣄⡀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣟⣀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠳⢤⡀⠹⡆⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⢀⡤⠞⠋⠉⠉⠉⠙⠲⣤⡀⠀⣠⡾⠋⠉⠁⠀⠀⠈⠙⢦⠀⠀⠀⠀⠀
            ⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀
            ⠀⢸⠁⠀⠀⢠⣄⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⢰⣶⠀⠀⠀⠀⢸⡇⠀⠀⠀
            ⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀
            ⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀
            ⠀⠀⠀⣳⢦⣀⣀⠀⣀⣠⠴⡞⠁⠀⠈⠓⠶⢤⣤⣤⡤⠶⠞⠋⣤⠀⠀⠀⠀
            ⠀⠀⠀⠘⠦⣄⣉⣉⣩⡆⢸⠃⠀⢀⡶⠀⠀⢠⣄⣀⣀⣀⣤⠞⠁⠀⠀⠀⠀
            ⠀⢀⣠⠤⢶⡶⠮⠍⠀⠀⢸⠀⢀⡼⠁⠀⠀⠀⠀⠉⠉⠁⠀⠐⠲⣄⡀⠀⠀
            ⢠⠞⢁⡴⠚⢩⢐⡤⢄⣀⠈⠳⠞⠁⠀⣀⢤⠖⢲⠯⡭⠋⠉⠛⠲⢎⠻⣦⠀
            ⡿⠀⡏⠀⠀⠈⠉⢻⣄⢼⠉⠁⡖⠒⣿⣀⡼⠓⠋⠀⠀⠀⠀⠀⠀⠈⢧⠘⡇
            ⢿⠀⣇⠀⠀⠀⠀⠀⠀⠈⠳⠚⠙⠚⠁⠈⣤⠶⠛⠛⠛⠲⣤⡀⠀⠀⢸⠀⡇
            ⠈⢧⡈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠒⠲⠦⣄⠀⠈⢳⡄⢀⡾⣠⠃
            ⠀⠈⠛⢦⣙⢲⣖⢲⣠⢤⣠⠴⣄⡠⢤⢀⣤⡀⣰⢶⣼⠳⣄⣠⠶⠋⣰⠋⠀
            ⠀⠀⠀⠀⠙⠳⢮⣿⣓⡦⠿⣤⣼⣇⣈⣛⣀⣙⣧⣤⠽⠚⠋⣥⠴⠛⠁⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """
        ))

    @staticmethod
    def start_game(tried_loading=False, invalid=False):
        """
        Prints feedback for user when they are starting/restarting the game
        :param tried_loading:
        :param invalid:
        """
        if not tried_loading:
            UserInfo.delay_text("Now starting new game.....", 2)

        elif invalid:
            UserInfo.delay_text("Hmmm..sorry but I dont recognize your input. "
                                "I'll go ahead and start a new game ;)...", 2)

        else:
            UserInfo.delay_text("No saved game data found..starting new game")

    @staticmethod
    def loading():
        """
        This method prints feedback during game load
        """
        print("loading game...")

    @staticmethod
    def loaded(name, keys):
        """
        This method prints feedback when game has successfully loaded
        :param name: player name
        :param keys: number of keys available
        :return:
        """
        print(
            f"Game loaded successfully! Welcome back "
            f"{name}. You have {keys} keys available!")

    @staticmethod
    def game_not_found():
        """
        This method prints feedback when save file is unavailable
        """
        print(f"No saved game file found")

    @staticmethod
    def inventory(keys):
        """
        This method prints the key count of the player
        :param keys: int
        """
        if not keys:
            inventory = "Sorry, no keys available!"
        elif keys == 1:
            inventory = "Ah, still have 1 key available. Better use it wisely."
        else:
            inventory = f"Phew. Still have {keys} keys in your pocket."

        print(inventory)
