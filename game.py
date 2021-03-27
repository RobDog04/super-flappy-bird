import sys
from constants import *
from bird import *
from pipe import *
from base import *

pygame.init()
pygame.display.set_caption("Flappy Bird")
base = Base()
pipe = Pipe()

def generate_pipes():
    tes =0

def game_loop():
    generate_pipes()
    
def draw_window():
    SCREEN.blit(BG_SURFACE,(0,0))
    base.draw()
    pygame.display.update()

def main():
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == GAME_OVER:
                run = False
        # game_loop()
        draw_window()

    pygame.quit()

main()