import sys
from constants import *
from bird import *
from base import *
from pipe import *
pygame.init()
pygame.display.set_caption("Flappy Bird")
base = Base()
birdObj = Bird()
pipelist = []


def generate_pipes():
    if len(pipelist) == 0:
        for i in range (1, 5):
            pipelist.append(Pipe(WIDTH + i*PIPE_SPACING))
    if pipelist[0].x_loc <= 0:
        pipelist.pop(0)
        pipelist.append(Pipe(WIDTH + PIPE_SPACING))

def game_loop():
    generate_pipes()
    for pipe in pipelist:
        pipe.move()
    birdObj.bird_fall()
    draw_window()
    pygame.display.update()


def draw_window():
    SCREEN.blit(BG_SURFACE,(0,0))
    for pipe in pipelist:
        pipe.draw_pipe()
    birdObj.draw_bird()
    base.draw()


def main():
    run = True
    while run:
        
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == GAME_OVER:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    birdObj.jump_bird()
            # if event.type == GENERATE_PIPE:
            #     pipelist.extend(pipeobj.create_pipe())
            #     pipeobj.movelist(pipelist)
            #     # print(pipelist)
        game_loop()

    pygame.quit()


main()