# main
import pygame
from settings import Settings
from cat import Cat
import game_functions as gf
from pygame.sprite import Group
from covid import Covid


def run_game():
    # инициализирует pygame, settings, экран
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("COVID-19 invasion")
    # создание кота
    cat = Cat(ai_settings, screen)
    # храним пули
    bullets = Group()
    # Создание вируса
    covid = Covid(ai_settings, screen)
    # тут цвет фона
    bg_color = (230, 230, 230)
    # основной цикл игры
    while True:
        # цикл заменить на доп функции
        gf.check_events(ai_settings, screen, cat, bullets)
        cat.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, cat, covid, bullets)


run_game()
