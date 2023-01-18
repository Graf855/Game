import pygame as pg
# from random import random
from collections import deque
import sys
# import time

from constants import *
from base_functions import *


def shortest_way_through_cells(start_cell_pos, end_cell_pos, level, level_x, level_y):
    # level[start_cell_pos[1]][start_cell_pos[0]] = 0
    # level[end_cell_pos[1]][end_cell_pos[0]] = 0
    # dict of adjacency lists
    graph = {}
    shortest_way = list()
    for y, row in enumerate(level):
        for x, col in enumerate(row):
            if not col:
                graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(level, x, y, level_x, level_y)

    queue, visited = bfs(start_cell_pos, end_cell_pos, graph)
    # draw path
    path_segment = end_cell_pos
    while path_segment in visited:
        shortest_way.append(path_segment)
        path_segment = visited[path_segment]
    return shortest_way

def get_next_nodes(grid, x, y, level_x, level_y):
    check_next_node = lambda x1, y1: True if 0 <= x1 < level_x and 0 <= y1 < level_y and not grid[y1][x1] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    # ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return queue, visited


# obstacle_map = [[1 if random() < 0.2 else 0 for col in range(1000)] for row in range(1000)]
# start = time.time()
# # obstacle_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# shortest_way_through_cells((1, 1), (998, 998), obstacle_map, 1000, 1000)
# end = time.time() - start
# print(end)

# def the_shortest_way(start_pos, end_pos, level, level_x, level_y, shift_x, shift_y):
#     shortest_way = [start_pos]
#     start_cell_pos = get_tile_pos(start_pos, shift_x, shift_y)
#     end_cell_pos = get_tile_pos(end_pos, shift_x, shift_y)
#     cords_cells = shortest_way_through_cells(start_cell_pos, end_cell_pos, level, level_x, level_y)
#     norm_cords = list(map(lambda x: get_central_pos_from_tile(x, shift_x, shift_y), cords_cells[:-1]))
#     norm_cords = norm_cords[::-1]
#     past_point = start_pos
#     norm_cords.append(end_pos)
#     new_point = [0, 0]
#     for point in norm_cords:
#         distance = distance_between_points(past_point, point)
#         koef = distance / TILE_WIDTH * 20
#         increase_x = (point[0] - past_point[0]) / koef
#         increase_y = (point[1] - past_point[1]) / koef
#         for i in range(int(koef)):
#             new_point[0] = past_point[0] + increase_x * i
#             new_point[1] = past_point[1] + increase_y * i
#             pos_cell = get_tile_pos(new_point, shift_x, shift_y)
#             if level[pos_cell[1]][pos_cell[0]] == 1:
#                 shortest_way.append(past_point)
#                 past_point = point
#                 break
#     shortest_way.append(end_pos)
#     print(shortest_way)
#     return shortest_way

# def the_shortest_way(start_pos, end_pos, level, level_x, level_y, shift_x, shift_y):
#     shortest_way = [start_pos]
#     start_cell_pos = get_tile_pos(start_pos, shift_x, shift_y)
#     end_cell_pos = get_tile_pos(end_pos, shift_x, shift_y)
#     cords_cells = shortest_way_through_cells(start_cell_pos, end_cell_pos, level, level_x, level_y)
#     norm_cords = list(map(lambda x: get_central_pos_from_tile(x, shift_x, shift_y), cords_cells[:-1]))
#     norm_cords = norm_cords[::-1]
#     past_point = start_pos
#     point_before_point = start_pos
#     norm_cords.append(end_pos)
#     for point in norm_cords:
#         ox, oy = point_before_point
#         xm, ym = mapping(ox, oy)
#         distance = distance_between_points(past_point, point)
#         sin_a = (point[1] - past_point[1]) / distance
#         cos_a = (point[0] - past_point[0]) / distance
#         sin_a = sin_a if sin_a else 0.000001
#         cos_a = cos_a if cos_a else 0.000001
#
#         # verticals
#         x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
#         for i in range(0, int(distance), TILE):
#             depth_v = (x - ox) / cos_a
#             y = oy + depth_v * sin_a
#             # if mapping(x + dx, y) in world_map:
#             #     break
#             pos_cell = get_tile_pos((x + dx, y), shift_x, shift_y)
#             if level[pos_cell[1]][pos_cell[0]] == 1:
#                 break
#             x += dx * TILE
#
#         # horizontals
#         y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
#         for i in range(0, int(distance), TILE):
#             depth_h = (y - oy) / sin_a
#             x = ox + depth_h * cos_a
#             # if mapping(x, y + dy) in world_map:
#             #     break
#             pos_cell = get_tile_pos((x, y + dy), shift_x, shift_y)
#             if level[pos_cell[1]][pos_cell[0]] == 1:
#                 break
#             y += dy * TILE
#
#         # projection
#         depth = depth_v if depth_v < depth_h else depth_h
#
#         if depth < distance:
#             shortest_way.append(point_before_point)
#             past_point = point_before_point
#
#         point_before_point = point

# def the_shortest_way(start_pos, end_pos, level, level_x, level_y, shift_x, shift_y):
#     shortest_way = [start_pos]
#     start_cell_pos = get_tile_pos(start_pos, shift_x, shift_y)
#     end_cell_pos = get_tile_pos(end_pos, shift_x, shift_y)
#     cords_cells = shortest_way_through_cells(start_cell_pos, end_cell_pos, level, level_x, level_y)
#     norm_cords = list(map(lambda x: get_central_pos_from_tile(x, shift_x, shift_y), cords_cells[:-1]))
#     norm_cords = norm_cords[::-1]
#     past_point = point_before_point = start_pos
#     norm_cords.append(end_pos)
#     for point in norm_cords:
#         ox, oy = point_before_point
#         xm, ym = mapping(ox, oy)
#         distance = distance_between_points(past_point, point)
#         sin_a = (point[1] - past_point[1]) / distance
#         cos_a = (point[0] - past_point[0]) / distance
#         sin_a = sin_a if sin_a else 0.000001
#         cos_a = cos_a if cos_a else 0.000001


def the_shortest_way(start_pos, end_pos, level, level_x, level_y, shift_x, shift_y):
    shortest_way = [start_pos]
    start_cell_pos = get_tile_pos(start_pos, shift_x, shift_y)
    end_cell_pos = get_tile_pos(end_pos, shift_x, shift_y)
    cords_cells = shortest_way_through_cells(start_cell_pos, end_cell_pos, level, level_x, level_y)
    norm_cords = list(map(lambda x: get_central_pos_from_tile(x, shift_x, shift_y), cords_cells[:-1]))
    norm_cords = norm_cords[::-1]
    past_point = point_before_point = start_pos
    norm_cords[-1] = end_pos
    for point in norm_cords:
        ans = raycast(past_point, point, level, shift_x, shift_y)
        print(ans)
        if not raycast(past_point, point, level, shift_x, shift_y):
            shortest_way.append(point_before_point)
            past_point = point_before_point
        point_before_point = point
    shortest_way.append(end_pos)
    return shortest_way

def raycast(point1, point2, level, shift_x, shift_y):
    dist = distance_between_points(point1, point2)
    dist_x = point1[0] - point2[0]
    dist_y = point1[1] - point2[1]
    if dist_x == 0:
        angle = 0
    else:
        angle = angle_from_tg_in_radians(dist_y / dist_x)
    xo, yo = point1
    sin_a = dist_y / dist
    cos_a = dist_x / dist
    # sin_a = sin(angle)
    # cos_a = cos(angle)
    for depth in range(int(dist)):
        x = xo + depth * cos_a
        y = yo + depth * sin_a
        pos = get_tile_pos((x, y), shift_x, shift_y)
        if level[pos[1]][pos[0]] == 1:
            return False
    return True

