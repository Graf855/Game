import pygame
from base_functions import load_image

def ui(screen, hp, energe):
    hp_image_bar = load_image('UI/hp_bar.png')
    energe_image_bar = load_image('UI/energy_bar.png')
    pygame.draw.rect(hp_image_bar, (255, 0, 0), (35, 15, 2 * hp, 10))
    pygame.draw.rect(energe_image_bar, (255, 186, 0), (35, 15, 2 * energe, 10))
    screen.blit(hp_image_bar, (5, 5))
    screen.blit(energe_image_bar, (5, 50))

