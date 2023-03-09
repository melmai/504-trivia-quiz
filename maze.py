import random
from room import Room
import pickle


class Maze:
    def __init__(self, size, savefile=None):
        self._size = size
        self._rooms = []
        self._entrance = (0, 0)
        self._exit = (size - 1, size - 1)
        self._location = (0, 0)

        self.create_maze_2()
        # self.create_maze()
        # self.validate_maze()
        self.print_maze()

    def at_exit(self):
        """
        This method determines if the player has reached the exit
        :return: True if currently located at exit cell, else False
        """
        return self._location == self._exit

    def get_location(self):
        """
        This method returns the current room location coordinates as a tuple
        of row, col
        :return: Tuple
        """
        return self._location

    def process_move(self, direction, player):
        """
        This method handles the Player's move request and checks to see if
        they are able to move in the specified direction before changing
        location.
        """
        has_moved = False

        directions = {
            "w": "north",
            "a": "west",
            "s": "south",
            "d": "east"
        }

        current_room = self.get_current_room()
        can_move = current_room.try_move(directions[direction], player)
        if can_move:
            self.move(direction)

    def move(self, direction):
        """
        This method updates the location of the Player
        :param direction: string representing direction of movement
        """
        movement = {
            "w": (0, -1),
            "a": (-1, 0),
            "s": (0, 1),
            "d": (1, 0)
        }

        row, col = self._location
        col += movement[direction][0]
        row += movement[direction][1]
        self._location = (row, col)

    def create_maze(self):
        """
        This method builds a 2D array of room objects
        :return:
        """
        for row in range(0, self._size):
            self._rooms.append(
                [Room(random.randint(1, 100)) for col in range(0, self._size)])

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

    def create_maze_2(self):
        for row in range(self._size):
            self._rooms.append([])
            for col in range(self._size):
                self._rooms[-1].append(Room(row, col))

        start = self.get_current_room()

        stack = [start]
        visited = [start]

        while stack:
            current = stack[-1]
            neighbors = self._get_neighbors(current, visited)

            if neighbors:
                neighbor = random.choice(neighbors)
                stack.append(neighbor)
                visited.append(neighbor)
                self._create_doors(current, neighbor)
            else:
                stack.pop()

    def _create_doors(self, current, neighbor):
        neighbor_dir = {
            "east": "west",
            "west": "east",
            "north": "south",
            "south": "north"
        }

        if neighbor.col > current.col:
            current_dir = "east"
        elif neighbor.col < current.col:
            current_dir = "west"
        elif neighbor.row > current.row:
            current_dir = "south"
        else:
            current_dir = "north"

        door = current.set_door(current_dir)
        neighbor.set_door(neighbor_dir[current_dir], door)

    def _get_neighbors(self, current, visited):
        row = current.row
        col = current.col
        end = self._size - 1
        current_neighbors = []

        # Room or false
        north_room = self.get_room(row - 1, col)
        south_room = self.get_room(row + 1, col)
        west_room = self.get_room(row, col - 1)
        east_room = self.get_room(row, col + 1)

        if row > 0 and north_room not in visited:
            current_neighbors.append(north_room)
        if row < end and south_room not in visited:
            current_neighbors.append(south_room)
        if col > 0 and west_room not in visited:
            current_neighbors.append(west_room)
        if col < end and east_room not in visited:
            current_neighbors.append(east_room)
        return current_neighbors

    def get_room(self, row, col):
        if 0 <= row < self._size and 0 <= col < self._size:
            return self._rooms[row][col]

    def is_traversable(self, row=None, col=None, visited_rooms=[]):
        """
        This method determines if a given maze is traversable when starting
        at a particular row/col coordinate
        :param: row, col
        :return: boolean
        """
        found_exit = False
        visited = visited_rooms
        if not row:
            row = self._location[0]

        if not col:
            col = self._location[1]

        current_room = self._rooms[row][col]

        if current_room and current_room not in visited:
            visited.append(current_room)

            if current_room.exit:
                return True

            # If not an exit, traverse to the adjacent rooms and check again
            if current_room.has_answerable_door("south"):
                found_exit = self.is_traversable(row + 1, col, visited)  #
                # south

            if not found_exit and current_room.has_answerable_door("east"):
                found_exit = self.is_traversable(row, col + 1, visited)  # east

            if not found_exit and current_room.has_answerable_door("north"):
                found_exit = self.is_traversable(row - 1, col, visited)  # north

            if not found_exit and current_room.has_answerable_door("west"):
                found_exit = self.is_traversable(row, col - 1, visited)  # west

        return found_exit

    def validate_maze(self):
        if self.is_traversable(0, 0):
            self.print_maze()
            self._generate_doors()
            return True
        else:
            self._rooms = []
            self.create_maze()
            self.validate_maze()

    def load_maze(self, savefile):
        with open(savefile, 'rb') as file:
            maze_data = pickle.load(file)
            self._rooms = maze_data['rooms']
            self._entrance = maze_data['entrance']
            self._exit = maze_data['exit']
            self._location = maze_data["location"]

    def is_valid_room(self, row, col):
        """
        This method determines if a given room by coordinates is
        in bounds and can be entered
        :param: row, col
        :return: boolean
        """
        return 0 <= row < self._size and 0 <= col < self._size

    def print_maze(self):
        """
        This method prints out the entire maze in string representation and
        utilizes some helper methods
        """
        room_list = []
        for row in range(0, self._size):
            for col in range(0, self._size):
                doors = self.show_all_possible_directions(row, col)
                room_list.append(
                    self._rooms[row][col].construct_room_string())
            self.format_strings(room_list)
            room_list = []

    def format_strings(self, rooms):
        """
        This method takes a list of string Room components to be printed out
        in rows and columns
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
        print(self._rooms[row][col])

    def show_all_possible_directions(self, x, y):
        """
        This method returns the possible directions of movement for the player
        :param x:
        :param y:
        :return: Tuple
        """

        can_move_north = (0 <= x - 1 < self._size) and self._rooms[x - 1][
            y] is not None and self._rooms[x - 1][y].can_move_to()
        can_move_south = (0 <= x + 1 < self._size) and self._rooms[x + 1][
            y] is not None and self._rooms[x + 1][y].can_move_to()
        can_move_west = (0 <= y - 1 < self._size) and self._rooms[x][
            y - 1] is not None and self._rooms[x][y - 1].can_move_to()
        can_move_east = (0 <= y + 1 < self._size) and self._rooms[x][
            y + 1] is not None and self._rooms[x][y + 1].can_move_to()
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
