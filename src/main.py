import os
import sys
import pygame
import pytmx
import time

from constants import *
from base_functions import *
from player import Player
from enemies import Skeleton
from generation_level import generate_level
from camera import Camera
from main_menu import menu_main
from UI import ui
from spells import Fireball
from new_level import new_lvl

menu_main()

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
is_fullscreen = False
last_size = screen.get_size()

lvl_now = 1
lvl_name_now = f'map{lvl_now}.tmx'
level_x, level_y, obstacle_map = generate_level(lvl_name_now)
enemies = list()
with open(f'../data/maps/map{lvl_now}.txt') as f:
    player_cord = tuple(map(int, f.readline().split()))
    for cord in f.readlines():
        norm_cord = tuple(map(int, cord.split()))
        enemies.append(Skeleton(norm_cord, enemies_group))

player = Player(player_cord, player_group)

spells = list()

win_cords = list()

camera = Camera()
amount_loops = 0

start = time.time()
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
                # Два раза написано специально, это какой-то баг pygame наверное, но если написать только один раз
                # то тогда после входы и выхода из полноэкранного режима пропадёт возможность менять размеры экрана
                screen = pygame.display.set_mode(last_size, pygame.RESIZABLE)
                screen = pygame.display.set_mode(last_size, pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            if player.energy > 20:
                spells.append(Fireball(player, player.rect.center, pygame.mouse.get_pos(), spells_group))

    amount_loops += 1
    player.update_location()
    for enemy in enemies:
        if enemy.process(player, obstacle_map, level_x, level_y, camera.sum_dx, camera.sum_dy) == 1:
            enemies.remove(enemy)
    if amount_loops >= 6:
        amount_loops = 0
        animated_sprites.update()
    for spell in spells:
        if spell.process() == 1:
            spells.remove(spell)
    player.characteristics()
    if not enemies:
        if cords := new_lvl(lvl_name_now, lvl_now, camera.sum_dx, camera.sum_dy):
            win_cords = cords
    if win_cords and get_tile_pos(player.rect.center, camera.sum_dx, camera.sum_dy) in win_cords:
        for tile in all_tiles:
            tile.kill()
        for player in player_group:
            player.kill()
        camera = Camera()
        win_cords = list()
        info = new_lvl(lvl_name_now, lvl_now,  camera.sum_dx, camera.sum_dy, True, time.time() - start)
        level_x, level_y, obstacle_map = info[:3]
        player = Player(info[3], player_group)
        lvl_now += 1
        lvl_name_now = f'map{lvl_now}.tmx'
        for enemy_cord in info[4]:
            enemies.append(Skeleton(enemy_cord, enemies_group))
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
