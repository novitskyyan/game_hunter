import pygame as pg

from hunter import Hunter
from screen import Screen


class Bullet:
    SIZE = 30
    SPEED = 30

    def __init__(self, hunter, bullet_45, bullet_135, angle):
        self.angle = angle

        if self.angle == 45:
            self.img = pg.transform.scale(bullet_45, (Bullet.SIZE, Bullet.SIZE))
        elif self.angle == 135:
            self.img = pg.transform.scale(bullet_135, (Bullet.SIZE, Bullet.SIZE))

        self.x = hunter.pos_x + Hunter.SIZE // 2
        self.y = hunter.pos_y + Hunter.SIZE // 2
        self.is_active = True

    def move_45(self):
        self.y -= Bullet.SPEED
        if self.x > 0 - Bullet.SIZE:
            self.x -= Bullet.SPEED
        else:
            self.is_active = False

    def move_135(self):
        self.y -= Bullet.SPEED
        if self.x < Screen.WIDTH:
            self.x += Bullet.SPEED
        else:
            self.is_active = False

    def collision_bird(self, bird):
        if bird.x - 30 <= self.x <= bird.x + 30 and bird.y - 30 <= self.y <= bird.y + 30:
            return True
        return False

    def update(self, screen):
        if self.is_active:
            if self.angle == 45:
                self.move_45()
            elif self.angle == 135:
                self.move_135()
            screen.blit(self.img, (self.x, self.y))
