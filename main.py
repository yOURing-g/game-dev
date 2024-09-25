import pygame
import settings

def init_game():
    pygame.init()
    pygame.mixer.init() #sound system
    screen = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT)) #sets window width and height
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    running = True  # if game is running
    playing =True

    return screen, clock , all_sprites,playing,running
# create new instance of the game
def new_game(screen,clock,all_sprites,running):
     all_sprites = pygame.sprite.Group()
     playing = True
     return run_game(screen,clock,all_sprites,playing,running)

def handle_event(playing,running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing =False
            running = False
    return  playing, running


def run_game(screen,clock,all_sprites,playing,running):
    while playing:
        clock.tick(settings.FPS)
        playing,running = handle_event(playing,running)
        update_game(all_sprites)
        draw_sprites(screen,all_sprites)
    return  playing , running


def draw_sprites(screen , all_sprites):
    screen.fill(settings.WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

def update_game(all_sprites):
    all_sprites.update()

def start_game():
    screen, clock, all_sprites, playing, running = init_game()
    while running:
        playing, running = new_game(screen,clock,all_sprites,running)
    pygame.quit()


start_game()
