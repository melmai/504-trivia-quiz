from tkinter import *
from tkinter import ttk
from trivia_quiz import TriviaQuiz
from trivia_quiz_two import TriviaQuizTwo
from user_info import UserInfo

class UserInterface:
    def __init__(self, root):
        self.user_info = UserInfo()
        self.quiz = None
        self.root = root
        self.game_window = Toplevel()
        self.game_window.withdraw()

        self.style = ttk.Style()
        self.configure_styles()

        self.intro_frame = ttk.Frame(root)
        self.intro_frame.pack()

        self.intro_art = ttk.Label(self.intro_frame,
                          justify = LEFT,
                          text = self.user_info.intro_art(),
                          style='TLabel')

        self.intro = ttk.Label(self.intro_frame,
                          text = "HEY YOU, PLAY THIS GAME "
                                 "[Just kidding, gonna use the cool text Mel wrote]",
                          style='TLabel')

        self.intro_art.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10)
        self.intro.grid(row=1, column=1, columnspan=3, padx=10, pady=5)


        self.config_frame = ttk.Frame(root)
        self.entry_name = ttk.Entry(self.config_frame, width=24, font=('Courier', 12))
        self.entry_difficulty = ttk.Entry(self.config_frame, width=24, font=('Courier', 12))
        self.submit_button = ttk.Button(self.config_frame, text="Play Game",
                   command = self.play_game, cursor="target")

        self.build_game_config_frame()

        self.user_choice_frame = ttk.Frame(self.game_window)
        self.question_text = ttk.Label(self.user_choice_frame,
                                              text="What now?",
                                              style='TLabel')

        self.key_notify_label = ttk.Label(self.user_choice_frame,
                                          text = "You found a key! You'll need it...",
                                          style = "TLabel")

        self.true_button = ttk.Button(self.user_choice_frame, text="True", command=lambda:self.handle_answer("True"))
        self.false_button = ttk.Button(self.user_choice_frame, text="False")


        self.view_all_button = ttk.Button(self.user_choice_frame, text="View Maze", style="TButton", command=self.view_maze)

        self.game_frame = ttk.Frame(self.game_window)
        self.maze_location = ttk.Label(self.game_frame,
                                          style="Game.TLabel")

        # Direction Buttons
        self.up_button = ttk.Button(self.game_frame, text="⇡", command=self.move_up, style="Game.TButton")
        self.down_button = ttk.Button(self.game_frame, text="⇣", command=self.move_down, style="Game.TButton")
        self.right_button = ttk.Button(self.game_frame, text="⇢", command=self.move_right, style="Game.TButton")
        self.left_button = ttk.Button(self.game_frame, text="⇠", command=self.move_left, style="Game.TButton")

        # Menu and Inventory
        self.save_button = ttk.Button(self.game_frame, text="Save")
        self.inventory = ttk.Label(self.game_frame, text="You have __ keys", style="TLabel")
        self.quit_button = ttk.Button(self.game_frame, text="Quit")

    def set_quiz(self, player, level):
        self.quiz = TriviaQuizTwo(player, level)

    def view_maze(self):
        self.quiz._maze.print_maze()

    def handle_answer(self, response):
        print(response)
        self.game_loop_start()

    def move_up(self):
        self.quiz.user_choice('w')
        self.post_choice_maintenance()

    def move_down(self):
        self.quiz.user_choice('s')
        self.post_choice_maintenance()

    def move_left(self):
        self.quiz.user_choice('a')
        self.post_choice_maintenance()

    def move_right(self):
        self.quiz.user_choice('d')
        self.post_choice_maintenance()

    def post_choice_maintenance(self):
        self.up_button.config(state=DISABLED)
        self.down_button.config(state=DISABLED)
        self.left_button.config(state=DISABLED)
        self.right_button.config(state=DISABLED)

        self.question_text.config(text="The initials JPEG stand for Jagged Point Enabled Graphs")
        self.true_button.grid(row=2, column=1)
        self.false_button.grid(row=2, column=2)


    def configure_styles(self):
        self.style.theme_use('classic')

        self.root.title('Trivia Quiz!')
        self.root.resizable(False, False)
        self.root.configure(background='#000000')

        self.game_window.title('Trivia Quiz!')
        self.game_window.resizable(False, False)
        self.game_window.configure(background='#000000')

        self.style.configure('TLabel', background='#000000', foreground="#f0f14e", font=('Courier', 12))
        self.style.configure('TFrame', background='#000000')
        self.style.configure('TButton', background='#f0f14e', font=('Courier', 12), cursor="target")

        self.style.configure('Game.TLabel', background='#000000', foreground="#f0f14e", font=('Courier', 16), border="white")
        self.style.configure('Game.TButton', background='#f0f14e', font=('Courier', 24), cursor="target")

    def build_game_config_frame(self):
        self.config_frame.pack()

        ttk.Label(self.config_frame,
                  text = "What is your name adventurer? ").grid(row=0,
                                                                column=0,
                                                                padx=5,
                                                                pady=5,
                                                                sticky='w')
        ttk.Label(self.config_frame,
                  text = "Please enter a difficulty (level 1-3)  ").grid(row=1,
                                                                         column=0,
                                                                         padx=5,
                                                                         pady=5,
                                                                         sticky='w')
        self.submit_button.grid(row=2,
                                column=0,
                                columnspan=2,
                                padx=10,
                                pady=10)

        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        self.entry_difficulty.grid(row=1, column=1, padx=5, pady=5)

    def build_main_game_window(self):
        self.game_window.deiconify()
        self.game_window.geometry('500x400')
        self.game_window.rowconfigure(0, weight=1)
        self.game_window.columnconfigure(0, weight=1)

        row, col = self.quiz._maze.get_location()

        self.user_choice_frame.grid(row=0)
        self.game_frame.grid(row=1)

        self.maze_location.configure(text=self.quiz._maze.draw_location(row, col))

        # self.view_all_button.grid(row=0, column=0, pady=10, padx=10, sticky="nw")
        self.question_text.grid(row=1, column=1, columnspan=2, pady=10, padx=10)

        self.up_button.grid(row=3, column=2, padx=10, pady=10)
        self.left_button.grid(row=4, column=1, padx=10, pady=10)
        self.maze_location.grid(row=4, column=2, padx=20, pady=20)
        self.right_button.grid(row=4, column=3, padx=10, pady=10)
        self.down_button.grid(row=5, column=2, padx=10, pady=10)

        self.save_button.grid(row=6, column=0, padx=10, pady=10)
        self.inventory.grid(row=6, column=2, padx=10, pady=10)
        self.quit_button.grid(row=6, column=4, padx=10, pady=10)

    def game_loop_start(self):
        if not self.quiz._game_over:
            self.up_button.config(state=NORMAL)
            self.down_button.config(state=NORMAL)
            self.left_button.config(state=NORMAL)
            self.right_button.config(state=NORMAL)
            self.key_notify_label.grid_forget()

            row, col = self.quiz._maze.get_location()
            self.maze_location.configure(text=self.quiz._maze.draw_location(row, col))

            if self.quiz._maze.get_current_room().key:
                # print("You found a key! You'll need it...")
                self.key_notify_label.grid(row=0, column=1, padx=10, pady=10)
                self.quiz._player.add_key()
                self.quiz._maze.get_current_room().transfer_key()

            # self.quizuser_choice()

    def clear_field(self, field):
        field.delete(0,  'end')

    def disable_field(self, field):
        field.config(state='disabled')

    def clear_and_disable(self, field):
        field.delete(0,  'end')
        field.config(state='disabled')

    def play_game(self):
        player_name = self.entry_name.get().strip()
        maze_level = self.entry_difficulty.get().strip()

        self.clear_and_disable(self.entry_name)
        self.clear_and_disable(self.entry_difficulty)

        self.submit_button.config(state=DISABLED)


        print("name: ", player_name, " | ", "difficulty: ", maze_level)
        # self.quiz = TriviaQuizTwo(player_name, maze_level)
        self.set_quiz(player_name, maze_level)

        self.build_main_game_window()
        self.game_loop_start()

        # return player_name, maze_difficulty




def main():
    root = Tk()
    app = UserInterface(root)
    root.mainloop()

if __name__ == "__main__": main()