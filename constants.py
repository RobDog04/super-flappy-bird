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
