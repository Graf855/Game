from map import Tile
from player import Player
from constants import *

import pytmx


def generate_level(name):
    level = pytmx.load_pygame(f'../data/maps/{name}')
    x, y, obstacle_map = None, None, list(list())
    for i, layer in enumerate(level.visible_layers):
        for x, y, image in layer.tiles():
            if y != len(obstacle_map) - 1:
                obstacle_map.append(list())
            if i == 0:
                Tile(image, 1, TILE_WIDTH * x, TILE_HEIGHT * y, all_tiles)
                obstacle_map[y].append(0)
            elif i == 2 or i == 1:
                Tile(image, 1, TILE_WIDTH * x, TILE_HEIGHT * y, all_tiles, impassable_cells)
                obstacle_map[y][x] = 1
    while not obstacle_map[-1]:
        obstacle_map.pop(-1)
    return len(obstacle_map[0]) - 1, len(obstacle_map) - 1, obstacle_map
