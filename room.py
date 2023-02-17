from door import Door


class Room:
    def __init__(self, key_chance):
        self._has_key = self.generate_key(key_chance)
        self._impassable = False
        self._is_exit = False
        self._is_entrance = False
        self._doors = {
            "north": False,
            "east": False,
            "west": False,
            "south": False
        }

    def generate_key(self, key_chance):
        """
        This method determines if the current room contains a key based
        on the likelihood of generating a key object.
        :param key_chance: chance of the room having a key object
        :return: Boolean
        """
        return False

    def transfer_key(self):
        """This method removes the key from the room"""
        pass

    def set_entrance(self):
        """
        This method sets the boolean value of _entrance to True
        :param: None
        :return: None
        """
        self._is_entrance = True

    def set_impassible(self, is_impassable):
        """
        This method sets the boolean value of _impassable
        :parameters: is_impassable
        :return: None
        """
        self._impassable = is_impassable
