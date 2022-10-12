import pygame

pygame.init()
pygame.display.init()

window = pygame.display.set_mode((900,900))
pygame.display.set_caption("terrain")

def draw():
    x = 100
    y = 100
    for i in range(40):
        for j in range(40):
            pygame.draw.rect(window, (0,138,255), pygame.Rect(50 + (20 * i),50 + (20 * j),20,20), 1)

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
