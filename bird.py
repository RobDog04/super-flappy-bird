import pygame
from constants import *

'''
def bird_fall(change):
    change += 0.5
    BIRD_BOUNDARY.centery += change
    return BIRD_BOUNDARY

def bird_jump():
    BIRD_Y_CHANGE = 0
    BIRD_Y_CHANGE -= 10
    print("flap")
    return BIRD_Y_CHANGE
'''
def animated_bird(bird, move):
   fallingBird = pygame.transform.rotozoom(bird, -move * 5, 1)
   return fallingBird

def draw_bird(bird, boundary):

    SCREEN.blit(bird, boundary)
    #base.draw()
    pygame.display.update()


