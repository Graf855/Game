import pygame
from constants import *


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, group, x=0, y=0):
        super().__init__(animated_sprites, all_sprites, group)
        self.frames = []
        self.columns = columns
        self.rows = rows
        self.cut_sheet(sheet, columns, rows)
        self.cur_frames = list()
        self.update_animathion_line(rows + 1, columns + 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.stand_or_go = True

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        if self.stand_or_go:
            self.cur_frame = (self.cur_frame + 1) % len(self.cur_frames)
        else:
            self.cur_frame = 0
        try:
            self.image = self.frames[self.cur_frames[self.cur_frame]]
        except ZeroDivisionError:
            print('выбран неверный диапозон значений')

    def update_animathion_line(self, finish_indent_y, finish_indent_x,
                               start_indent_x=1, start_indent_y=1):
        self.cur_frames = list()
        first_elem = self.columns * (start_indent_y - 1) - 1 + start_indent_x
        for i in range(finish_indent_y - start_indent_y):
            for j in range(finish_indent_x - start_indent_x):
                self.cur_frames.append(first_elem + j + i * self.columns)
