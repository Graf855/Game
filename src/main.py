import os
import sys
import pygame

from constants import *
from base_functions import terminate

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    pygame.display.flip()
    clock.tick(FPS)
