import sys
from constants import *
from bird import *
from pipe import *
from base import *

pygame.init()
pygame.display.set_caption("Flappy Bird")
base = Base()
pipeobj = Pipe()


GENERATE_PIPE = pygame.USEREVENT
pygame.time.set_timer(GENERATE_PIPE,1200)


def game_loop():
    tes=0
def draw_window(pipe):
    SCREEN.blit(BG_SURFACE,(0,0))
    base.draw()
    pipeobj.draw_pipe(pipe)

    
def main():
    pipe = []
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == GAME_OVER:
                run = False
            draw_window()
            pygame.display.update()
        # game_loop()
        
    
    pygame.quit()
main()