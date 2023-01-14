from base_functions import load_image

# main
FPS = 50
SIZE = WIDTH, HEIGHT = 500, 500
# tiles
TILE_WIDTH = TALE_HEIGHT = 32
TILE_IMAGES = {
    'wall': load_image('default_tiles_x (2).png').subsurface(pygame.Rect(32, 0, 32, 32)),
    'empty': load_image('default_tiles_x (2).png').subsurface(pygame.Rect(0, 0, 32, 32))
}

# player
PLAYER_IMAGE = load_image('Mage-M-01.png', -1)

# sprites' groups
all_sprites = pygame.sprite.Group()
all_tiles = pygame.sprite.Group()
player_group = pygame.sprite.Group()
animated_spites = pygame.sprite.Group()
