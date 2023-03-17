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
        This method gets input from the user to determine if the game should be generated or loaded
        :return: String
        """
        return input(
            "Input [1] if you are starting a new adventure, or input [2] if "
            "you are loading....")


