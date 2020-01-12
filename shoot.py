from tkinter import *
from PIL import ImageTk, Image


class Shoot:
    def __init__(self, canvas, divider):
        """

        :param canvas:
        :param divider:
        """
        self.canvas = canvas
        self.divider = divider
        self.divider_cnt = 0
        self.bullets = list()

    def trigger_shoot(self, def_coords):
        """

        :param def_coords:
        :return:
        """
        bullet = self.canvas.create_rectangle(def_coords[0]-1, def_coords[1]-10, def_coords[0]+1, def_coords[1],
                                              tag="bullet", fill="white")
        self.bullets.append(bullet)

    def draw(self):
        """

        :return:
        """
        if len(self.bullets) > 0:
            self.divider_cnt += 1
            if self.divider_cnt >= self.divider:
                for element in self.bullets:
                    self.canvas.move(element, 0, -3)

                    coords = self.canvas.coords(element)
                    if len(coords) > 0:
                        if int(coords[1]) <= 0:
                            self.bullets.remove(element)
                            self.canvas.delete(element)
                    else:
                        self.bullets.remove(element)
                self.divider_cnt = 0
