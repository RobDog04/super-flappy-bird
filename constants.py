import pygame

CLOCK = pygame.time.Clock()
FPS = 30
VEL = 3

WIDTH, HEIGHT = 576, 900
SCREEN_DIM = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode (SCREEN_DIM)

BG_SURFACE = pygame.image.load("assets/bg_day.png").convert()
BG_SURFACE = pygame.transform.scale(BG_SURFACE,(SCREEN_DIM))

BASE_HEIGHT = 200
BASE_SURFACE = pygame.image.load("assets/base.png").convert()
BASE_SURFACE = pygame.transform.scale(BASE_SURFACE,(WIDTH, 200))

PIPE_WIDTH = 75
PIPE_SURFACE = pygame.image.load("assets/pipe.png").convert()

GENERATE_PIPE = pygame.USEREVENT
GAME_OVER = pygame.USEREVENT + 1
BIRD_FLAP = pygame.USEREVENT + 2 # For animating wings

# Bird Constants
BIRD_WIDTH = BIRD_HEIGHT = 50
BIRD_X = 50
BIRD_Y = int ( 576/2 - BIRD_HEIGHT/2 )
BIRD_1 = pygame.image.load("assets/bird1.png").convert_alpha()
BIRD_2 = pygame.image.load("assets/bird2.png").convert_alpha()
BIRD_3 = pygame.image.load("assets/bird3.png").convert_alpha()
BIRD = [BIRD_1, BIRD_2, BIRD_3]
BIRD_INDEX = 0
BIRD_SURFACE = BIRD[BIRD_INDEX]
BIRD_BOUNDARY = BIRD_SURFACE.get_rect(center=(150,500))
BIRD_Y_CHANGE = 0