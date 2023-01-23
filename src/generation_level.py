from map import Tile
from player import Player
from constants import *

import pytmx

# def generate_level(level):
#     new_player, x, y, obstacle_map = None, None, None, list()
#     for y in range(len(level)):
#         obstacle_map.append(list())
#         for x in range(len(level[y])):
#             if level[y][x] == '.':
#                 obstacle_map[y].append(0)
#                 Tile('empty', x, y, all_tiles)
#             elif level[y][x] == '#':
#                 obstacle_map[y].append(1)
#                 Tile('wall', x, y, all_tiles, impassable_cells)
#             elif level[y][x] == '@':
#                 obstacle_map[y].append(0)
#                 Tile('empty', x, y, all_tiles)
#                 new_player = Player(x, y, player_group)
#     # вернем игрока, а также размер поля в клетках и карту препятствий
#     return new_player, x, y, obstacle_map


def generate_level(name):
    level = pytmx.load_pygame(f'../data/maps/{name}')
    x, y, obstacle_map = None, None, list()
    for i, layer in enumerate(level.visible_layers):
        for x, y, image in layer.tiles():
            if i == 0:
                if level.get_tile_gid(x, y, i) in (1, 5, 3, 10, 11, 12, 7, 4, 2):
                    Tile(image, 1, TILE_WIDTH * x, TILE_HEIGHT * y, all_tiles, impassable_cells)
                    obstacle_map.append(1)
                else:
                    Tile(image, 0, TILE_WIDTH * x, TILE_HEIGHT * y, all_tiles)
                    obstacle_map.append(0)
            else:
                if level.get_tile_gid(x, y, i) in (13, 14, 15, 16, 17, 18, 19, 20, 21):
                    Tile(image, 1, TILE_WIDTH * x, TILE_HEIGHT * y, all_tiles, impassable_cells)
                    obstacle_map[x * y] = 1
                else:
                    Tile(image, 0, TILE_WIDTH * x, TILE_HEIGHT * y, all_tiles)
    return x, y, obstacle_map

