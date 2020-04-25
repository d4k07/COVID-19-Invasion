import sys
import pygame
from settings import Settings
from cat import Cat
import game_functions as gf


def run_game():
    # инициализирует pygame, settings, экран
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("COVID-19 invasion")
    # создание кота
    cat = Cat(screen)
    # тут цвет фона
    bg_color = (230, 230, 230)
    # основной цикл игры
    while True:
        # отслеживание событий клавы и мыши
        gf.check_events()
        # перерисовывается экран
        screen.fill(ai_settings.bg_color)
        cat.bltime()
        # отображение последней прорисовки экрана
        pygame.display.flip()


run_game()
