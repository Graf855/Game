import os
import sys

import pygame

from constants import *
from base_functions import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        TILE_IMAGES = {
            'wall': load_image('tiles/default_tiles.png').subsurface(pygame.Rect(32, 0, 32, 32)),
            'empty': load_image('tiles/default_tiles.png').subsurface(pygame.Rect(0, 0, 32, 32))
        }
        super().__init__(all_tiles, all_sprites)
        self.type = tile_type
        self.image = TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)
