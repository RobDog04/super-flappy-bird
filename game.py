import sys
from constants import *
from bird import *
from pipe import *
from base import *

pygame.init()
pygame.display.set_caption("Flappy Bird")
base = Base()
pipe = []

def generate_pipes():
    #tes =0
    myPipe = Pipe(100,400)
    myPipe.draw()
    pipe.append(myPipe)

def game_loop():
    generate_pipes()

def draw_window():
    SCREEN.blit(BG_SURFACE,(0,0))
    base.draw()
    pygame.display.update()


def main(BIRD_Y_CHANGE, BIRD_INDEX):
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == GAME_OVER:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #bird_jump()
                    BIRD_Y_CHANGE = 0
                    BIRD_Y_CHANGE -= 7.5
            if event.type == BIRD_FLAP:
                print("here")
                BIRD_INDEX = (BIRD_INDEX + 1) % 2

        game_loop()
        draw_window()
        #BIRD_MOVE = bird_fall(BIRD_Y_CHANGE)
        BIRD_Y_CHANGE += 0.25
        BIRD = animated_bird(BIRD_SURFACE, BIRD_Y_CHANGE)
        BIRD_BOUNDARY.centery += BIRD_Y_CHANGE
        draw_bird(BIRD, BIRD_BOUNDARY)

    pygame.quit()

main(BIRD_Y_CHANGE, BIRD_INDEX)