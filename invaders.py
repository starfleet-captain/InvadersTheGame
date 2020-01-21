from tkinter import *
from PIL import ImageTk, Image
import random


class Invaders:
    def __init__(self, canvas, game_data, shoot, divider, number_of_types_inv, number_of_types_boss):
        """

        :param canvas:
        :param shoot:
        :param divider:
        :param number_of_types_inv:
        """
        self.canvas = canvas
        self.game_data = game_data
        self.shoot = shoot
        self.divider = divider
        self.divider_cnt = 0
        # Invaders
        self.invaders_pictures = list()
        self.number_of_types_inv = number_of_types_inv
        self.number_of_invaders = None

        self.bosses_pictures = list()
        self.number_of_types_boss = number_of_types_boss
        self.number_of_boss_hit = None

        self.explosion_picture = None
        # Game stat
        self.level_completed = False
        self.score = 0
        self.level = 0

        self.load_graphics()

    def get_score(self):
        """

        :return:
        """
        return self.score

    def get_level(self):
        """

        :return:
        """
        return self.level

    def load_graphics(self):
        """

        :return:
        """
        item_list = [("inv_0" + str(x) + ".png") for x in range(1, self.number_of_types_inv + 1)]
        raw_image = None

        for item in item_list:
            raw_image = Image.open("./static/" + item)
            self.invaders_pictures.append(ImageTk.PhotoImage(raw_image))

        item_list = [("boss_0" + str(x) + ".png") for x in range(1, self.number_of_types_boss + 1)]

        for item in item_list:
            raw_image = Image.open("./static/" + item)
            self.bosses_pictures.append(ImageTk.PhotoImage(raw_image))

        raw_image = Image.open("./static/explosion.png")
        self.explosion_picture = ImageTk.PhotoImage(raw_image)

    def locate_invader(self):
        """

        :return:
        """
        new_invader_type = random.randint(0, self.number_of_types_inv - 1)
        print(new_invader_type)

        item_collision = True

        while item_collision:
            position = random.randint(50, 650)
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

    def move_invaders_down(self):
        """

        :return:
        """
        invader_items = self.canvas.find_withtag("invader")

        for item_i in invader_items:
            self.canvas.move(item_i, 0, 1)

    def move_invaders_random(self):
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
        self.divider_cnt += 1

        if self.level_completed:
            self.level += 1
            self.level_completed = False

            if self.level < 5:
                self.set_invaders(number_of_invaders=self.number_of_invaders + self.level)

        else:
            # TODO: moving of invaders - depending on level
            # TODO: manage divider
            if self.level < 5:
                invader_items = self.canvas.find_withtag("invader")

                if len(invader_items) > 0:
                    current_draw = self.draw(self.move_invaders_down)
                    current_draw()
                else:
                    self.level_completed = True

        if self.divider_cnt % self.divider == 0:
            self.divider_cnt = 0

    def clear_explosion(self):
        """

        :return:
        """
        explosion_items = self.canvas.find_withtag("explosion")

        if self.divider_cnt % self.divider == 0:
            for item_e in explosion_items:
                self.canvas.delete(item_e)

    def hit_invader(self):
        """

        :return:
        """
        bullet_items = self.canvas.find_withtag("bullet")
        invader_items = self.canvas.find_withtag("invader")

        for item_i in invader_items:
            invader_x0, invader_y0, invader_x1, invader_y1 = self.canvas.bbox(item_i)

            if invader_y1 >= (self.game_data.get_window_size()['HEIGHT'] - 35):
                self.game_data.in_game = False
                print("GAME OVER!")

        for item_b in bullet_items:
            bullet_x0, bullet_y0, bullet_x1, bullet_y1 = self.canvas.bbox(item_b)
            elements_overlap = self.canvas.find_overlapping(bullet_x0, bullet_y0, bullet_x1, bullet_y1)

            for overlap in elements_overlap:
                for item_i in invader_items:
                    if item_i == overlap:
                        invader_x0, invader_y0, invader_x1, invader_y1 = self.canvas.bbox(item_i)
                        self.canvas.delete(item_i)
                        self.canvas.delete(item_b)
                        self.score += 1

                        self.canvas.create_image(invader_x0, invader_y0, anchor=NW, image=self.explosion_picture,
                                                 tag="explosion")

    def hit_boss(self):
        """

        :return:
        """
        pass

    def draw(self, moving_method):
        """

        :return:
        """
        self.clear_explosion()
        self.hit_invader()

        def wrap_funct():
            moving_method()

        return wrap_funct
