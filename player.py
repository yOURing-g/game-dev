import pygame as pg
# from pygame.examples.grid import TILE_SIZE
from settings import *

def init_player(game,x,y):
    image = pg.image.load("pixil-gif-drawing_1.png").convert_alpha()
    resized_image = pg.transform.scale(image,(60,60))
    img_border= image.get_rect()
    player={
        "image": resized_image,
        "rect": img_border,
        "x": x,
        "y":y
    }
    img_border.x = x * TILESIZE
    img_border.y = y * TILESIZE
    game["all_sprites"].append(player)
    game["player"] = player

    return player


def move_player(player,x=0,y=0):
# calculate the sprite position
    new_x  = player["x"] + x
    new_y =  player["y"] + y

    # get the  max available position
    max_x = (WIDTH // TILESIZE) -1
    max_y = (HEIGHT // TILESIZE) -1
           
# limit sprite movement
    player["x"] =  max(0 , min(new_x, max_x))
    player["y"] =  max(0 , min(new_y, max_y))


    
    

def update_player(player):

    # make sure the image stays in the boxing rectangle
    player["rect"].x =player["x"] * TILESIZE
    player["rect"].y = player["y"] * TILESIZE
