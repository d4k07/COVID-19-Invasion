import sys
import pygame
from bullet import Bullet
from covid import Covid

"""тут упрощение основного кода"""


def check_keydown_events(event, ai_settings, screen, cat, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        # Двинуть кота вправо
        # cat.rect.centerx += 1
        cat.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Двинуть кота влево
        # cat.rect.centerx -= 1
        cat.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, cat, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, cat, bullets):
    """пускает пулю если не макс."""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, cat)
        bullets.add(new_bullet)


def check_keyup_events(event, cat):
    """Реагирует на отпускание клавиш"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            cat.moving_right = False
        elif event.key == pygame.K_LEFT:
            cat.moving_left = False


def check_events(ai_settings, screen, cat, bullets):
    # обрабатывает нажатия клавиш и мышки
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, cat, bullets)
        elif event.type == pygame.KEYUP:
            check_keydown_events(event, ai_settings, screen, cat, bullets)


def update_screen(ai_settings, screen, cat, covids, bullets):
    """Обновляет изображения на экране и отображает новый экран"""
    # при каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    # все пули позади кота и ковидов
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    cat.blitme()
    # covid.blitme()
    covids.draw(screen)

    # отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(bullets):
    """обновляет позиции пуль и уничтожает старые"""
    # обновление позиций
    bullets.update()
    # удаление улетевших за края пуль
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, covids):
    """создает флотилию ковидов"""
    # создание вируса и вычисление кол-ва вирусов в ряду
    # интервал между вирусами равен 1 ширине пришельца

    covid = Covid(ai_settings, screen)
    covid_width = covid.rect.width
    number_covids_x = get_number_covids_x(ai_settings, covid_width)
    # создает 1 ряд вирусов
    for covid_number in range(number_covids_x):
        # create covid
        create_covid(ai_settings, screen, covids, covid_number)


def get_number_covids_x(ai_settings, covid_width):
    """вычисляет колво вирусов в ряду"""
    available_space_x = ai_settings.screen_width - 2 * covid_width
    number_covids_x = int(available_space_x / (2 * covid_width))
    return number_covids_x


def create_covid(ai_settings, screen, covids, covid_number):
    """делает вирус и размещает его"""
    covid = Covid(ai_settings, screen)
    covid_width = covid.rect.width
    covid.x = covid_width + 2 * covid_width * covid_number
    covid.rect.x = covid.x
    covids.add(covid)