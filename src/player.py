import pygame
from animations import AnimatedSprite
from base_functions import load_image
from constants import *

class Player(AnimatedSprite):
    def __init__(self, pos_x, pos_y, group):
        player_image = load_image('character/Mage-M-01.png', -1)
        super().__init__(player_image, 3, 4, group)
        self.centering_x = (TILE_WIDTH - self.image.get_width()) // 2
        self.centering_y = (TILE_HEIGHT - self.image.get_height()) // 2
        self.rect = self.image.get_rect().move(
            (TILE_WIDTH * pos_x) + self.centering_x,
            (TILE_HEIGHT * pos_y) + self.centering_y)
        self.currect_location = self.rect
        self.v = 20

    def update_location(self, x_or_y, shift):
        # if self.currect_location == self.rect:
        #     self.cur_frames = self.cur_frames[1]
        # else:
        #     pass
        new_rect = self.rect.copy()
        if x_or_y == 0:
            self.rect.x += TILE_WIDTH * shift
            if shift == 1:
                self.update_animathion_line(3, 4, 1, 2)
            else:
                self.update_animathion_line(5, 4, 1, 4)
        else:
            self.rect.y += TILE_HEIGHT * shift
            if shift == 1:
                self.update_animathion_line(4, 4, 1, 3)
            else:
                self.update_animathion_line(2, 4, 1, 1)
        # на случай если можно выйти за границы карты
        try:
            if pygame.sprite.spritecollide(self, all_tiles, False)[0].type == 'wall':
                self.rect = new_rect.copy()
            else:
                self.update()
        except IndexError:
            self.rect = new_rect.copy()

    def new_location(self, pos):
        self.currect_location.x = pos[0]
        self.currect_location.y = pos[1]
