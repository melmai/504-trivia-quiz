from door import Door
from user_info import UserInfo
from user_input import UserInput
import random


class Room:
    def __init__(self, row, col):
        self.__impassable = False
        self.__visited = False
        self.__row = row
        self.__col = col
        self.__is_exit = False
        self.__is_entrance = False
        self.__has_key = self.__generate_key()
        self.__doors = {
            "north": False,
            "east": False,
            "west": False,
            "south": False
        }
        self.__active_door = None

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col

    @property
    def key(self):
        return self.__has_key

    @key.setter
    def key(self, has_key):
        self.__has_key = has_key

    @property
    def active_door(self):
        return self.__active_door

    @property
    def entrance(self):
        return self.__is_entrance

    @entrance.setter
    def entrance(self, is_entrance):
        self.__is_entrance = is_entrance

    @property
    def exit(self):
        return self.__is_exit

    @exit.setter
    def exit(self, is_exit):
        self.__is_exit = is_exit

    def __generate_key(self):
        """
        This method determines if the current room contains a key based
        on the likelihood of generating a key object.
        :return: Boolean
        """
        key_chance = random.randint(1, 100)
        if not self.entrance and not self.exit:
            return key_chance >= 90
        else:
            return False

    def transfer_key(self):
        """This method removes the key from the room"""
        self.__has_key = False

    def __str__(self):
        """
        This method creates a room string that can be printed to represent
        the room
        :param: Tuple of available doors
        :return: String
        """

        if self.__is_exit:
            content = "🏁"
        elif self.__is_entrance:
            content = "🎬"
        elif self.__has_key:
            content = "🗝"
        else:
            content = "  "

        room_str = ""

        if self.__doors["north"]:
            room_str += "*   *\n"
        else:
            room_str += "* * *\n"

        if self.__doors["east"] and self.__doors["west"]:
            room_str += f"  {content} \n"
        elif not self.__doors["east"] and self.__doors["west"]:
            room_str += f"  {content}*\n"
        elif self.__doors["east"] and not self.__doors["west"]:
            room_str += f"* {content} \n"
        else:
            room_str += f"* {content}*\n"

        if self.__doors["south"]:
            room_str += "*   *\n"
        else:
            room_str += "* * *\n"

        return room_str

    def get_door(self, direction):
        """
        This method gets the door that is positioned at the specified direction
        :param direction: String that represents the door position in the room
        :return: Door object or False if no door exists
        """
        return self.__doors[direction]

    def set_door(self, direction, door=None):
        """
        This method adds a door at the specified direction
        :param direction: String that represents the door position in the room
        :param door: Door object to add.
        """
        door = door if door else Door()
        self.__doors[direction] = door
        return door

    def set_active_door(self, direction):
        """
        This method sets focus on an existing door of the room
        :param direction: string representing door to activate
        """
        self.__active_door = self.__doors[direction]

    def unlock_door(self):
        """
        This method unlocks the active door if it is locked
        :return: True if successfully unlocks the door or False if already
        unlocked
        """
        if self.__active_door.locked:
            self.__active_door.unlock()
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
        door = self.__doors[direction]

        if door and player.dev:  # god mode, move if possible
            return True
        elif door:  # there's a door
            self.__active_door = door
            is_locked, is_answerable = door.try_door()

            # it's not locked, ok to move player
            if not is_locked:
                can_move = True

            # can't answer anymore but keys are available
            elif not is_answerable and player.keys:
                use_key = UserInput.yes_or_no("key")

                # player wants to use a key
                if use_key == "y":
                    player.use_key()
                    self.unlock_door()
                    can_move = True
                else:
                    UserInfo.decline_key()

            elif player.keys == 0:
                UserInfo.no_key()

            self.__active_door = None

        else:  # no door
            UserInfo.no_door()

        return can_move  # can't move this direction


if __name__ == "__main__":
    Room(2, 2)
