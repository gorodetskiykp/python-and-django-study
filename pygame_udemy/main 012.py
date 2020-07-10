import pygame
import random
import math

pygame.init()

game_speed = 5

screen_width = 800
screen_height = 600
screen_resolution = screen_width, screen_height
screen = pygame.display.set_mode(screen_resolution)
background = pygame.image.load("bg.jpg")

score = 0
font = pygame.font.Font(None, 25)
text = font.render(str(score), True, (255, 255, 255))


# https://www.flaticon.com/
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

player_image = pygame.image.load("ship.png")
player_size = 64
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - 2 * player_size
player_x_change = 0
player_y_change = 0
player_speed = game_speed

enemy_image = pygame.image.load("enemy.png")
enemy_size = 64
enemy_x = random.randint(0, screen_width - enemy_size)
enemy_y = random.randint(enemy_size, 2 * enemy_size)
enemy_x_change = 0
enemy_y_change = 0
enemy_speed = game_speed
enemy_x_direction = 1

bullet_image = pygame.image.load("bullet.png")
bullet_size = 32
bullet_y_change = game_speed * 2
bullet_state = "ready"
bullet_x = 0
bullet_y = 0


def player(x, y):
    screen.blit(player_image, (x, y)) 


def enemy(x, y):
    screen.blit(enemy_image, (x, y)) 


def fire_bullet(x, y):
    screen.blit(bullet_image, (x, y))


def explosion(x, y):
    screen.blit(pygame.image.load("explosion.png"), (x, y))


def is_collision(x_1, y_1, x_2, y_2, size_1, size_2):
    x_1 = x_1 + size_1 // 2
    x_2 = x_2 + size_2 // 2
    y_1 = y_1 + size_1 // 2
    y_2 = y_2 + size_2 // 2
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distance < min(size_1, size_2):
        return True
    else:
        return False


running = True
game = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(text, (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player_x_change = player_speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player_x_change = - player_speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player_y_change = - player_speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player_y_change = player_speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if bullet_state == "ready":
                bullet_state = "fire"
                bullet_x = player_x + player_size // 2 - bullet_size // 2 
                bullet_y = player_y - bullet_size
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            player_x_change = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            player_x_change = - 1
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            player_y_change = - 1
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            player_y_change = 1
    
    enemy_x_change = enemy_speed * enemy_x_direction
    
    if 0 < player_x + player_x_change < screen_width - player_size:
        player_x += player_x_change
    if 0 < player_y + player_y_change < screen_height - player_size:        
        player_y += player_y_change

    if 0 < enemy_x + enemy_x_change < screen_width - enemy_size:
        enemy_x += enemy_x_change
        # enemy_y = int(enemy_y_change + enemy_size // 4 * math.sin(enemy_x * 0.05))
        enemy_y = enemy_y_change
    else:
        enemy_x_direction *= -1
        enemy_y_change += screen_height // 10       

    enemy(enemy_x, enemy_y)

    if is_collision(player_x, player_y, enemy_x, enemy_y, player_size, enemy_size):
        explosion(player_x, player_y)
        screen.blit(pygame.image.load("game-over.png"), (screen_width // 2 - 64, screen_height // 2 - 64))
        game = False 
    else:
        player(player_x, player_y)

    if is_collision(enemy_x, enemy_y, bullet_x, bullet_y, enemy_size, bullet_size):
        explosion(bullet_x, bullet_y - bullet_size)
        # screen.blit(pygame.image.load("win.png"), (screen_width // 2 - 64, screen_height // 2 - 64))
        enemy_x = random.randint(0, screen_width - enemy_size)
        enemy_y = random.randint(enemy_size, 2 * enemy_size)
        enemy_y_change = 0
        bullet_y = - 2 * bullet_size
        score += 1
        text = font.render(str(score), True, (255, 255, 255))
        enemy_speed += 1

        # game = False
    else:
        if bullet_state == "fire":
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change
        if bullet_y <= - bullet_size:
            bullet_state = "ready"
            bullet_y = - 2 * bullet_size   
    # pygame.draw.aaline(screen, (255, 0, 0), [bullet_x, 0], [bullet_x, 600])
    # pygame.draw.aaline(screen, (255, 0, 0), [0, bullet_y], [800, bullet_y])
    # pygame.draw.aaline(screen, (255, 0, 0), [bullet_x + bullet_size, 0], [bullet_x + bullet_size, 600])
    # pygame.draw.aaline(screen, (255, 0, 0), [bullet_x + bullet_size // 2, 0], [bullet_x + bullet_size // 2, 600])

    # pygame.draw.aaline(screen, (255, 255, 255), [enemy_x, 0], [enemy_x, 600])
    # pygame.draw.aaline(screen, (255, 255, 255), [enemy_x + enemy_size, 0], [enemy_x + enemy_size, 600])


    if enemy_y > 540:
        screen.blit(pygame.image.load("game-over.png"), (screen_width // 2 - 64, screen_height // 2 - 64))
        game = False

    pygame.display.update()

    if not game:
        pygame.time.delay(2000)
        running = False