import pygame
from pygame.sprite import Sprite


class Covid(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Covid, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # загрузка  covida
        self.image = pygame.image.load('images/covid.bmp')
        self.rect = self.image.get_rect()
        # каждый новый вирус появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # сохраняем позицию
        self.x = float(self.rect.x)

    def blitme(self):
        """рисует covid в текущем состоянии"""
        self.screen.blit(self.image, self.rect)
