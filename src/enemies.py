import pygame
from animations import AnimatedSprite
from base_functions import *
from constants import *

from movement import shortest_way_through_cells


class Skeleton(AnimatedSprite):
    def __init__(self, pos_x, pos_y, group):
        player_image = load_image('enemies/skelet.png', -1)
        super().__init__(player_image, 3, 4, group)
        centering_x = (TILE_WIDTH - self.image.get_width()) // 2
        centering_y = (TILE_HEIGHT - self.image.get_height()) // 2
        self.rect = self.image.get_rect().move(
            (TILE_WIDTH * pos_x) + centering_x,
            (TILE_HEIGHT * pos_y) + centering_y)
        self.stand_or_go = False
        self.v = 2
        self.dy = 0
        self.dx = 0
        self.damage = 1

    def process(self, aim, level, level_x, level_y, shift_x, shift_y, flag=True, tile_points=None):
        start_tile_pos = self.self_cords(shift_x, shift_y)
        end_tile_pos = get_tile_pos((aim.rect.x + aim.rect.width // 2, aim.rect.y + aim.rect.height // 2),
                                    shift_x, shift_y)
        if flag:
            tile_points = shortest_way_through_cells(start_tile_pos, end_tile_pos, level, level_x, level_y)

        try:
            point = list(map(lambda x: get_central_pos_from_tile(x, shift_x, shift_y), tile_points))[-2]
        except IndexError:
            return

        dist = distance_between_points((self.rect.x, self.rect.y), point)
        steps = dist // self.v
        try:
            self.dx = (point[0] - self.rect.x) / steps
            self.dy = (point[1] - self.rect.y) / steps
        except ZeroDivisionError:
            self.dx = 0
            self.dy = 0

        self.stand_or_go = True
        game_angle = get_game_angle((self.rect.x, self.rect.y), point)
        if 135 >= game_angle >= 45:
            self.update_animathion_line(2, 4, 1, 1)
        elif 225 <= game_angle <= 315:
            self.update_animathion_line(4, 4, 1, 3)
        elif 135 < game_angle < 225:
            self.update_animathion_line(3, 4, 1, 2)
        else:
            self.update_animathion_line(5, 4, 1, 4)

        past_pos = self.rect.copy()
        self.rect.x += self.dx
        self.rect.y += self.dy

        if pygame.sprite.spritecollideany(self, player_group):
            aim.health -= self.damage
            self.rect = past_pos.copy()

        if len(enemy := pygame.sprite.spritecollide(self, enemies_group, False)) > 1:
            self.rect = past_pos.copy()

    def self_cords(self, shift_x, shift_y):
        return get_tile_pos((self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2),
                            shift_x, shift_y)
