from map import Tile
from player import Player
from constants import *

def generate_level(level):
    new_player, x, y, obstacle_map = None, None, None, list()
    for y in range(len(level)):
        obstacle_map.append(list())
        for x in range(len(level[y])):
            if level[y][x] == '.':
                obstacle_map[y].append(0)
                Tile('empty', x, y, all_tiles)
            elif level[y][x] == '#':
                obstacle_map[y].append(1)
                Tile('wall', x, y, all_tiles, impassable_cells)
            elif level[y][x] == '@':
                obstacle_map[y].append(0)
                Tile('empty', x, y, all_tiles)
                new_player = Player(x, y, player_group)
    # вернем игрока, а также размер поля в клетках и карту препятствий
    return new_player, x, y, obstacle_map
