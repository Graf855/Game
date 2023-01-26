# Imports
import sys
import pygame

from constants import *
from base_functions import *
from button import Button
from show_text import show_text

def end_menu(win, time=0, flag_new_time=False):
    pygame.init()
    menu_screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    font = pygame.font.Font('../data/fonts/123.ttf', 40)
    objects = list()
    objects.append(Button(font, 220, 260, 200, 50, 'QUIT', terminate))
    is_fullscreen = False
    virtual_screen = pygame.Surface(SIZE)
    scaled_screen = pygame.Surface(SIZE)

    background = load_image('background/default_picture_for_backgroung.jpg')
    background = pygame.transform.scale(background, SIZE)

    if win:
        text = ['ПОЗДРАВЛЯЕМ!', "Вы победили"]
        color = (255, 0, 0)
        if flag_new_time:
            text.append('К тому же')
            text.append("вы поставили новое время!!!")
        else:
            text.append('К сожелению')
            text.append('вы не поставили новый')
            text.append('рекорд')
    else:
        with open('../data/score/score.txt', mode='r') as f:
            time = float(f.readline())
        text = ['К сожелению', "Вы проиграли"]
        color = (0, 255, 0)
    text_time = [f'Ваше лучшее время {time:.2f}']
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    menu_screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
                else:
                    # Два раза написано специально, это какой-то баг pygame наверное, но если написать только один раз
                    # то тогда после входы и выхода из полноэкранного режима пропадёт возможность менять размеры экрана
                    menu_screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
                    menu_screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
        virtual_screen.fill((0, 0, 0))
        virtual_screen.blit(background, (0, 0))
        new_size = menu_screen.get_size()
        past_size = scaled_screen.get_size()
        scaled_screen = pygame.transform.scale(virtual_screen, new_size)
        for object in objects:
            object.change_buttonRect(new_size[0] / past_size[0], new_size[1] / past_size[1])
            object.drawing(scaled_screen)
            object.process()
        show_text(scaled_screen, font, text, (100, 10), new_size[0] / past_size[0], new_size[1] / past_size[1], color)
        show_text(scaled_screen, font, text_time, (50, 300), new_size[0] / past_size[0], new_size[1] / past_size[1],
                  color)
        menu_screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    menu_main()
