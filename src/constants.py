import pygame

# main
FPS = 30
SIZE = WIDTH, HEIGHT = 1000, 920
# tiles
TILE = TILE_WIDTH = TILE_HEIGHT = 32

# sprites' groups
all_sprites = pygame.sprite.Group()
all_tiles = pygame.sprite.Group()
impassable_cells = pygame.sprite.Group()
player_group = pygame.sprite.Group()
animated_sprites = pygame.sprite.Group()
