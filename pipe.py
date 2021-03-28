from constants import *
class Pipe:
    top_h = 0   
    bot_h = 0

    tick_count = 0

    def draw(self):
        self.tick_count -= VEL
        SCREEN.blit(PIPE_SURFACE,(self.tick_count + PIPE_WIDTH , HEIGHT))
        SCREEN.blit(PIPE_SURFACE,(self.tick_count + WIDTH + PIPE_WIDTH, HEIGHT))
        if self.tick_count <= -WIDTH:
            self.tick_count = 0

    def __init__(self,h,b):
            self.top_h = h
            self.bot_h = b