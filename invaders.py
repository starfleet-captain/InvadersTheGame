from tkinter import *
import random
import time

game_app = Tk()
game_app.title("Invaders - The Game")
game_app.resizable(0, 0)
game_app.wm_attributes("-topmost", 1)

game_canvas = Canvas(game_app, width=700, height=600, bd=0, highlightthickness=0, background='black')
game_canvas.pack()
game_canvas.update()

class GameStuff:
    def __init__(self):
        self.current_level = 0
        self.window_size = dict()
        self.game_speed = 0

    def read_configuration(self):
        pass


class Invaders:
    def __init__(self):
        pass

    def load_graphics(self):
        pass

    def create_graphics(self):
        pass

class Defender:
    def __init__(self):
        pass

    def load_graphics(self):
        pass

    def create_graphics(self):
        pass


def main():
    print("Invaders - The Game")

    while 1:
        game_app.update_idletasks()
        game_app.update()


if __name__ == '__main__':
    main()