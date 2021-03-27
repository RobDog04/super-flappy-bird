import sys
from constants import *
from bird import *
from pipe import *
from base import *

pygame.init()
pygame.display.set_caption("Flappy Bird")
base = Base()

# def game_loop():
    
def draw_window():
    SCREEN.blit(BG_SURFACE,(0,0))
    base.draw_floor()
    pygame.display.update()

run = True
while run:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # game_loop()
    draw_window()

pygame.quit()