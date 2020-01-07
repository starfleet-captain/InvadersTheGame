from tkinter import *
from PIL import ImageTk, Image
import random
import time

from defender import Defender
from shoot import Shoot
from invaders import Invaders


class GameStuff:
    def __init__(self):
        self.current_level = 0
        self.window_size = dict()
        self.game_speed = 0

        self.read_configuration()

    def read_configuration(self):
        self.window_size['WIDTH'] = 700
        self.window_size['HEIGHT'] = 600

    def get_window_size(self):
        return self.window_size


def main():
    game_data = GameStuff()

    game_app = Tk()
    game_app.title("Invaders - The Game")
    game_app.resizable(0, 0)
    game_app.wm_attributes("-topmost", 1)

    game_canvas = Canvas(game_app, width=game_data.get_window_size()['WIDTH'],
                         height=game_data.get_window_size()['HEIGHT'], bd=0, highlightthickness=0, background='black')
    game_canvas.pack()
    game_canvas.update()

    print("Invaders - The Game")
    shoot = Shoot(game_canvas, 1)
    defender = Defender(game_canvas, game_data, shoot)
    invaders = Invaders(game_canvas, shoot, 1, 3)

    # TODO: Change to manage_invaders() with number of current invaders = 1
    invaders.locate_invader()

    while 1:
        game_app.update_idletasks()
        game_app.update()
        defender.draw()
        shoot.draw()
        invaders.manage_invaders()
        time.sleep(0.02)


if __name__ == '__main__':
    main()
