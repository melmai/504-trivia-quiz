from user_info import UserInfo


class UserInput:

    @staticmethod
    def name():
        """
        This method gets input from the user to create a Player object.
        :return: String for player name
        """
        return input("But first, tell me... what is your name, "
                     "adventurer? ").strip()

    @staticmethod
    def load():
        """
        This method gets input from the user to determine if the game should be
        generated or loaded
        :return: String
        """
        valid_commands = ["1", "2"]

        command = None
        while command not in valid_commands:
            command = input(
                "Input [1] if you are starting a new adventure, or input [2] "
                "if you are loading....").lower().strip()

            if command not in valid_commands:
                UserInfo.invalid()

        return command

    @staticmethod
    def difficulty(name):
        """
        This method gets input from the user to set the difficulty of the game.
        :return: int
        """

        number = 0
        while not isinstance(number, int) or not (0 < number < 4):
            number = input(
                f"Welcome {name}. Please enter a difficulty level (1-3) "
                f"").strip()

            try:
                number = int(number)
            except ValueError:
                number = 0

            if not (0 < number < 4):
                UserInfo.invalid()

        return number

    @staticmethod
    def command():
        """
        Gets input from the player during the game loop and checks for validity
        :return: String representing a valid command
        """
        valid_commands = ["w", "a", "s", "d", "i", "m", "1", "o", "g", "q"]

        command = None
        while command not in valid_commands:
            command = input("Please enter your next action: ").lower().strip()

            if command not in valid_commands:
                UserInfo.invalid()

        return command

    @staticmethod
    def yes_or_no(prompt):
        """
        Gets input from the player for a yes/no question and checks for
        validity
        :param prompt: String representing the prompt type
        :return: String representing a valid command
        """
        if prompt == "replay":
            text = "Play again? (Y/N)\n"
        elif prompt == "key":
            text = "Care to use a key? (Y/N)\n"

        valid_commands = ["n", "y"]

        command = None
        while command not in valid_commands:
            command = input(text).lower().strip()

            if command not in valid_commands:
                UserInfo.invalid()

        return command

    @staticmethod
    def answer(question):
        """
        This method presents the player with a question and waits
        for an answer from the player
        :return: String
        """
        return input(str(question) + '\n')



