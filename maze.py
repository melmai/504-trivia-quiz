import random
from room import Room


class Maze:
    def __init__(self, size):
        self._size = size
        self._rooms = []
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
            self._rooms.append([Room(10) for col in range(0, self._size)]) # Just putting a key-chance of 10 for now


        for row in range(0, self._size):
            for col in range(0, self._size):
                impassible_chance = random.randint(1, 100)

                if impassible_chance > 80: # % chance a room is impassable
                    self._rooms[row][col].set_impassible(True)

        # set entrance and exit
        self._rooms[0][0].set_entrance()
        self._rooms[0][0].set_impassible(False)
        self._rooms[self._size - 1][self._size - 1].set_exit()
        self._rooms[self._size - 1][self._size - 1].set_impassible(False)


    def is_traversable(self, row, col):
        """
        This method determines whether or not a given maze is traversable when starting at a particular row/col coordinate
        :param: row, col
        :return: boolean
        """
        pass


    def is_valid_room(self, row, col):
        """
        This method determines whether or not a given room by coordinates is in bounds and can be entered
        :param: row, col
        :return: boolean
        """
        pass
        # return 0 <= row < self._size and col >= 0 and col < self._size and self._rooms[row][col].can_enter()


# Below lines for local tests
m = Maze(3)