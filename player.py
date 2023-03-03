class Player:
    def __init__(self, name):
        self._name = name
        self._keys = 2

    @property
    def name(self):
        return self._name

    @property
    def keys(self):
        return self._keys

    def add_key(self):
        """This method increments the number of keys in the inventory."""
        self._keys += 1

    def use_key(self):
        """This method decrements the number of keys in the inventory."""
        if self._keys != 0:  # never go below 0
            self._keys -= 1

    def check_inventory(self):
        if not self._keys:
            inventory = "Sorry, no keys available!"
        elif self._keys == 1:
            inventory = "Ah, still have 1 key available. Better use it wisely."
        else:
            inventory = f"Phew. Still have {self._keys} keys in your pocket."

        print(inventory)
        return self._keys
