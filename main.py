import pygame as pg
import sys
from random import randint

from hunter import Hunter
from screen import Screen
from bird import Bird
from bullet import Bullet

pg.init()

# IMAGE
icon = pg.image.load("img/hunter.png")
hunter_img = pg.image.load("img/hunter.png")
hunter_left_list = [pg.image.load(f"img/hunter_left_{i}.png") for i in range(1, 3)]
hunter_right_list = [pg.image.load(f"img/hunter_right_{i}.png") for i in range(1, 3)]
hunter_img.set_colorkey((255, 255, 255))
back_img = pg.image.load("img/back.jpg")

bird_right_list = [pg.image.load(f"img/bird_right_{i}.png") for i in range(1, 7)]
bird_left_list = [pg.image.load(f"img/bird_left_{i}.png") for i in range(1, 7)]

bullet_45_img = pg.image.load("img/bullet_45.png")
bullet_45_img.set_colorkey((255, 255, 255))
bullet_135_img = pg.image.load("img/bullet_135.png")

# AUDIO
bullet_shot = pg.mixer.Sound("audio/sounds/bullet_sound.mp3")

# DISPLAY
surface = pg.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
pg.display.set_caption("HUNTERS")
pg.display.set_icon(icon)

# CREATE OBJECTS
screen_obj = Screen(back_img)
hunter_obj = Hunter(hunter_img, hunter_left_list, hunter_right_list)

# VARIABLES
frame_hunter = 0

frame_bird = 0
bird_list = []
bird_i = 0
bird_random = randint(20, 60)

bullet_list = []

clock = pg.time.Clock()


# FUNCTION


def close_app(event):
    if event.type == pg.QUIT:
        pg.quit()
        sys.exit()


def move_hunter(event):
    if event.key in [pg.K_a, pg.K_d]:
        hunter_obj.move(chr(event.key))
        hunter_obj.set_is_move(True)


def random_create_bird():
    global frame_bird
    global bird_i
    global bird_random

    frame_bird += 1
    frame_bird %= 6

    bird_i += 1

    if bird_i % bird_random == 0:
        bird_list.append(Bird(bird_right_list, bird_left_list))
        bird_i = 0
        bird_random = randint(20, 60)


def update_animation_hunter():
    global frame_hunter
    frame_hunter += 1
    frame_hunter %= 2

    hunter_obj.update(surface, frame_hunter)


def create_bullet(event, max_bullet):
    if len(bullet_list) < max_bullet:
        if event.key == pg.K_q:
            bullet_shot.play()
            bullet_list.append(Bullet(hunter_obj, bullet_45_img, bullet_135_img, 45))
        elif event.key == pg.K_e:
            bullet_shot.play()
            bullet_list.append(Bullet(hunter_obj, bullet_45_img, bullet_135_img, 135))


def update_birds():
    for bird in bird_list:
        if bird.is_active:
            bird.update(surface, frame_bird)
        else:
            bird_list.remove(bird)


def update_bullets():
    for bullet in bullet_list:
        if bullet.is_active:
            bullet.update(surface)
        else:
            bullet_list.remove(bullet)


def collision_bird_bullet():
    for bullet in bullet_list:
        for bird in bird_list:
            if bullet.collision_bird(bird):
                bullet_list.remove(bullet)
                bird_list.remove(bird)


def collision_objects():
    collision_bird_bullet()


def update_objects():
    screen_obj.update(surface)
    update_birds()
    update_bullets()
    update_animation_hunter()


while True:
    for event in pg.event.get():
        close_app(event)
        if event.type == pg.KEYDOWN:
            move_hunter(event)
            create_bullet(event, 3)

    random_create_bird()
    collision_objects()
    update_objects()

    clock.tick(Screen.FPS)
    pg.display.flip()
