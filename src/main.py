import os
import sys
import pygame
import pytmx

from constants import *
from base_functions import *
from player import Player
from generation_level import generate_level
from camera import Camera

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)

level_x, level_y, obstacle_map = generate_level('basik.tmx')
player = Player(3, 18, player_group)

camera = Camera()
amount_loops = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.new_duration(event.pos)
    amount_loops += 1
    player.update_location()
    if amount_loops >= 10:
        amount_loops = 0
        animated_sprites.update()
    camera.update(player)
    camera.apply_player_end_pos(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill((0, 0, 0))
    all_tiles.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
