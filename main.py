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
        self.in_game = True

        self.read_configuration()

    def read_configuration(self):
        self.window_size['WIDTH'] = 700
        self.window_size['HEIGHT'] = 600

    def get_window_size(self):
        return self.window_size

    def update_score(self, canvas, score, level):
        score_label = canvas.find_withtag("score")
        canvas.delete(score_label)
        canvas.create_text(5, 580, text="SCORE: {}, LEVEL: {}".format(score, level), font="Arial, 11", fill="gray",
                           tag="score", anchor=NW)


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
    invaders = Invaders(game_canvas, game_data, shoot, 8, 4)

    invaders.set_invaders(number_of_invaders=5)

    while game_data.in_game:
        game_app.update_idletasks()
        game_app.update()
        defender.draw()
        shoot.draw()
        invaders.manage_invaders()
        game_data.update_score(game_canvas, invaders.get_score(), invaders.get_level())
        time.sleep(0.02)

    while 1:
        game_app.update_idletasks()
        game_app.update()
        game_canvas.create_text(game_data.window_size['WIDTH'] / 2, 250, text="GAME OVER", font="Arial, 35",
                                  fill="red", anchor=CENTER)


if __name__ == '__main__':
    main()
