import pygame
from constants import *

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = self.sum_dx = -8
        self.dy = self.sum_dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + 36 - WIDTH // 2)
        self.dy = -(target.rect.y + 48 - HEIGHT // 2)
        self.sum_dx += self.dx
        self.sum_dy += self.dy
