import time
from maze import Maze
from player import Player
import pickle
import datetime
import sys
from user_info import UserInfo

savefile = 'save.pkl'


class TriviaQuiz:
    def __init__(self):
        self.__game_over = False
        self.__info = UserInfo()

        if not self.load_start(savefile):
            # self._info.print_intro_art()
            # self._info.print_instructions()
            self.__player = self.__create_player()
            self.__difficulty = self._set_difficulty()
            self.__maze = Maze(self.__difficulty)
            self.__info.print_menu()

        self.main_game_loop()

    def save_game(self, savefile, maze, player):
        with open(savefile, 'wb') as file:
            pickle.dump({'maze': maze, 'player': player}, file)
            print(f"Game has been saved at {datetime.datetime.now()}")
            sys.exit()

    def load_game(self, savefile):
        try:
            with open(savefile, 'rb') as file:
                game_data = pickle.load(file)
                if game_data is not None:
                    self.__maze = game_data['maze']
                    player_data = game_data['player']
                    self.__player = Player(player_data.name)
                    self.__player.keys = player_data.keys
                    print(
                        f"Game loaded successfully! Welcome back, "
                        f"{self.__player.name}")
                    return self.__maze
        except FileNotFoundError:
            print(f"No saved game file found")
            return False

    def load_start(self, savefile):
        loading = input(
            "Input 1 if you are starting a new adventure, or input 2 if you "
            "are loading....")
        if loading == '1':
            print("Now starting new game.....")
            time.sleep(2)
            return None
        elif loading == '2':
            loaded_data = self.load_game(savefile)
            if loaded_data is None:
                print("No saved game data found..starting new game")
                time.sleep(1)
                return None
            else:
                print("loading game...")
                return loaded_data
        else:
            print(
                "Hmmm...sorry but I dont recognize your input. I'll go ahead "
                "and start a new game...")
            time.sleep(2)
            return None

    def __create_player(self):
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
            self.__info.print_menu()

        elif choice == '1':
            self.save_game(savefile, self.__maze, self.__player)

        elif choice == 'o':  # See entire maze for development
            self.__maze.print_maze()

        elif choice == 'q':  # Auto-quit the game for development
            self.__game_over = True

        elif choice == 'g':  # enable god mode
            print("Looks like you have a skeleton key. No door can stop you "
                  "now.")
            self.__player.dev = True

        else:
            print(f"Sorry {self.__player.name}, that's not a valid command!")

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
                print("You found a key! You'll need it...")
                self.__player.add_key()
                self.__maze.get_current_room().transfer_key()

            self.user_choice()

        if self.__maze.at_exit():
            self.__maze.print_maze()
            self.__info.print_win(self.__player.name)
        else:
            self.__info.print_loss()

        choice = input("Play again? (Y/N) ").strip().lower()

        while choice != 'n' and choice != 'y':
            print('Sorry, that is not a valid response! Give it another try.')
            choice = input("Play again? (Y/N) ").strip().lower()

        if choice == 'y':
            self.__info.print_restart()
            TriviaQuiz()


if __name__ == "__main__":
    TriviaQuiz()
