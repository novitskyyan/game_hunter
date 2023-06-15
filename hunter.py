import pygame as pg
from screen import Screen

pg.init()


class Hunter:
    SIZE = 100
    SPEED = SIZE // 2

    def __init__(self, img, img_left_list, img_right_list):
        self.img = pg.transform.scale(img, (Hunter.SIZE, Hunter.SIZE))
        self.img_left_list = [pg.transform.scale(img, (Hunter.SIZE, Hunter.SIZE)) for img in img_left_list]
        self.img_right_list = [pg.transform.scale(img, (Hunter.SIZE, Hunter.SIZE)) for img in img_right_list]
        self.img_list = self.img
        self.pos_x = (Screen.WIDTH - Hunter.SIZE) // 2
        self.pos_y = Screen.HEIGHT * 0.8 - Hunter.SIZE
        self.is_move = False

    def move_left(self):
        if self.pos_x > 0:
            self.img_list = self.img_left_list
            self.pos_x -= Hunter.SPEED
            self.is_move = True
        else:
            self.is_move = False

    def move_right(self):
        if self.pos_x < Screen.WIDTH - Hunter.SIZE:
            self.img_list = self.img_right_list
            self.pos_x += Hunter.SPEED
            self.is_move = True
        else:
            self.is_move = False

    def move(self, key):
        move_dir = {"a": self.move_left,
                    "d": self.move_right}

        if move_func := move_dir.get(key):
            move_func()

    def set_static_img(self):
        if not self.is_move:
            self.img_list = self.img

    def set_is_move(self, flag):
        self.is_move = flag

    def update(self, surface, frame):
        self.set_static_img()
        if self.is_move:
            surface.blit(self.img_list[frame], (self.pos_x, self.pos_y))
        else:
            surface.blit(self.img_list, (self.pos_x, self.pos_y))
