import pygame as pg
from random import random
from collections import deque
import sys

from constants import *


def shortest_way_through_cells(start_pos, end_pos, level, level_x, level_y):
    # dict of adjacency lists
    graph = {}
    shortest_way = list()
    for y, row in enumerate(level):
        for x, col in enumerate(row):
            if not col:
                graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(level, x, y, level_x, level_y)

    queue, visited = bfs(start_pos, end_pos, graph)
    # draw path
    path_segment = end_pos
    while path_segment and path_segment in visited:
        shortest_way.append(path_segment)
        path_segment = visited[path_segment]
    return shortest_way

def get_next_nodes(grid, x, y, level_x, level_y):
    check_next_node = lambda x1, y1: True if 0 <= x1 < level_x and 0 <= y1 < level_y and not grid[y1][x1] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
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

# obstacle_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# print(shortest_way((1, 1), (4, 1), obstacle_map, 11, 11))
