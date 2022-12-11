import pygame
from sys import exit

from pygame import surface
from pygame.constants import MOUSEMOTION
from pygame.draw import line

pygame.init()

screen = pygame.display.set_mode((800, 400)) # pygame window
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Runner', False, (64, 64, 64))
text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))
snail_x_pos = 600

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50, 300))
player_gravity = 0

while True: # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
           if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                player_gravity = -20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -20

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', text_rect)
    pygame.draw.rect(screen, '#c0e8ec', text_rect, 10)
    screen.blit(text_surface, text_rect)
    snail_rect.left -= 3
    if snail_rect.right <= 0:
        snail_rect.left = 800 

    screen.blit(snail_surface, snail_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
    screen.blit(player_surface, player_rect)

    if snail_rect.colliderect(player_rect):
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)
