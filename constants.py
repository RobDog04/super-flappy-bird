import pygame

CLOCK = pygame.time.Clock()
FPS = 30
VEL = 3

WIDTH, HEIGHT = 600, 900
SCREEN_DIM = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode (SCREEN_DIM)

BG_SURFACE = pygame.image.load("assets/bg_day.png").convert()
BG_SURFACE = pygame.transform.scale(BG_SURFACE,(SCREEN_DIM))

BASE_HEIGHT = 100
BASE_SURFACE = pygame.image.load("assets/base.png").convert()
BASE_SURFACE = pygame.transform.scale(BASE_SURFACE,(WIDTH, BASE_HEIGHT))

PIPE_WIDTH = 50
PIPE_GAP = 120
PIPE_SPACING = 200
PIPE_HEIGHT = 500
PIPE_SURFACE = pygame.image.load("assets/pipe.png").convert()
# BOT_PIPE_SURFACE = pygame.transform.scale(PIPE_SURFACE,(PIPE_WIDTH, PIPE_HEIGHT))
# TOP_PIPE_SURFACE = pygame.transform.flip(PIPE_SURFACE,False,True)

GENERATE_PIPE = pygame.USEREVENT + 2 # For generating pipes

GAME_OVER = pygame.USEREVENT + 1

# Bird Constants
BIRD_WIDTH = BIRD_HEIGHT = 50
# BIRD_X = 50
# BIRD_Y = int ( 576/2 - BIRD_HEIGHT/2 )
BIRD_SURFACE = pygame.image.load("assets/bird1.png").convert_alpha()
FALLING_ACC = 0.5
# BIRD_Y_CHANGE = 0

FLOOR = HEIGHT - BASE_HEIGHT