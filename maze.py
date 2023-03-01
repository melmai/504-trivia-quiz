import random
from room import Room


class Maze:
    def __init__(self, size):
        self._size = size
        self._rooms = []
        self._entrance = (0, 0)
        self._exit = (size-1, size-1)
        self._location = (0, 0)

        self.create_maze()
        self.validate_maze()

    def get_location(self):
        """
        This method returns the current room location coordinates as a tuple of row, col
        :return: Tuple
        """
        return self._location

    def move(self, x, y):
        """
        This method updates the location of the player in the maze
        :return: Boolean of whether the player successfully moved to the desired location
        """
        valid_move = False
        row, col = self._location
        can_move_north, can_move_south, can_move_west, can_move_east = self.show_all_possible_directions(row, col)

        if (x > 0 and can_move_east) or (x < 0 and can_move_west):
            col += x
            valid_move = True

        if (y > 0 and can_move_south) or (y < 0 and can_move_north):
            row += y
            valid_move = True

        self._location = (row, col)
        return valid_move

    def create_maze(self):
        """
        This method builds a 2D array of room objects
        :return:
        """
        for row in range(0, self._size):
            self._rooms.append([Room(random.randint(1, 100)) for col in range(0, self._size)])

        for row in range(0, self._size):
            for col in range(0, self._size):
                impassable_chance = random.randint(1, 100)

                if impassable_chance > 73:  # % chance a room is impassable
                    self._rooms[row][col].set_impassable(True)

        # set entrance and exit
        self._rooms[0][0].set_entrance()
        self._rooms[0][0].set_impassable(False)
        self._rooms[self._size - 1][self._size - 1].set_exit()
        self._rooms[self._size - 1][self._size - 1].set_impassable(False)

    def is_traversable(self, row, col):
        """
        This method determines whether or not a given maze is traversable when starting at a particular row/col coordinate
        :param: row, col
        :return: boolean
        """
        found_exit = False

        if self.is_valid_room(row, col):
            self._rooms[row][col].set_visited(True)

            if self._rooms[row][col].get_is_exit():
                return True

            # If not an exit, traverse to the adjacent rooms and check again
            found_exit = self.is_traversable(row + 1, col)  # south
            if not found_exit:
                found_exit = self.is_traversable(row, col + 1)  # east
            if not found_exit:
                found_exit = self.is_traversable(row - 1, col)  # north
            if not found_exit:
                found_exit = self.is_traversable(row, col - 1)  # west

            if not found_exit:
                self._rooms[row][col].set_visited(True)
        else:
            return False

        return found_exit

    def validate_maze(self):
        if self.is_traversable(0, 0):
            self._generate_doors()
            return True
        else:
            self._rooms = []
            self.create_maze()
            self.validate_maze()

    def _generate_doors(self):
        """
        This method generates door objects that represent the passageways
        between rooms of the maze
        :return: True if successful, or false if fails
        """
        for row in range(0, self._size):
            for col in range(0, self._size):
                n, s, w, e = self.show_all_possible_directions(row, col)
                current_room = self._rooms[row][col]

                if n:
                    door = self._rooms[row - 1][col].get_door("south")
                    current_room.set_door("north", door)

                if s:
                    current_room.set_door("south")

                if e:
                    current_room.set_door("east")

                if w:
                    door = self._rooms[row][col - 1].get_door("east")
                    current_room.set_door("west", door)

    def is_valid_room(self, row, col):
        """
        This method determines whether or not a given room by coordinates is in bounds and can be entered
        :param: row, col
        :return: boolean
        """
        return 0 <= row < self._size and col >= 0 and col < self._size and self._rooms[row][col].can_enter()

    def print_maze(self):
        """
        This method prints out the entire maze in string representation and utilizes some helper methods
        :param: None
        :return: None
        """
        room_list = []
        for row in range(0, self._size):
            for col in range(0, self._size):
                doors = self.show_all_possible_directions(row, col)
                room_list.append(self._rooms[row][col].construct_room_string(doors))
            self.format_strings(room_list)
            room_list = []

    def format_strings(self, rooms):
        """
        This method takes a list of string Room components to be printed out in rows and columns
        :param: rooms
        :return: None
        """
        split_list = []

        for room in rooms:
            if room is not None:
                split_list.append(room.split("\n"))

        for layer in range(3):
            for room_pieces in split_list:
                print(room_pieces[layer], end=" ")
            print("")

    def draw_location(self, row, col):
        """
        This method draws the current room location of the player in the maze
        :param row:
        :param col:
        :return:
        """
        doors = self.show_all_possible_directions(row, col)
        print(self._rooms[row][col].construct_room_string(doors))

    def show_all_possible_directions(self, x, y):
        """
        This method returns the possible directions of movement for the player
        :param x:
        :param y:
        :return: Tuple
        """
        can_move_north = (0 <= x - 1 < self._size) and self._rooms[x - 1][y] is not None and self._rooms[x - 1][y].can_move_to()
        can_move_south = (0 <= x + 1 < self._size) and self._rooms[x + 1][y] is not None and self._rooms[x + 1][y].can_move_to()
        can_move_west = (0 <= y - 1 < self._size) and self._rooms[x][y - 1] is not None and self._rooms[x][y - 1].can_move_to()
        can_move_east = (0 <= y + 1 < self._size) and self._rooms[x][y + 1] is not None and self._rooms[x][y + 1].can_move_to()
        return can_move_north, can_move_south, can_move_west, can_move_east

    def get_current_room(self):
        """
        This method returns the current location of the Player
        :return: Room
        """
        x, y = self._location
        return self._rooms[x][y]


if __name__ == "__main__":
    maze = Maze(3)
