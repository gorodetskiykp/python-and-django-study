import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# https://www.flaticon.com/
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((100, 100, 100))
    pygame.display.update()