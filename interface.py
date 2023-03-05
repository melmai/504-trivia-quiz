from tkinter import *
from tkinter import ttk
from trivia_quiz import TriviaQuiz

class UserInterface:
    def __init__(self, root):
        # self.quiz = TriviaQuiz()
        self.root = root

        root.title('Trivia Quiz!')
        root.resizable(False, False)
        root.configure(background='#FFFFFF')

        self.style = ttk.Style()
        self.configure_styles()

        self.intro_frame = ttk.Frame(root)
        self.intro_frame.pack()

        # self.intro_art = ttk.Label(self.intro_frame,
        #                   justify = LEFT,
        #                   text = self.quiz.art,
        #                   font=('Courier', 12),
        #                   style='TLabel')

        self.intro = ttk.Label(self.intro_frame,
                          text = "HEY YOU, PLAY THIS GAME "
                                 "[Just kidding, gonna use the cool text Mel wrote]",
                          style='TLabel')

        # self.start_button = ttk.Button(self.frame_intro,
        #                                text='Play Game',
        #                                command=self.play)

        self.intro_art.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10)
        self.intro.grid(row=1, column=1, columnspan=3, padx=10, pady=5)
        # self.start_button.grid(row=2, column=2, padx=20, pady=20)


        self.config_frame = ttk.Frame(root)
        self.entry_name = ttk.Entry(self.config_frame, width=24)
        self.entry_difficulty = ttk.Entry(self.config_frame, width=24)
        self.submit_button = ttk.Button(self.config_frame, text="Submit",
                   command = self.submit)
        self.build_game_config_frame()


        self.game_frame = ttk.Frame(self.root)
        self.game_frame.pack()
        self.placeholder_text = ttk.Label(self.game_frame,
                                          text = "[GAME FRAME PLACEHOLDER]",
                                          style= 'TLabel')
        self.placeholder_text.pack()


    def configure_styles(self):
        self.style.theme_use('classic')
        self.style.configure('TLabel', background='#FFFFFF')
        self.style.configure('TFrame', background='#FFFFFF')
        self.style.configure('TButton', background='#FFFFFF')

    def build_game_config_frame(self):
        self.config_frame.pack()

        ttk.Label(self.config_frame,
                  text = "What is your name adventurer? ").grid(row=0,
                                                                column=0,
                                                                padx=5,
                                                                pady=5,
                                                                sticky='w')
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.config_frame,
                  text = "Please enter a difficulty (level 1-3)  ").grid(row=1,
                                                                         column=0,
                                                                         padx=5,
                                                                         pady=5,
                                                                         sticky='w')
        self.entry_difficulty.grid(row=1, column=1, padx=5, pady=5)


        self.submit_button.grid(row=2,
                                column=0,
                                columnspan=2,
                                padx=10,
                                pady=10)

    def play(self):
        print('PLAY!')
        # self.quiz._create_player()
        # self.quiz._set_difficulty()

    def clear_field(self, field):
        field.delete(0,  'end')

    def disable_field(self, field):
        field.config(state='disabled')

    def submit(self):
        player_name = self.entry_name.get().strip()
        maze_difficulty = self.entry_difficulty.get().strip()

        self.clear_field(self.entry_name)
        self.clear_field(self.entry_difficulty)

        self.disable_field(self.entry_name)
        self.disable_field(self.entry_difficulty)

        self.submit_button.config(state=DISABLED)

        print("name: ", player_name, " | ", "difficulty: ", maze_difficulty)
        return player_name, maze_difficulty


def main():
    root = Tk()
    app = UserInterface(root)
    root.mainloop()

if __name__ == "__main__": main()