import pygame as pg
from random import randint, choice

from hunter import Hunter
from screen import Screen

pg.init()


class Bird:
    SIZE_LIST = [30, 40, 50, 60, 70]
    SPEED_LIST = [i * 2 for i in range(1, 10)]

    def __init__(self, bird_right_list, bird_left_list):
        self.side = choice(["left", "right"])
        self.size = choice(Bird.SIZE_LIST)
        if self.side == "left":
            self.x = 0
            self.img_list = [pg.transform.scale(img, (self.size, self.size)) for img in bird_right_list]
        else:
            self.x = Screen.WIDTH
            self.img_list = [pg.transform.scale(img, (self.size, self.size)) for img in bird_left_list]
        self.y = randint(50, Screen.HEIGHT - Hunter.SIZE - 300)
        self.speed = choice(Bird.SPEED_LIST)
        self.is_active = True

    def move_right(self):
        if self.x < Screen.WIDTH:
            self.x += self.speed
        else:
            self.is_active = False

    def move_left(self):
        if self.x > 0 - self.size:
            self.x -= self.speed
        else:
            self.is_active = False

    def update(self, screen, frame):
        if self.is_active:
            if self.side == "left":
                self.move_right()
            else:
                self.move_left()
            screen.blit(self.img_list[frame], (self.x, self.y))
