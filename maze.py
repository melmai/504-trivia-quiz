from room import Room


class Maze:
    def __init__(self, size):
        self._size = size
        self._rooms: []
        self._entrance = (0, 0)
        self._exit = (size, size)
        self._location = (0, 0)

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
        pass
