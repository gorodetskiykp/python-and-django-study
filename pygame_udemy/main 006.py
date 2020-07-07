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
player_x_change = 0
player_y_change = 0

enemy_image = pygame.image.load("enemy.png")
enemy_x = 370
enemy_y = 480
enemy_x_change = 0
enemy_y_change = 0

def player(x, y):
    screen.blit(player_image, (x, y)) 


def enemy(x, y):
    screen.blit(player_image, (x, y)) 


running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_LEFT:
                player_x_change = - 1
            if event.key == pygame.K_UP:
                player_y_change = -1
            if event.key == pygame.K_DOWN:
                player_y_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

    if 0 < player_x + player_x_change < 740:
        player_x += player_x_change
    if 0 < player_y + player_y_change < 540:        
        player_y += player_y_change              
    player(player_x, player_y)
    pygame.display.update()