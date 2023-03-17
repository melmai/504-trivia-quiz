import time
from maze import Maze
from player import Player
import pickle
import sys
from user_info import UserInfo

savefile = 'save.pkl'


class TriviaQuiz:
    def __init__(self):
        self.__game_over = False
        self.__quit = False

        if not self.load_start(savefile):
            # UserInfo.intro_art()
            # UserInfo.instructions()
            self.__player = self.__create_player()
            self.__difficulty = self._set_difficulty()
            self.__maze = Maze(self.__difficulty)
            UserInfo.menu()

        self.main_game_loop()

    @staticmethod
    def save_game(save_file, maze, player):
        with open(save_file, 'wb') as file:
            pickle.dump({'maze': maze, 'player': player}, file)
            UserInfo.saved()
            sys.exit()

    def load_game(self, save_file):
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

    def load_start(self, savefile):
        loading = input(
            "Input 1 if you are starting a new adventure, or input 2 if you "
            "are loading....")
        if loading == '1':
            UserInfo.start_game()
            return None
        elif loading == '2':
            loaded_data = self.load_game(savefile)
            if loaded_data is None:
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
        player_name = input("But first, tell me... what is your name, "
                            "adventurer? "
                            "").strip()
        return Player(player_name)

    def _set_difficulty(self):
        """
        This method gets input from the user to set the difficulty level (1-5)
        of the game.
        :return: Int
        """
        while True:
            number = input(
                f"Welcome {self.__player.name}. Please enter a difficulty "
                f"level (1-3) ").strip()
            if int(number.isdigit()) and 1 <= int(number) <= 3:
                if number == '1':
                    return 4
                elif number == '2':
                    return 5
                elif number == '3':
                    return 6
            else:
                print("That's not a number between 1-3! Try again!")

    def user_choice(self):
        """
        Returns the player's next move
        :return: string
        """
        choice = input("Please enter your next action: ").lower().strip()

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
            self.save_game(savefile, self.__maze, self.__player)

        elif choice == 'o':  # See entire maze for development
            self.__maze.print_maze()

        elif choice == 'q':  # Auto-quit the game for development
            self.__game_over = True
            self.__quit = True

        elif choice == 'g':  # enable god mode
            UserInfo.found_key(True)
            self.__player.dev = True

        else:
            UserInfo.invalid()

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

        choice = input("Play again? (Y/N) ").strip().lower()

        while choice != 'n' and choice != 'y':
            UserInfo.invalid()
            choice = input("Play again? (Y/N) ").strip().lower()

        if choice == 'y':
            UserInfo.restart()
            TriviaQuiz()


if __name__ == "__main__":
    TriviaQuiz()
