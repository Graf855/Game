import pygame
import pytmx

from map import Tile
from constants import TILE_WIDTH, TILE_HEIGHT, all_tiles
from generation_level import generate_level
from end_menu import end_menu

flag = True

def new_lvl(name, index,  shift_x, shift_y, next_lvl=False):
    global flag
    if next_lvl:
        index += 1
        flag = True
        try:
            level_x, level_y, level = generate_level(f'map{index}.tmx')
            with open(f'../data/maps/map{index}.txt') as f:
                player_cord = tuple(map(int, f.readline().split()))
                enemies_cords = list()
                for cord in f.readlines():
                    norm_cord = tuple(map(int, cord.split()))
                    enemies_cords.append(norm_cord)
            return level_x, level_y, level, player_cord, enemies_cords
        except FileNotFoundError:
            end_menu(True)
    if not flag:
        return
    level = pytmx.load_pygame(f'../data/maps/{name}')
    win_layer = level.layers[-1]
    cords = list()
    for x, y, image in win_layer.tiles():
        Tile(image, 2, TILE_WIDTH * x + shift_x, TILE_HEIGHT * y + shift_y, all_tiles)
        cords.append((x, y))
    flag = False
    return cords
