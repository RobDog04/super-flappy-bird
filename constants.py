import pygame

WIDTH, HEIGHT = 576, 900
BASE_HEIGHT = 200
VEL = 3
SCREEN_DIM = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode (SCREEN_DIM)
CLOCK = pygame.time.Clock()
BG_SURFACE = pygame.image.load("assets/bg_day.png").convert()
BG_SURFACE = pygame.transform.scale(BG_SURFACE,(SCREEN_DIM))
BASE_SURFACE = pygame.image.load("assets/base.png").convert()
BASE_SURFACE = pygame.transform.scale(BASE_SURFACE,(WIDTH, 200))
PIPE_SURFACE = pygame.image.load("assets/pipe.png").convert()
PIPE_ARRAY = []
SCROLLPIPE = pygame.USEREVENT
pygame.time.set_timer(SCROLLPIPE, 2000)
FLOOR_X_POS = 0
FPS = 30
