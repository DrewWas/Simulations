import pygame

pygame.init()
pygame.display.init()

window = pygame.display.set_mode((1000,700))
pygame.display.set_caption("terrain")

def draw():
    pygame.draw.rect(window, (0,138,255), pygame.Rect(250,100,500,500), 1)
    for i in range(100):
        pygame.draw.polygon(window, (0,138,255), ((250,100), (270,100), (260, 120)), 1)

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
