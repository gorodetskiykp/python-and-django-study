import pygame
import random
import math

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
enemy_x = random.randint(0, 740)
enemy_y = random.randint(0, 100)
enemy_x_change = 0
enemy_x_direction = 1
enemy_y_change = 50


def player(x, y):
    screen.blit(player_image, (x, y)) 


def enemy(x, y):
    screen.blit(enemy_image, (x, y)) 


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

    enemy_x_change = 1 * enemy_x_direction

    if 0 < player_x + player_x_change < 740:
        player_x += player_x_change
    if 0 < player_y + player_y_change < 540:        
        player_y += player_y_change

    if 0 < enemy_x + enemy_x_change < 740:
        enemy_x += enemy_x_change
        enemy_y = int(enemy_y_change + 10 * math.sin(enemy_x * 0.05))
    else:
        enemy_x_direction *= -1
        enemy_y_change += 50       

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()

    if enemy_x <= player_x <= enemy_x + 64 and enemy_y <= player_y <= enemy_y + 64 or enemy_y > 540:
        running = False
