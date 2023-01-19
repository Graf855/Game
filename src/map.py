import os
import sys

import pygame

from constants import *
from base_functions import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, tile_type, pos_x, pos_y, *tile_group):
        super().__init__(all_sprites, tile_group)
        self.type = tile_type
        self.image = image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
