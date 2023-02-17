import random
from room import Room


class Maze:
    def __init__(self, size):
        self._size = size
        self._rooms: []
        self._entrance = (0, 0)
        self._exit = (size, size)
        self._location = (0, 0)

        self.create_maze()

    def move(self):
        """
        This method updates the location of the player in the maze
        """
        pass

    def create_maze(self):
        """
        This method builds a 2D array of room objects
        :return:
        """
        for row in range(0, self._size):
            # self._rooms.append([Room(10) for col in range(0, self._size)]) # Just putting a key-chance of 10 for now
            pass

        for row in range(0, self._size):
            for col in range(0, self._size):
                impassable_chance = random.randint(1, 100)

                if impassable_chance > 80: # % chance a room is impassable
                    # self._rooms[row][col].set_impassible(True)
                    pass


# Below lines for local tests
# m = Maze(3)