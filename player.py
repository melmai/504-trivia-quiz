from user_info import UserInfo


class Player:
    def __init__(self, name, keys=2):
        self.__name = name
        self.__dev = False
        self.__keys = keys

    @property
    def name(self):
        return self.__name

    @property
    def dev(self):
        return self.__dev

    @dev.setter
    def dev(self, is_dev):
        self.__dev = is_dev

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, count):
        self.__keys = count

    def add_key(self):
        """This method increments the number of keys in the inventory."""
        self.__keys += 1

    def use_key(self):
        """This method decrements the number of keys in the inventory."""
        if self.__keys != 0:  # never go below 0
            self.__keys -= 1

    def check_inventory(self):
        UserInfo.inventory(self.__keys)
        return self.__keys
