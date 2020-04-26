import pygame
from pygame.sprite import Sprite


class Covid(Sprite):
    """класс представляет 1 вируса"""
    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию"""
        super(Covid, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # загрузка  вируса
        self.image = pygame.image.load('images/covid2.bmp')
        self.rect = self.image.get_rect()
        # каждый новый вирус появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # сохраняем позицию
        self.x = float(self.rect.x)

    def blitme(self):
        """рисует вирус в текущем состоянии"""
        self.screen.blit(self.image, self.rect)
