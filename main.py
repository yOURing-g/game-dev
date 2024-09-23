import pygame
import settings

# globals

screen = None
clock = None
running = False #if game is running
all_sprites = None

def init_game():
    global  screen,clock
    pygame.init()
    pygame.mixer.init() #sound system
    screen = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT)) #sets window width and height
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()
def new_game():
    global all_sprites
    all_sprites = pygame.sprite.Group()

def draw_sprite():
    global  screen, all_sprites
    screen.fill(settings.WHITE)









def run_game():

    #loop to run the game
    while running:


