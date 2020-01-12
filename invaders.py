from tkinter import *
from PIL import ImageTk, Image
import random


class Invaders:
    def __init__(self, canvas, shoot, divider, number_of_types):
        """

        :param canvas:
        :param shoot:
        :param divider:
        :param number_of_types:
        """
        self.canvas = canvas
        self.shoot = shoot
        self.divider = divider
        self.divider_cnt = 0
        self.invaders_pictures = list()
        self.number_of_types = number_of_types
        self.number_of_invaders = None
        self.score = 0

        self.load_graphics()

    def load_graphics(self):
        """

        :return:
        """
        item_list = [("inv_0" + str(x) + ".png") for x in range(1, self.number_of_types+1)]
        raw_image = None

        for item in item_list:
            raw_image = Image.open("./static/" + item)
            self.invaders_pictures.append(ImageTk.PhotoImage(raw_image))

    def locate_invader(self):
        """

        :return:
        """
        new_invader_type = random.randint(0, self.number_of_types-1)
        print(new_invader_type)

        item_collision = True

        while item_collision:
            position = random.randint(100, 600)
            invader_x = position
            position = random.randint(10, 250)
            invader_y = position

            elements_overlap = self.canvas.find_overlapping(invader_x, invader_y, invader_x + 30, invader_y + 30)

            if len(elements_overlap) == 0:
                self.canvas.create_image(invader_x, invader_y, anchor=NW,
                                         image=self.invaders_pictures[new_invader_type], tag="invader")
                item_collision = False
            else:
                print("Wylosowano na innym obcym!")
                item_collision = True

    def move_invaders(self):
        """

        :return:
        """
        pass

    def set_invaders(self, number_of_invaders=None, level=None):
        """

        :param number_of_invaders:
        :param level:
        :return:
        """
        if number_of_invaders:
            self.number_of_invaders = number_of_invaders

        for i in range(self.number_of_invaders):
            self.locate_invader()

    def manage_invaders(self, level=None):
        """

        :param level:
        :return:
        """
        pass

    def hit_invader(self):
        """

        :return:
        """
        bullet_items = self.canvas.find_withtag("bullet")
        invader_items = self.canvas.find_withtag("invader")

        for item_b in bullet_items:
            bullet_x0, bullet_y0, bullet_x1, bullet_y1 = self.canvas.bbox(item_b)
            elements_overlap = self.canvas.find_overlapping(bullet_x0, bullet_y0, bullet_x1, bullet_y1)

            for overlap in elements_overlap:
                for item_i in invader_items:
                    if item_i == overlap:
                        self.canvas.delete(item_i)
                        self.canvas.delete(item_b)

    def draw(self):
        """

        :return:
        """
        self.hit_invader()
        # TODO: move_invaders()
        pass