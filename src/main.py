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

level = load_level(f'map2.txt')
player, level_x, level_y, obstacle_map = generate_level(level)

camera = Camera()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN and event.key == 119:
            player.update_location(1, -1)
        if event.type == pygame.KEYDOWN and event.key == 97:
            player.update_location(0, -1)
        if event.type == pygame.KEYDOWN and event.key == 115:
            player.update_location(1, 1)
        if event.type == pygame.KEYDOWN and event.key == 100:
            player.update_location(0, 1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.new_location(event.pos, get_angle((player.rect.x, player.rect.y), event.pos))
    player.update_location()
    # изменяем ракурс камерв
    # camera.update(player)
    # # обновляем положение всех спрайтов
    # for sprite in all_sprites:
    #     camera.apply(sprite)
    all_tiles.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
