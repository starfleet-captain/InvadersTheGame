from tkinter import *
from PIL import ImageTk, Image


class Defender:
    def __init__(self, canvas, game_data, shoot):
        """

        :param canvas:
        :param game_data:
        :param shoot:
        """
        self.canvas = canvas
        self.game_data = game_data
        self.shoot = shoot

        self.defender = None
        self.id = None
        self.x_move = 0

        # Key binds
        self.bind_keys()

        self.load_graphics()
        self.create_graphics()

    def bind_keys(self):
        """
        Bind keys to control the defender.
        :return:
        """
        self.canvas.bind_all('<KeyPress-Left>', lambda event, step=-7: self.turn_left(event, step))
        self.canvas.bind_all('<KeyPress-Right>', lambda event, step=7: self.turn_right(event, step))
        self.canvas.bind_all('<KeyPress-Down>', lambda event: self.stop_defenter(event))
        self.canvas.bind_all('<space>', lambda event: self.shoot_event(event))

    def unbind_keys(self):
        """
        Unbind keys to disable control of the defender.
        :return:
        """
        self.canvas.unbind_all('<KeyPress-Left>')
        self.canvas.unbind_all('<KeyPress-Right>')
        self.canvas.unbind_all('<KeyPress-Down>')
        self.canvas.unbind_all('<space>')

    def load_graphics(self):
        """
        Load defender.
        :return:
        """
        try:
            raw_image = Image.open("./static/defender_1.png")
            self.defender = ImageTk.PhotoImage(raw_image)
        except IOError as e:
            print("Error: " + e)
            exit(-1)

    def get_position(self):
        """

        :return:
        """
        defender_item = self.canvas.find_withtag("defender")
        d_x0, d_y0, d_x1, d_y1 = self.canvas.bbox(defender_item[0])

        position = (d_x0, d_x1)

        return position

    def create_graphics(self):
        """
        Put defender on game screen.
        :return:
        """
        self.id = self.canvas.create_image(self.game_data.get_window_size()['WIDTH']/2 - 15,
                                           self.game_data.get_window_size()['HEIGHT']-50,
                                           image=self.defender, anchor=NW, tag='defender')

    def draw(self):
        """
        Draw defender on current position.
        :return:
        """
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
        """
        Sets left direction of the defender.
        :param event:
        :param step:
        :return:
        """
        self.x_move = step

    def turn_right(self, event, step):
        """
        Sets right direction of the defender.
        :param event:
        :param step:
        :return:
        """
        self.x_move = step

    def stop_defenter(self, event):
        """
        Stops defender.
        :param event:
        :return:
        """
        self.x_move = 0

    def shoot_event(self, event):
        """
        Triggers shoot.
        :param event:
        :return:
        """
        coords = self.canvas.coords(self.id)
        self.shoot.trigger_shoot((coords[0]+15, coords[1]))