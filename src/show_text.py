import pygame

def show_text(screen, font, text, text_pos, scale_x, scale_y, color):
    text_x = text_pos[0]
    text_y = text_pos[1]
    for line in text:
        string_rendered = font.render(line, 1, color)
        intro_rect = string_rendered.get_rect()
        text_y += 10
        intro_rect.top = text_y
        intro_rect.x = text_x
        text_y += intro_rect.height
        intro_rect.x *= scale_x
        intro_rect.y *= scale_y
        intro_rect.width *= scale_x
        intro_rect.height *= scale_y
        screen.blit(string_rendered, intro_rect)
