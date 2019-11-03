from tkinter import *
from PIL import ImageTk, Image
import random
import time

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


class Invaders:
    def __init__(self):
        pass

    def load_graphics(self):
        pass

    def create_graphics(self):
        pass

class Defender:
    def __init__(self, canvas, game_data, shoot):
        self.canvas = canvas
        self.game_data = game_data
        self.shoot = shoot

        self.defender = None
        self.id = None
        self.x_move = 0

        # Key binds
        self.canvas.bind_all('<KeyPress-Left>', lambda event, step=-5: self.turn_left(event, step))
        self.canvas.bind_all('<KeyPress-Right>', lambda event, step=5: self.turn_right(event, step))
        self.canvas.bind_all('<space>', lambda event: self.shoot_event(event))

        self.load_graphics()
        self.create_graphics()

    def load_graphics(self):
        raw_image = Image.open("./static/defender_1.png")
        self.defender = ImageTk.PhotoImage(raw_image)

    def create_graphics(self):
        self.id = self.canvas.create_image(self.game_data.get_window_size()['WIDTH']/2 - 15,
                                           self.game_data.get_window_size()['HEIGHT']-50,
                                           image=self.defender, anchor=NW, tag='defender')

    def draw(self):
        pos = self.canvas.coords(self.id)

        # Movement logic.
        if 0 < pos[0] < (self.game_data.get_window_size()['WIDTH'] - 35):
            self.canvas.move(self.id, self.x_move, 0)

        if pos[0] <= 0 and self.x_move > 0:
            self.canvas.move(self.id, self.x_move, 0)

        if pos[0] >= (self.game_data.get_window_size()['WIDTH'] - 35) and self.x_move < 0:
            self.canvas.move(self.id, self.x_move, 0)

        self.x_move = 0

    def turn_left(self, event, step):
        self.x_move = step

    def turn_right(self, event, step):
        self.x_move = step

    def shoot_event(self, event):
        print('SHOOT!')


class Shoot:
    def __init__(self):
        self.x_shoot = 0

    def draw(self):
        pass


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
    shoot = Shoot()
    defender = Defender(game_canvas, game_data, shoot)

    while 1:
        game_app.update_idletasks()
        game_app.update()
        defender.draw()
        time.sleep(0.01)


if __name__ == '__main__':
    main()