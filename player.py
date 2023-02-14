class Player:
    def __init__(self, name):
        self._name = name
        self._keys = 2

    def move(self, row, col):
        """
        This method updates the location of the player in the maze.
        :param row: row to move to
        :param col: column to move to
        :return: None
        """
        pass

    def add_key(self):
        """This method increments the number of keys in the inventory."""
        pass

    def use_key(self):
        """This method decrements the number of keys in the inventory."""
        pass
