import pygame
import sys
from constants import *
from bird import *
from pipe import *

pygame.init()
def draw_floor():
      SCREEN.blit(BASE_SURFACE,(FLOOR_X_POS, 800))
      SCREEN.blit(BASE_SURFACE,(FLOOR_X_POS + 576, 800))



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
                
        


     
