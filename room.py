from door import Door


class Room:
    def __init__(self, key_chance):
        self._has_key = self.generate_key(key_chance)
        self._is_exit = False
        self._is_entrance = False
        self._doors = {
            "north": False,
            "east": False,
            "west": False,
            "south": False
        }

        self._impassable = False
        self._visited = False

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
        This method sets the boolean value of _is_entrance to True
        :param: None
        :return: None
        """
        self._is_entrance = True

    def get_is_exit(self):
        """
        This method returns the boolean value of the _is_exit attribute
        :param: None
        :return: Boolean
        """
        return self._is_exit

    def set_exit(self):
        """
        This method sets the boolean value of _is_exit to True
        :param: None
        :return: None
        """
        self._is_exit = True

    def set_impassable(self, is_impassable):
        """
        This method sets the boolean value of _impassable
        :param: is_impassable
        :return: None
        """
        self._impassable = is_impassable

    def set_visited(self, visited):
        """
        This method sets the boolean value of _visited
        :param: visited
        :return: None
        """
        self._visited = visited

    def can_enter(self):
        """
        This methods returns a boolean that signifies if the room can be entered
        :param:
        :return:
        """
        return not self._impassable and not self._visited