import pygame as pg
from settings import *
def draw_wall(game,x,y):
    image = pg.Surface((1280,TILESIZE+TILESIZE))
    image.fill(WHITE)

    rect = image.get_rect()
    rect.x = x * TILESIZE
    rect.y = x * TILESIZE

    wall = {
        "image":image,
        "rect": rect,
        "x":x,
        "y":y,
        "game":game
    }

    game["all_sprites"].append(wall)
    game["walls"].append(wall)
    return wall


def update():
    pass

