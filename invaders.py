from tkinter import *
from PIL import ImageTk, Image
import random
import time

class Invaders:
    def __init__(self, canvas, game_data, shoot, addons, defender, divider, number_of_types_inv, number_of_types_boss):
        """

        :param canvas:
        :param shoot:
        :param divider:
        :param number_of_types_inv:
        """
        self.canvas = canvas
        self.game_data = game_data
        self.shoot = shoot
        self.defender = defender
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

        self.star_animation = addons

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
        item_collision = True

        while item_collision:
            position = random.randint(50, 650)
            invader_x = position
            position = random.randint(10, 150)
            invader_y = position

            elements_overlap = self.canvas.find_overlapping(invader_x, invader_y, invader_x + 30, invader_y + 30)

            if len(elements_overlap) == 0:
                self.canvas.create_image(invader_x, invader_y, anchor=NW,
                                         image=self.invaders_pictures[new_invader_type], tag="invader")
                item_collision = False
            else:
                item_collision = True

    def locate_boss(self):
        """

        :return:
        """
        new_boss_type = random.randint(0, self.number_of_types_boss - 1)

        position = random.randint(50, 600)
        boss_x = position
        position = random.randint(10, 200)
        boss_y = position

        self.canvas.create_image(boss_x, boss_y, anchor=NW, image=self.bosses_pictures[new_boss_type], tag="boss")

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

    def move_boss(self):
        """

        :return:
        """
        boss_item = self.canvas.find_withtag("boss")

        boss_x0, boss_y0, boss_x1, boss_y1 = self.canvas.bbox(boss_item)

        calculate_y = lambda x: 1 if (x > 15) else 0

        direction = random.randint(0, 1)
        move_x = random.randint(0, 4)

        if direction == 0:
            move_x = move_x * (-1)

        move_y = calculate_y(random.randint(0, 50))

        if boss_x1 + move_x < self.game_data.get_window_size()['WIDTH'] > boss_x0 + move_x > 0:
            pass
        else:
            move_x = move_x * (-1)

        self.canvas.move(boss_item, move_x, move_y)

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
        bullet_items = self.canvas.find_withtag("bullet")
        boss_item = self.canvas.find_withtag("boss")

        boss_x0, boss_y0, boss_x1, boss_y1 = self.canvas.bbox(boss_item)

        if boss_y1 >= (self.game_data.get_window_size()['HEIGHT'] - 35):
            self.game_data.in_game = False
            print("GAME OVER!")

        for item_b in bullet_items:
            bullet_x0, bullet_y0, bullet_x1, bullet_y1 = self.canvas.bbox(item_b)
            elements_overlap = self.canvas.find_overlapping(bullet_x0, bullet_y0, bullet_x1, bullet_y1)

            for overlap in elements_overlap:
                if boss_item[0] == overlap:
                    if self.number_of_boss_hit == 1:
                        self.canvas.delete(boss_item)
                        self.canvas.delete(item_b)
                        self.score += 10
                        self.canvas.create_image(boss_x0, boss_y0, anchor=NW, image=self.explosion_picture,
                                                 tag="explosion")
                    else:
                        self.canvas.delete(item_b)
                        self.number_of_boss_hit -= 1

    def manage_invaders(self, level=None):
        """

        :param level:
        :return:
        """
        self.divider_cnt += 1

        if self.level_completed and self.star_animation.get_animation_status():
            # TODO: modify that for higher levels
            # TODO: add animation between levels
            if self.level < 6:
                self.level += 1
                self.level_completed = False

            if self.level < 5:
                self.set_invaders(number_of_invaders=self.number_of_invaders + self.level)
            elif self.level == 5:
                self.defender.bind_keys()
                self.locate_boss()
                self.number_of_boss_hit = 40
            elif self.level > 5:
                print("END GAME")

        elif not self.level_completed:
            # TODO: moving of invaders - depending on level
            # TODO: manage divider
            if self.level < 5:
                invader_items = self.canvas.find_withtag("invader")

                if len(invader_items) > 0:
                    current_draw = self.draw(self.move_invaders_down, self.hit_invader)
                    current_draw()
                else:

                    self.level_completed = True

                    if self.level == 4:
                        self.defender.stop_defenter(None)
                        self.defender.unbind_keys()
                        position = self.defender.get_position()
                        self.star_animation.locate_stars(20, position)
                        self.star_animation.start_animation()
                        # TODO: clear las explosion
                        self.clear_explosion()
            elif self.level == 5:
                boss_item = self.canvas.find_withtag("boss")
                if len(boss_item) > 0:
                    current_draw = self.draw(self.move_boss, self.hit_boss)
                    current_draw()
                else:
                    self.level_completed = True

        if self.divider_cnt % self.divider == 0:
            self.divider_cnt = 0

    def draw(self, moving_method, hit_method):
        """

        :return:
        """
        self.clear_explosion()

        def wrap_funct():
            moving_method()
            hit_method()

        return wrap_funct
