import pygame

class Button:
    def __init__(self, font, x=0, y=0, width=100, height=100, buttonText='Button',
                 onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': (255, 255, 255),
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

    def process(self):
        answer = None

        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill((255, 25, 255))
        self.buttonSurface.set_colorkey((255, 25, 255))
        pygame.draw.rect(self.buttonSurface, self.fillColors['normal'], (0, 0, self.width, self.height), 0, 20)
        if self.buttonRect.collidepoint(mousePos):
            pygame.draw.rect(self.buttonSurface, self.fillColors['hover'], (0, 0, self.width, self.height), 0, 20)

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                pygame.draw.rect(self.buttonSurface, self.fillColors['pressed'], (0, 0, self.width, self.height), 0, 20)

                if self.onePress:
                    answer = self.function_call(self.onclickFunction)

                elif not self.alreadyPressed:
                    answer = self.function_call(self.onclickFunction)
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])

        return answer

    def drawing(self, screen):
        screen.blit(self.buttonSurface, self.buttonRect)

    def function_call(self, fuction):
        try:
            return fuction()
        except TypeError:
            return
