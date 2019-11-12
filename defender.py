from tkinter import *
from PIL import ImageTk, Image


class Defender:
    def __init__(self, canvas, game_data, shoot):
        self.canvas = canvas
        self.game_data = game_data
        self.shoot = shoot

        self.defender = None
        self.id = None
        self.x_move = 0

        # Key binds
        self.canvas.bind_all('<KeyPress-Left>', lambda event, step=-7: self.turn_left(event, step))
        self.canvas.bind_all('<KeyPress-Right>', lambda event, step=7: self.turn_right(event, step))
        self.canvas.bind_all('<KeyPress-Down>', lambda event: self.stop_defenter(event))
        self.canvas.bind_all('<space>', lambda event: self.shoot_event(event))

        self.load_graphics()
        self.create_graphics()

    def load_graphics(self):
        try:
            raw_image = Image.open("./static/defender_1.png")
            self.defender = ImageTk.PhotoImage(raw_image)
        except IOError as e:
            print("Error: " + e)
            exit(-1)

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

        #self.x_move = 0

    def turn_left(self, event, step):
        self.x_move = step

    def turn_right(self, event, step):
        self.x_move = step

    def stop_defenter(self, event):
        self.x_move = 0

    def shoot_event(self, event):
        coords = self.canvas.coords(self.id)
        self.shoot.trigger_shoot((coords[0]+15, coords[1]))