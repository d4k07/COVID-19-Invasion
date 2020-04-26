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
    # Создание вируса
    covid = Covid(ai_settings, screen)
    # храним группы пуль и группы вирусов
    bullets = Group()
    covids = Group()
    # создание флота
    gf.create_fleet(ai_settings, screen, covids)
    # тут цвет фона
    bg_color = (255, 255, 255)
    # основной цикл игры
    while True:
        # цикл заменить на доп функции
        gf.check_events(ai_settings, screen, cat, bullets)
        cat.update()
        bullets.update()
        gf.update_bullets(bullets)
        # gf.update_screen(ai_settings, screen, cat, covid, bullets)
        gf.update_screen(ai_settings, screen, cat, covids, bullets)


run_game()
