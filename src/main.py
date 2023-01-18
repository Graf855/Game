import os
import sys
import pygame

from constants import *
from base_functions import *
from generation_level import generate_level
from camera import Camera

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)

level = load_level(f'map1.txt')
player, level_x, level_y, obstacle_map = generate_level(level)

camera = Camera()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.new_duration(event.pos)
    player.update_location()
    camera.update(player)
    camera.apply_player_end_pos(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill((0, 0, 0))
    all_tiles.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
