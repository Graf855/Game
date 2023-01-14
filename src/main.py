import os
import sys
import pygame

from constants import *
from base_functions import terminate, load_level
from generation_level import generate_level

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

player, level_x, level_y = generate_level(load_level(f'map1.txt'))

amount_loops = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    pygame.display.flip()
    clock.tick(FPS)
