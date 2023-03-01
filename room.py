from door import Door


class Room:
    def __init__(self, key_chance):
        self._impassable = False
        self._visited = False

        self._has_key = self.generate_key(key_chance)
        self._is_exit = False
        self._is_entrance = False
        self._doors = {
            "north": False,
            "east": False,
            "west": False,
            "south": False
        }
        self._active_door = None

    def generate_key(self, key_chance):
        """
        This method determines if the current room contains a key based
        on the likelihood of generating a key object.
        :param key_chance: chance of the room having a key object
        :return: Boolean
        """
        if self.can_move_to():
            return key_chance >= 95
        else:
            return False

    def transfer_key(self):
        """This method removes the key from the room"""
        pass

    def construct_room_string(self, doors):
        """
        This method creates a room string that can be printed to represent the room
        :param: Tuple of available doors
        :return: String
        """
        self._doors["north"], self._doors["south"], self._doors["west"], self._doors["east"] = doors

        if self._is_exit:
            content = "🏁"
        elif self._is_entrance:
            content = "🎬"
        elif self._has_key:
            content = "🗝"
        else:
            content = "  "

        room_str = ""

        if self._doors["north"]:
            room_str += "* - *\n"
        else:
            room_str += "* * *\n"

        if self._doors["east"] and self._doors["west"]:
            room_str += f"| {content}|\n"
        elif not self._doors["east"] and self._doors["west"]:
            room_str += f"| {content}*\n"
        elif self._doors["east"] and not self._doors["west"]:
            room_str += f"* {content}|\n"
        else:
            room_str += f"* {content}*\n"

        if self._doors["south"]:
            room_str += "* - *\n"
        else:
            room_str += "* * *\n"

        return room_str

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

    def can_move_to(self):
        """
        This method gets the boolean value of _impassable and returns the opposite to show
        if the room can be moved into by the player
        :param: None
        :return: Boolean
        """
        return not self._impassable

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

    def get_door(self, direction):
        """
        This method gets the door that is positioned at the specified direction
        :param direction: String that represents the door position in the room
        :return: Door object or False if no door exists
        """
        return self._doors[direction]

    def set_door(self, direction, door=Door()):
        """
        This method adds a door at the specified direction
        :param direction: String that represents the door position in the room
        :param door: Door object to add. If none provided, a new door is
        generated
        """
        self._doors[direction] = door

    def unlock_door(self):
        """
        This method unlocks the active door if it is locked
        :return: True if successfully unlocks the door or False if already
        unlocked
        """
        if self._active_door.locked:
            self._active_door.unlock()
            return True
        return False
