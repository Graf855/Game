import pygame
from animations import AnimatedSprite
from base_functions import load_image
from constants import *

from math import sin, cos, radians

class Player(AnimatedSprite):
    def __init__(self, pos_x, pos_y, group):
        player_image = load_image('character/Mage-M-01.png', -1)
        super().__init__(player_image, 3, 4, group)
        self.centering_x = (TILE_WIDTH - self.image.get_width()) // 2
        self.centering_y = (TILE_HEIGHT - self.image.get_height()) // 2
        self.rect = self.image.get_rect().move(
            (TILE_WIDTH * pos_x) + self.centering_x,
            (TILE_HEIGHT * pos_y) + self.centering_y)
        self.angle = 0
        self.end_l_more_or_less = 0
        self.end_location = self.rect.copy()
        self.v = 20

    def update_location(self):
        if self.end_location.x * self.end_l_more_or_less > self.rect.x:
            self.stand_or_go = False
            return
        self.stand_or_go = True
        increase_x = cos(radians(self.angle)) * self.v
        increase_y = sin(radians(self.angle)) * self.v
        new_rect = self.rect.copy()
        if self.end_location.x > self.rect.x:
            self.rect.x += increase_x
            self.rect.y += increase_y
        else:
            self.rect.x -= increase_x
            self.rect.y -= increase_y
        # new_rect = self.rect.copy()
        # if x_or_y == 0:
        #     self.rect.x += TILE_WIDTH * shift
        #     if shift == 1:
        #         # вправо
        #         self.update_animathion_line(3, 4, 1, 2)
        #     else:
        #         # влево
        #         self.update_animathion_line(5, 4, 1, 4)
        # else:
        #     self.rect.y += TILE_HEIGHT * shift
        #     if shift == 1:
        #         # вниз
        #         self.update_animathion_line(4, 4, 1, 3)
        #     else:
        #         # вверх
        #         self.update_animathion_line(2, 4, 1, 1)
        # # на случай если можно выйти за границы карты
        # try:
        #     if pygame.sprite.spritecollide(self, all_tiles, False)[0].type == 'wall':
        #         self.rect = new_rect.copy()
        #     else:
        #         self.update()
        # except IndexError:
        #     self.rect = new_rect.copy()

    def new_location(self, pos, new_angle):
        if pos[0] > self.rect.x:
            self.end_l_more_or_less = 1
        elif pos[0] < self.rect.x:
            self.end_l_more_or_less = -1
        else:
            self.end_l_more_or_less = 0
        self.end_location.x = pos[0]
        self.end_location.y = pos[1]
        self.angle = new_angle
