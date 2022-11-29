import pygame
from sys import exit

# Screen
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Appleseed')
clock = pygame.time.Clock()
font_1 = pygame.font.Font('Pixeltype.ttf', 50)
game_active = True

# Background
sky_surface = pygame.image.load('Sky.png').convert_alpha()
ground_surface = pygame.image.load('Ground.png').convert_alpha()
score_surface = font_1.render('Appleseed ', False, 'Black')
score_rect = score_surface.get_rect(center=(400, 60))

# Snail
snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 300))
snail_move = 5

# FLy
fly_surface = pygame.image.load('Fly1.png').convert_alpha()
fly_rect = snail_surface.get_rect(bottomright=(1000, 150))
fly_move = 7

# Player
player_surface = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))

# Gravity
player_gravity = 1

# Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
        if player_rect.top <= -80:
            player_gravity = 20
    if game_active:
        # Screen
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, 'white', score_rect)
        screen.blit(score_surface, (325, 50))
        # Snail
        screen.blit(snail_surface, snail_rect)
        snail_rect.right -= snail_move
        if snail_rect.right < - 50:
            snail_rect.right = 800
            snail_move += 0.5
        # Snail
        screen.blit(fly_surface, fly_rect)
        fly_rect.right -= snail_move
        if fly_rect.right < - 50:
            fly_rect.right = 1000
            fly_move += 1
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # APPLES
        if snail_rect.colliderect(player_rect):
            game_active = False
        if fly_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('White')
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        game_active = True
        snail_rect.left = 800
        snail_move = 5
        fly_rect.left = 1000
        fly_move = 7
    pygame.display.update()
    clock.tick(60)
