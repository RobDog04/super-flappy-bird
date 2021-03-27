from constants import *

class Base:
    tick_count = 0;

    def draw(self):
        self.tick_count -= VEL
        SCREEN.blit(BASE_SURFACE,(self.tick_count , HEIGHT - BASE_HEIGHT))
        SCREEN.blit(BASE_SURFACE,(self.tick_count + WIDTH, HEIGHT - BASE_HEIGHT))
        if self.tick_count <= -WIDTH:
            self.tick_count = 0