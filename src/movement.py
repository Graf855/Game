import pygame as pg
from collections import deque
import sys

from constants import *
from base_functions import *

def shortest_way_through_cells(start_cell_pos, end_cell_pos, level, level_x, level_y):
    # dict of adjacency lists
    graph = {}
    shortest_way = list()
    for y, row in enumerate(level):
        for x, col in enumerate(row):
            if not col:
                graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(level, x, y, level_x, level_y)

    queue, visited = bfs(start_cell_pos, end_cell_pos, graph)
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

def next_move(point1, point2, dist, v):
    steps = dist // v
    if steps == 0:
        return 0, 0
    dx = (point2[0] - point1[0]) / steps
    dy = (point2[1] - point1[1]) / steps
    return dx, dy
