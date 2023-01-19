import pygame
from animations import AnimatedSprite
from base_functions import load_image, distance_between_points, get_angle
from constants import *

from math import sin, cos, radians
from copy import deepcopy


class Player(AnimatedSprite):
    def __init__(self, pos_x, pos_y, group):
        player_image = load_image('character/Mage-M-01.png', -1)
        super().__init__(player_image, 3, 4, group)
        self.centering_x = (TILE_WIDTH - self.image.get_width()) // 2
        self.centering_y = (TILE_HEIGHT - self.image.get_height()) // 2
        self.rect = self.image.get_rect().move(
            (TILE_WIDTH * pos_x) + self.centering_x,
            (TILE_HEIGHT * pos_y) + self.centering_y)
        self.end_location = [self.rect.x, self.rect.y]
        self.v = 5
        self.dy = 0
        self.dx = 0

    def update_location(self):
        if self.rect.x == self.end_location[0] and self.rect.y == self.end_location[1]:
            self.stand_or_go = False
            return
        dist = distance_between_points((self.rect.x, self.rect.y), self.end_location)
        steps = dist // self.v
        try:
            self.dx = (self.end_location[0] - self.rect.x) / steps
            self.dy = (self.end_location[1] - self.rect.y) / steps
        except ZeroDivisionError:
            self.dx = 0
            self.dy = 0
        # if self.dx < 0:
        #     self.dx /= 2
        # if self.dy < 0:
        #     self.dy /= 2
        if self.dx > 0 and self.rect.x > self.end_location[0]:
            self.stand_or_go = False
            return
        elif self.dx < 0 and self.rect.x < self.end_location[0]:
            self.stand_or_go = False
            return
        if self.dy > 0 and self.rect.y > self.end_location[1]:
            self.stand_or_go = False
            return
        elif self.dy < 0 and self.rect.y < self.end_location[1]:
            self.stand_or_go = False
            return
        if (not self.dy > 0 and not self.dy < 0) and (not self.dx > 0 and not self.dx < 0):
            self.stand_or_go = False
            return
        self.stand_or_go = True
        angle = get_angle((self.rect.x, self.rect.y), self.end_location)
        if (45 <= angle < 90 or -90 < angle <= -45) or (angle == 0 and self.dx == 0):
            if self.dy < 0:
                self.update_animathion_line(2, 4, 1, 1)
            else:
                self.update_animathion_line(4, 4, 1, 3)
        else:
            if self.dx < 0:
                self.update_animathion_line(5, 4, 1, 4)
            else:
                self.update_animathion_line(3, 4, 1, 2)
        past_pos = self.rect.copy()
        self.rect.x += self.dx
        self.rect.y += self.dy

        if pygame.sprite.spritecollideany(self, impassable_cells):
            self.rect = past_pos.copy()
            self.end_location = [self.rect.x, self.rect.y]

    def new_duration(self, pos):
        if pygame.sprite.spritecollideany(self, impassable_cells):
            return
        self.end_location = [pos[0], pos[1]]
