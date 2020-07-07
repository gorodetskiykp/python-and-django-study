import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# https://www.flaticon.com/
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

player_image = pygame.image.load("ship.png")
player_x = 370
player_y = 480


def player():
    screen.blit(player_image, (player_x, player_y)) 


running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player()
    pygame.display.update()