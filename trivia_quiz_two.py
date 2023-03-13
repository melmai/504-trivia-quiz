from maze import Maze
from player import Player
from user_info import UserInfo


class TriviaQuizTwo:
    def __init__(self, player, level):
        self._game_over = False

        self._player = Player(player)
        self._level = level
        self._difficulty = self._set_difficulty()

        self._maze = Maze(self._difficulty)

    # @property
    # def maze(self):
    #     return self.maze

    def _set_difficulty(self):
        """
        This method gets input from the user to set the difficulty level (1-3)
        of the game.
        :return: Int
        """
        print(self._level)

        if self._level == '1':
            return 4
        elif self._level == '2':
            return 5
        elif self._level == '3':
            return 6

    def user_choice(self, choice):
        """
        Returns the player's next move
        :return: string
        """
        # choice = input("Please enter your next action: ").lower().strip()

        move_commands = ["w", "a", "s", "d"]
        if choice in move_commands:
            has_moved = self._maze.process_move(choice, self._player)

            #  if at exit or can't win, it's all over
            if self._maze.at_exit() or (not has_moved and
                                        not self._player.keys and
                                        not self._maze.is_traversable()):
                self._game_over = True

        # elif choice == '1':
        #     self.save_game(savefile, self._maze, self._player)

        # elif choice == 'o':  # See entire maze for development
        #     self._maze.print_maze()

        elif choice == 'q':  # Auto-quit the game for development
            self._game_over = True

        elif choice == 'g':  # enable god mode
            print("Looks like you have a skeleton key. No door can stop you "
                  "now.")
            self._player.dev = True

        else:
            print(f"Sorry {self._player.name}, that's not a valid command!")


    def main_game_loop(self):
        """
        This method contains the routing and logic for the Trivia Quiz main
        game loop. It will loop until the player
        wins or loses.
        :return: None
        """
        while not self._game_over:
            row, col = self._maze.get_location()
            self._maze.draw_location(row, col)

            if self._maze.get_current_room().key:
                print("You found a key! You'll need it...")
                self._player.add_key()
                self._maze.get_current_room().transfer_key()

            self.user_choice()

        # if self._maze.at_exit():
        #     self._maze.print_maze()
        #     self._info.print_win(self._player.name)
        # else:
        #     self._info.print_loss()

        # choice = input("Play again? (Y/N) ").strip().lower()
        #
        # while choice != 'n' and choice != 'y':
        #     print('Sorry, that is not a valid response! Give it another try.')
        #     choice = input("Play again? (Y/N) ").strip().lower()
        #
        # if choice == 'y':
        #     self._info.print_restart()
        #     new_game = TriviaQuiz()
