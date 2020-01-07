from tkinter import *
from PIL import ImageTk, Image
import random


class Invaders:
    def __init__(self, canvas, shoot, divider, number_of_types):
        self.canvas = canvas
        self.shoot = shoot
        self.divider = divider
        self.divider_cnt = 0
        self.invaders_pictures = list()
        self.number_of_types = number_of_types
        self.score = 0

        self.load_graphics()

    def load_graphics(self):
        item_list = [("inv_0" + str(x) + ".png") for x in range(1, self.number_of_types+1)]
        raw_image = None

        for item in item_list:
            raw_image = Image.open("./static/" + item)
            self.invaders_pictures.append(ImageTk.PhotoImage(raw_image))

    def locate_invader(self):
        invader = self.canvas.find_withtag("invader")

        if len(invader) > 0:
            self.canvas.delete(invader[0])

        new_invader_type = random.randint(0, self.number_of_types-1)
        print(new_invader_type)

        self.canvas.create_image(100, 100, anchor=NW, image=self.invaders_pictures[new_invader_type], tag="invader")

    def create_graphics(self):
        pass

    def manage_invaders(self, number_of_invaders=1):
        pass

    def hit_invader(self):
        pass

    def draw(self):
        pass