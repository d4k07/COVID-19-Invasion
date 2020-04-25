import pygame


class Cat:

    def __init__(self, ai_settings, screen):
        # init кота и задает его начальную позицию
        self.screen = screen
        self.ai_settings = ai_settings

        # загружаю кота и получаю прямоугольник
        self.image = pygame.image.load('images/cat2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый кот появляется у нижнего края окна
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # сохранение вещественной координаты центра
        self.center = float(self.rect.centerx)

        # флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # обновление позиции кота по флагу
        # обновить атрибут center вместо rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.cat_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.cat_speed_factor

        # rect на основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        # рисует кота в текущей позиции
        self.screen.blit(self.image, self.rect)
