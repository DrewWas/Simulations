import pygame
pygame.init()
pygame.display.init()
window = pygame.display.set_mode((700,700))

def draw():
    z1, z2 = 50,70 
    for i in range(4):
        for j in range(4):
             if i % 2 == 0:
                 pygame.draw.polygon(window, (0,138,255), (   
                                        (50 + 20 * i, 50 + 20 * j), 
                                        (70 + 20 * i, 70 + 20 * j),  
                                        (z1 + 20 * i, z2 + 20 * j)), 1)
        z1 = z2
        z2 = z1
    pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw()
