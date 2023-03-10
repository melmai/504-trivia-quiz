import random

from door import Door
import random


class Room:
    def __init__(self, row, col):
        self._impassable = False
        self._visited = False
        self._row = row
        self._col = col
        self._is_exit = False
        self._is_entrance = False
        self._has_key = self.generate_key(random.randint(1, 100))
        self._doors = {
            "north": False,
            "east": False,
            "west": False,
            "south": False
        }
        self._active_door = None

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def key(self):
        return self._has_key

    @property
    def active_door(self):
        return self._active_door

    @property
    def exit(self):
        return self._is_exit

    def generate_key(self, key_chance):
        """
        This method determines if the current room contains a key based
        on the likelihood of generating a key object.
        :param key_chance: chance of the room having a key object
        :return: Boolean
        """
        if self.can_move_to() and not self._is_entrance and not self._is_exit:
            return key_chance >= 95
        else:
            return False

    def transfer_key(self):
        """This method removes the key from the room"""
        self._has_key = False

    def __str__(self):
        return self.construct_room_string()

    def construct_room_string(self):
        """
        This method creates a room string that can be printed to represent the room
        :param: Tuple of available doors
        :return: String
        """

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
            room_str += "*   *\n"
        else:
            room_str += "* * *\n"

        if self._doors["east"] and self._doors["west"]:
            room_str += f"  {content} \n"
        elif not self._doors["east"] and self._doors["west"]:
            room_str += f"  {content}*\n"
        elif self._doors["east"] and not self._doors["west"]:
            room_str += f"* {content} \n"
        else:
            room_str += f"* {content}*\n"

        if self._doors["south"]:
            room_str += "*   *\n"
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
        This method returns a boolean that signifies if the room can be entered
        :param: None
        :return: Boolean
        """
        return not self._impassable and not self._visited

    def get_door(self, direction):
        """
        This method gets the door that is positioned at the specified direction
        :param direction: String that represents the door position in the room
        :return: Door object or False if no door exists
        """
        return self._doors[direction]

    def set_door(self, direction, door=None):
        """
        This method adds a door at the specified direction
        :param direction: String that represents the door position in the room
        :param door: Door object to add.
        """
        door = door if door else Door()
        self._doors[direction] = door
        return door

    def set_active_door(self, direction):
        """
        This method sets focus on an existing door of the room
        :param direction: string representing door to activate
        """
        self._active_door = self._doors[direction]

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

    def try_move(self, direction, player):
        """
        This method activates the door, if exists, that corresponds to the
        passage selected by the player and allows the player to use a key if
        the question is answered incorrectly
        :param direction: string representing direction of desired movement
        :param player: the player object
        :return: True if player is free to move, else False
        """
        can_move = False
        door = self._doors[direction]

        if door and player.dev:
            return True

        if door:  # there's a door
            self._active_door = door
            is_locked, is_answerable = door.try_door()

            if not is_locked:
                can_move = True
            elif not is_answerable and player.keys:
                use_key = input("Care to use a key? (Y/N)\n")
                use_key = use_key.lower().strip()

                if use_key == "y":
                    player.use_key()
                    self.unlock_door()
                    can_move = True

            elif player.keys == 0:
                print("Uh oh, the way is blocked and there are no keys at my "
                      "disposal.")

            self._active_door = None

        return can_move  # can't move this direction

    def has_answerable_door(self, direction):
        return self._doors[direction] and self._doors[direction].answerable
