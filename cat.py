import pygame


class Cat:

    def __init__(self, screen):
        # init кота и задает его начальную позицию
        self.screen = screen

        # загружаю кота и получаю прямоугольник
        self.image = pygame.image.load('images/cat2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый кот появляется у нижнего края
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def bltime(self):
        # рисует кота в текущей позиции
        self.screen.blit(self.image, self.rect)