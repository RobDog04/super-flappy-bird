from constants import *
BIRD_WIDTH = BIRD_HEIGHT = 50
BIRD_X = 50
BIRD_Y = int ( 576/2 - BIRD_HEIGHT/2 )
BIRD_SURFACE = pygame.image.load("assets/bird2.png").convert()
BIRD_BOUNDARY = BIRD_SURFACE.get_rect(center=(150,500))



