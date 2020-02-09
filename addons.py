from tkinter import *
from PIL import ImageTk, Image
import random
import time


class StarTrip:
    def __init__(self, canvas, number_of_types_stars):
        self.canvas = canvas
        self.number_of_types_stars = number_of_types_stars
        self.stars_pictures = list()
        self.load_graphics()
        self.animation_finished = True

    def start_animation(self):
        """

        :return:
        """
        self.animation_finished = False

    def get_animation_status(self):
        """

        :return:
        """
        return self.animation_finished

    def load_graphics(self):
        """

        :return:
        """
        item_list = [("star_0" + str(x) + ".png") for x in range(1, self.number_of_types_stars + 1)]
        raw_image = None

        for item in item_list:
            raw_image = Image.open("./static/" + item)
            self.stars_pictures.append(ImageTk.PhotoImage(raw_image))

    def locate_stars(self, stars_nb, pos_range):
        """

        :param stars_nb:
        :return:
        """
        for star in range(stars_nb):
            new_star_type = random.randint(0, self.number_of_types_stars - 1)
            item_collision = True

            while item_collision:
                position = random.randint(10, 650)
                star_x = position
                position = random.randint(0, 250)
                star_y = position

                elements_overlap = self.canvas.find_overlapping(star_x, star_y, star_x + 30, star_y + 30)

                if len(elements_overlap) == 0 and (star_x < pos_range[0] or star_x > pos_range[1]):
                    self.canvas.create_image(star_x, star_y, anchor=NW, image=self.stars_pictures[new_star_type],
                                             tag="star")
                    item_collision = False
                else:
                    item_collision = True

    def animate(self):
        """

        :return:
        """
        star_items = self.canvas.find_withtag("star")

        for item_s in star_items:
            self.canvas.move(item_s, 0, 2)

        star_items = self.canvas.find_withtag("star")
        print("STAR ITEMS: {}".format(len(star_items)))

        if len(star_items) > 0:
            for star in star_items:
                star_x0, star_y0, star_x1, star_y1 = self.canvas.bbox(star)
                if star_y0 >= 600:
                    self.canvas.delete(star)
        else:
            self.animation_finished = True

    def manage_animation(self):
        """

        :return:
        """

        if not self.animation_finished:
            self.animate()
