import pygame as pg
import sys
from settings import *
from player import *

from obstacles import *

def init_game():
    pg.init()
    game = {
        'screen': pg.display.set_mode((WIDTH, HEIGHT)),
        'clock': pg.time.Clock(),
        'all_sprites': [],
        'walls': [],
        'player': None,
        'running': True,
        'playing': False
    }
    pg.display.set_caption(TITLE)
    return game


def new_instance(game):
    # Reset all sprites
    game['all_sprites'] = []
    game['walls'] = []

    # Create player and walls
    init_player(game, 0, 0)
    draw_wall(game,5,0)



def run_game(game):
    game['playing'] = True
    while game['playing']:
        dt = game['clock'].tick(FPS) / 1000
        handle_events(game)
        update_game(game)
        draw_game(game)


def handle_events(game):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game(game)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                move_player(game["player"], x=-1)
            if event.key == pg.K_RIGHT:
                move_player(game["player"], x=1)
            if event.key == pg.K_UP:
                move_player(game["player"], y=-1)
            if event.key == pg.K_DOWN:
               move_player(game["player"], y=1)



def update_game(game):
    # Update player and walls
    player = game["player"]
    update_player(game["player"])
    # for wall in game['walls']:
    #     update_wall(wall)
    # pass



def draw_grid(game):
    for x in range(0,WIDTH,TILESIZE):
        pg.draw.line(game["screen"],BLACK,(x,0),(x,HEIGHT))
    for  y in range(0,WIDTH,TILESIZE):
        pg.draw.line(game["screen"],BLACK,(0,y),(WIDTH,y))



def draw_game(game):
    # Clear screen and draw everything
    game['screen'].fill(TAN)
    draw_grid(game)
    for sprite in game['all_sprites']:
        game['screen'].blit(sprite['image'], sprite['rect'])

    # Update display
    pg.display.flip()


def quit_game(game):
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    game = init_game()
    while game['running']:
        new_instance(game)
        run_game(game)
