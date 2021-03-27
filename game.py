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

pygame.display.set_caption("Flappy Bird ")
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        SCREEN.blit(BG_SURFACE,(0,0))
        SCREEN.blit(PIPE_SURFACE,PIPE_BOUNDARY)
        FLOOR_X_POS -= 1
        draw_floor()
        if FLOOR_X_POS <= -576:
            FLOOR_X_POS = 0
       
       
        pygame.display.update()
        CLOCK.tick(120)              
                
        


     
pygame.quit()
