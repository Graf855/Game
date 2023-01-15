import os
import sys
import pygame

from constants import *
from base_functions import *
from generation_level import generate_level
from camera import Camera
from shortest_way import shortest_way

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)

level = load_level(f'map1.txt')
player, level_x, level_y, obstacle_map = generate_level(level)

amount_loops = 0

camera = Camera()
points = None

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
            start = get_tile_pos((player.rect.x, player.rect.y), camera.sum_dx, camera.sum_dy)
            end = get_tile_pos(event.pos, camera.sum_dx, camera.sum_dy)
            tile_points = shortest_way(start, end, obstacle_map, level_x, level_y)
            points = list(map(lambda x: get_pos_from_tile(x, camera.sum_dx, camera.sum_dy), tile_points))
    # изменяем ракурс камерв
    # camera.update(player)
    # # обновляем положение всех спрайтов
    # for sprite in all_sprites:
    #     camera.apply(sprite)
    amount_loops += 1
    screen.fill((0, 0, 0))
    if amount_loops == 10:
        # animated_sprites.update()
        amount_loops = 0
    all_tiles.draw(screen)
    player_group.draw(screen)
    if points:
        pygame.draw.lines(screen, (255, 255, 255), False, points)
    pygame.display.flip()
    clock.tick(FPS)
