import pygame

CLOCK = pygame.time.Clock()
FPS = 30
VEL = 3

WIDTH, HEIGHT = 576, 700
SCREEN_DIM = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode (SCREEN_DIM)

BG_SURFACE = pygame.image.load("assets/bg_day.png").convert()
BG_SURFACE = pygame.transform.scale(BG_SURFACE,(SCREEN_DIM))

BASE_HEIGHT = 100
BASE_SURFACE = pygame.image.load("assets/base.png").convert()
BASE_SURFACE = pygame.transform.scale(BASE_SURFACE,(WIDTH,100))

PIPE_WIDTH = 75
PIPE_SURFACE = pygame.image.load("assets/pipe.png").convert()

GAME_OVER = pygame.USEREVENT + 1
