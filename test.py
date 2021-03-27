import pygame, sys
pygame.init()
def draw_floor():
      screen.blit(base_surface,(floor_x_pos,800))
      screen.blit(base_surface,(floor_x_pos+576,800))

screen = pygame.display.set_mode ((576,1024))
clock = pygame.time.Clock()
bg_surface = pygame.image.load('assets/bg_day.png').convert()
bg_surface = pygame.transform.scale(bg_surface,(576,1000))
base_surface = pygame.image.load('assets/base.png').convert()
base_surface = pygame.transform.scale(base_surface,(576,200))
floor_x_pos=0

pygame.display.set_caption("Flappy Bird ")
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        screen.blit(bg_surface,(0,0))
        floor_x_pos-=1
        draw_floor()
        if floor_x_pos<=-576:
            floor_x_pos=0
       
       
        pygame.display.update()
        clock.tick(120)              
                
        


     
