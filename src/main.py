import os
import sys
import pygame
import pytmx

from constants import *
from base_functions import *
from player import Player
from enemies import Skeleton
from generation_level import generate_level
from camera import Camera
from main_menu import menu_main
from UI import ui
from spells import Fireball

menu_main()

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
is_fullscreen = False
last_size = screen.get_size()

level_x, level_y, obstacle_map = generate_level('map1.tmx')

player = Player(1, 8, player_group)
enemies = list()
enemies.append(Skeleton(8, 7, enemies_group))

spells = list()

camera = Camera()
amount_loops = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            player.new_duration(event.pos)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            is_fullscreen = not is_fullscreen
            if is_fullscreen:
                last_size = screen.get_size()
                screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode(last_size, pygame.RESIZABLE)
                screen = pygame.display.set_mode(last_size, pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            if player.energy > 20:
                spells.append(Fireball(player, player.rect.center, pygame.mouse.get_pos(), spells_group))

    amount_loops += 1
    player.update_location()
    for enemy in enemies:
        enemy.process(player, obstacle_map, level_x, level_y, camera.sum_dx, camera.sum_dy)
    if amount_loops >= 6:
        amount_loops = 0
        animated_sprites.update()
    for spell in spells:
        if spell.process() == 1:
            spells.remove(spell)
    player.characteristics()
    camera.update(player, screen.get_size())
    camera.apply_player_end_pos(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill((0, 0, 0))
    all_tiles.draw(screen)
    player_group.draw(screen)
    spells_group.draw(screen)
    enemies_group.draw(screen)
    ui(screen, player.health, player.energy)
    pygame.display.flip()
    clock.tick(FPS)
