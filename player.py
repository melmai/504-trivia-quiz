from maze import Maze

class Player:
    def __init__(self, name):
        self._name = name
        self._keys = 2
        self._location = (0, 0)
        self._maze = Maze(20)

    @property
    def keys(self):
        return self._keys

    def move(self, direction):
        """
        This method updates the location of the player in the maze.
        :param row: row to move to
        :param col: column to move to
        :return: None
        """
        x, y = self._location

        new_x, new_y = x, y

        if direction == 'north':
            new_x = x - 1
        elif direction == 'south':
            new_x = x + 1

        elif direction == 'east':
            new_y = y + 1
        elif direction == 'west':
            new_y = y - 1
        else:
            print("invalid movement")

        if self._maze.is_valid_room(new_x, new_y):
            self._location = new_x, new_y
        elif not self._maze.is_valid_room(new_x, new_y):
            print("You can't go that way!")

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

    def show_location(self):
        """This method returns the position of the player."""
        return self._location
