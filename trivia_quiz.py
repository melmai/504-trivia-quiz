from maze import Maze
from player import Player
import pickle
from user_info import UserInfo
from user_input import UserInput


class TriviaQuiz:
    def __init__(self):
        self.__game_over = False
        self.__quit = False
        self.__save_file = 'save.pkl'

        if not self.load_start(self.__save_file):
            # UserInfo.intro_art()
            # UserInfo.intro_text()
            self.__player = self.__create_player()
            self.__difficulty = self._set_difficulty()
            self.__maze = Maze(self.__difficulty)
            UserInfo.menu()

        self.main_game_loop()

    @staticmethod
    def save_game(save_file, maze, player):
        """
        This method is used for saving a game by converting the python objects
        into a byte stream to store in save_file
        :param save_file: file to store game data
        :param maze: the current maze instance
        :param player: the current player instance
        :return: None
        """
        with open(save_file, 'wb') as file:
            pickle.dump({'maze': maze, 'player': player}, file)
            UserInfo.saved()
            UserInfo.quit()

    def load_game(self, save_file):
        """
        This method is used for loading a game by converting the byte stream
        stored in save_file into python objects for playing the game
        :param save_file: the file to load
        :return: None
        """

        try:
            with open(save_file, 'rb') as file:
                game_data = pickle.load(file)
                if game_data is not None:
                    self.__maze = game_data['maze']
                    player_data = game_data['player']
                    self.__player = Player(player_data.name)
                    self.__player.keys = player_data.keys
                    UserInfo.loaded(self.__player.name, self.__player.keys)
                    return self.__maze
        except FileNotFoundError:
            UserInfo.game_not_found()
            return False

    def load_start(self, save_file):
        """
        This method presents the user, at the beginning of the game, to start a
        new game or continue from a load file.
        :param save_file: the file with game data stored
        """
        loading = UserInput.load()

        if loading == '1':  # new game
            UserInfo.start_game()
            return None

        elif loading == '2':  # load game
            loaded_data = self.load_game(save_file)

            if loaded_data is None:  # oops, no load file
                UserInfo.start_game(True)
                return None

            else:
                UserInfo.loading()
                return loaded_data

        else:
            UserInfo.start_game(False, True)
            return None

    @staticmethod
    def __create_player():
        """
        This method gets input from the user to create a Player object.
        :return: Player object
        """
        return Player(UserInput.name())

    def _set_difficulty(self):
        """
        This method gets input from the user to set the difficulty level (1-5)
        of the game.
        :return: Int
        """
        number = UserInput.difficulty(self.__player.name)

        if number == 1:
            return 4
        elif number == 2:
            return 5
        elif number == '3':
            return 6

    def user_choice(self):
        """
        Returns the player's next move
        :return: string
        """
        choice = UserInput.command()

        move_commands = ["w", "a", "s", "d"]
        if choice in move_commands:
            has_moved = self.__maze.process_move(choice, self.__player)

            #  if at exit or can't win, it's all over
            if self.__maze.at_exit() or (not has_moved and
                                         not self.__player.keys and
                                         not self.__maze.is_traversable()):
                self.__game_over = True

        elif choice == 'i':
            self.__player.check_inventory()

        elif choice == 'm':
            UserInfo.menu()

        elif choice == '1':
            self.save_game(self.__save_file, self.__maze, self.__player)

        elif choice == 'o':  # See entire maze for development
            self.__maze.print_maze()

        elif choice == 'q':  # Auto-quit the game for development
            self.__game_over = True
            self.__quit = True

        elif choice == 'g':  # enable god mode
            UserInfo.found_key(True)
            self.__player.dev = True

    def main_game_loop(self):
        """
        This method contains the routing and logic for the Trivia Quiz main
        game loop. It will loop until the player
        wins or loses.
        :return: None
        """

        while not self.__game_over:
            row, col = self.__maze.get_location()
            self.__maze.draw_location(row, col)

            if self.__maze.get_current_room().key:
                UserInfo.found_key()
                self.__player.add_key()
                self.__maze.get_current_room().transfer_key()

            self.user_choice()

        if self.__maze.at_exit():  # win
            self.__maze.print_maze()
            UserInfo.win(self.__player.name)

        elif self.__quit:  # quit
            UserInfo.quit()

        else:  # lose
            UserInfo.lose()

        choice = UserInput.yes_or_no("replay")

        if choice == 'y':
            UserInfo.restart()
            TriviaQuiz()


if __name__ == "__main__":
    TriviaQuiz()
