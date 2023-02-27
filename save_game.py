import pickle
import datetime
import maze
import player

game_data = {
    'maze': maze,
    'player': player

}


def save_game(savefile):
    with open(savefile, 'wb') as file:
        pickle.dump(game_data, file)
    print(f"Game has been saved at {datetime.datetime}")


def load_game(savefile):
    try:
        with open(savefile, 'rb') as file:
            game_data = pickle.load(file)
            return game_data
    except FileNotFoundError:
        print(f"No saved game file found with name {file}")
