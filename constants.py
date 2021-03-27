import pygame

SCREEN = pygame.display.set_mode ((576,1024))
CLOCK = pygame.time.Clock()
BG_SURFACE = pygame.image.load("assets/bg_day.png").convert()
BG_SURFACE = pygame.transform.scale(BG_SURFACE,(576,1000))
BASE_SURFACE = pygame.image.load("assets/base.png").convert()
BASE_SURFACE = pygame.transform.scale(BASE_SURFACE,(576,200))
FLOOR_X_POS = 0