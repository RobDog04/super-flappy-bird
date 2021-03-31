from constants import *
import random
class Pipe:

    def create_pipe(self):
            x_loc = WIDTH+250
            pipe_level = [450,500,600]
            y_loc = random.choice(pipe_level)
            bot_pipe = PIPE_SURFACE.get_rect(midtop = (x_loc,y_loc))
            top_pipe = PIPE_SURFACE.get_rect(midbottom = (x_loc,y_loc-100))
            return bot_pipe,top_pipe
    def movelist(self,pipes):
            for pipe in pipes:
             pipe.move_ip(-150,0)
            return pipes
    def draw_pipe(self,pipes):
            for pipe in pipes:
                if pipe.bottom >=900:
                    SCREEN.blit(PIPE_SURFACE,pipe) 
                else:
                    pipe_rotate = pygame.transform.flip(PIPE_SURFACE,False,True) # flipping the pipe vertically
                    SCREEN.blit(pipe_rotate,pipe)