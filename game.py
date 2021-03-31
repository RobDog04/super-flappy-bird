import sys
from constants import *
from bird import *
from base import *
from pipe import *
pygame.init()
pygame.display.set_caption("Flappy Bird")
base = Base()
pipeobj = Pipe()
GENERATE_PIPE = pygame.USEREVENT # For generating pipes
pygame.time.set_timer(GENERATE_PIPE,3000)

def generate_pipes():
    tes=0

def game_loop():
    tes1=0

def draw_window():
    SCREEN.blit(BG_SURFACE,(0,0))
    pipeobj.draw_pipe(pipelist)
    base.draw()
    
    
    
pipelist = []

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
            
            if event.type == GENERATE_PIPE:
                pipelist.extend(pipeobj.create_pipe())
                pipeobj.movelist(pipelist)
                print(pipelist)
                
                
                
                 
               
        game_loop()
        draw_window()
        pygame.display.update()
        #BIRD_MOVE = bird_fall(BIRD_Y_CHANGE)
        BIRD_Y_CHANGE += 0.25
        BIRD = animated_bird(BIRD_SURFACE, BIRD_Y_CHANGE)
        BIRD_BOUNDARY.centery += BIRD_Y_CHANGE
        draw_bird(BIRD, BIRD_BOUNDARY)
        
        
    pygame.quit()

main(BIRD_Y_CHANGE, BIRD_INDEX)