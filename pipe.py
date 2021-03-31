from constants import *
import random
class Pipe:

    def create_pipe(self):
            x_loc = WIDTH+250
            pipe_level = [500,600,700]
            y_loc = random.choice(pipe_level)
            newpipe = PIPE_SURFACE.get_rect(midtop = (x_loc,y_loc))
            return newpipe
    def movelist(self,pipes):
            for pipe in pipes:
             pipe.move_ip(-150,0)
            return pipes
    def draw_pipe(self,pipes):
            for pipe in pipes:
                SCREEN.blit(PIPE_SURFACE,pipe)  
               