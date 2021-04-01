import sys
from constants import *
from bird import *
from base import *
from pipe import *
pygame.init()
pygame.display.set_caption("Flappy Bird")
base = Base()
pipeobj = Pipe()
birdObj = Bird()
pygame.time.set_timer(GENERATE_PIPE,3000)
pipelist = []


def generate_pipes():
    tes=0


def game_loop():
    birdObj.bird_fall()
    draw_window()
    pygame.display.update()


def draw_window():
    SCREEN.blit(BG_SURFACE,(0,0))
    pipeobj.draw_pipe(pipelist)
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
            if event.type == GENERATE_PIPE:
                pipelist.extend(pipeobj.create_pipe())
                pipeobj.movelist(pipelist)
                # print(pipelist)
        game_loop()

    pygame.quit()


main()