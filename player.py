
class Player:
    def __init__(self, name, savefile=None):
        self.__name = name
        self.__dev = False
        self.__keys = 2
        if savefile is not None:
            self.__name = ['._name']
            self.__keys = ['._keys']

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
        if not self.__keys:
            inventory = "Sorry, no keys available!"
        elif self.__keys == 1:
            inventory = "Ah, still have 1 key available. Better use it wisely."
        else:
            inventory = f"Phew. Still have {self.__keys} keys in your pocket."

        print(inventory)
        return self.__keys
