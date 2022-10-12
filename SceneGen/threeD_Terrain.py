import pygame
from itertools import cycle

pygame.init()
pygame.display.init()

window = pygame.display.set_mode((900,900))
pygame.display.set_caption("terrain")

def draw():
    xplus = cycle([0, 850])
    yplus = cycle([70,830]) 
    for i in range(40):

        for j in range(40):
            #pygame.draw.rect(window, (0,138,255), pygame.Rect(50 + (20 * i),50 + (20 * j),20,20), 1)
            pygame.draw.polygon(window, (0,138,255), (  (xplus + 20 * i, xplus + 20 * j), (yplus + 20 * i, yplus + 20 * j), (xplus + 20 * i, yplus + 20 * j)), 1)


            #pygame.draw.polygon(window, (0,138,255), (  (850 - 20 * i, 850 - 20 * j), (830 - 20 * i, 830 - 20 * j), (850 - 20 * i, 830 - 20 * j)), 1)

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
