import pygame

from base_functions import *
from constants import *
from animations import AnimatedSprite

class Fireball(AnimatedSprite):
    def __init__(self, player, pos, end_pos, group):
        fireball_image = pygame.transform.flip(load_image('spells/fireball.png'), True, True)
        fireball_image = pygame.transform.scale(fireball_image, (70, 70))
        angle = get_game_angle(pos, end_pos)
        super().__init__(fireball_image, 2, 2, group)
        self.rotate(angle)
        self.rect = self.image.get_rect().move(
            pos[0] - self.image.get_width() // 2,
            pos[0] - self.image.get_height() // 2)
        self.v = 8
        self.damage = 10
        self.cost = 20
        self.calculation_d(pos, end_pos)
        player.energy -= self.cost
        self.mask = pygame.mask.from_surface(self.image)
        if player.energy <= 0:
            player.energy = 1

    def calculation_d(self, pos1, pos2):
        dist = distance_between_points(pos1, pos2)
        dist_x = pos1[0] - pos2[0]
        dist_y = pos1[1] - pos2[1]
        sin_a = dist_y / dist
        cos_a = dist_x / dist
        self.dy = sin_a * self.v
        self.dx = cos_a * self.v

    def process(self):
        past_pos = self.rect.copy()
        self.rect.x -= self.dx
        self.rect.y -= self.dy

        if enemy := pygame.sprite.spritecollide(self, enemies_group, False):
            self.rect = past_pos.copy()
            enemy[0].health -= self.damage
            self.kill()
            return 1

        if tiles := pygame.sprite.spritecollide(self, impassable_cells, False):
            for tile in tiles:
                if pygame.sprite.collide_mask(self, tile):
                    self.kill()
                    return 1
