from constants import *
class Pipe:
        
        def create_pipe(self):
            x_loc = WIDTH*2
            y_loc = HEIGHT/2
            newpipe = PIPE_SURFACE.get_rect(midtop = (x_loc,y_loc))
            return newpipe
        def move(self,pipelist):
            for pipe in pipelist:
             pipe.centerx -= 150
            return pipelist

        def draw_pipe(self,pipelist):
            for pipe in pipelist:
                SCREEN.blit(PIPE_SURFACE,pipe)   