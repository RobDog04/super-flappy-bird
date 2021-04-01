import pygame
from constants import *

class Bird:

    def animate_bird(self, bird, move):
        rotoBird = pygame.transform.rotozoom(bird, -move * 5, 1)
        return rotoBird

    def draw_bird(self, bird, boundary):
        SCREEN.blit(bird, boundary)

    def bird_fall(self, change, boundary):
        change += 0.25
        boundary.centery += change
        return change, boundary

    def jump_bird(self, bird):
        bird = 0
        bird -= 7.5
        return bird


