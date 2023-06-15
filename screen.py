import pygame as pg

pg.init()


class Screen:
    WIDTH = 800
    HEIGHT = 600
    FPS = 10

    def __init__(self, img):
        self.img = pg.transform.scale(img, (Screen.WIDTH, Screen.HEIGHT))

    def update(self, surface):
        surface.blit(self.img, (0, 0))
