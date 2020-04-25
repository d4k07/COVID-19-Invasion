import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулями кота"""

    def __init__(self, ai_settings, screen, cat):
        """создает обьект пули в текущем положении кота"""
        super(Bullet, self).__init__()
        self.screen = screen

        # создание пули и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = cat.rect.centerx
        self.rect.top = cat.rect.top

        # позиция пули в флоат!
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """двигает пулю по экрану ^"""
        # обновить позиции пули
        self.y -= self.speed_factor
        # обновить позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """рисует пульки на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)