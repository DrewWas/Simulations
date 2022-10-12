import pygame
from itertools import cycle

pygame.init()
pygame.display.init()

window = pygame.display.set_mode((900,900))
pygame.display.set_caption("terrain")

def draw():
    z1, z2 = 50, 70
    for i in range(40):
        for j in range(40):
            #Could these be combined into 1??
            pygame.draw.polygon(window, (0,138,255), (  
                                        (50 + 20 * i, 50 + 20 * j), 
                                        (70 + 20 * i, 70 + 20 * j), 
                                        (z1 + 20 * i, z2 + 20 * j)), 1)

            pygame.draw.polygon(window, (0,138,255), ( 
                                        (850 - 20 * i, 850 - 20 * j), 
                                        (830 - 20 * i, 830 - 20 * j), 
                                        (850 - 20 * i, 830 - 20 * j)), 1)


def main():
    run = True
    while run:
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()
        pygame.display.update()



main()
