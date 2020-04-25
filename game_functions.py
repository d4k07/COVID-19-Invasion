import sys
import pygame
from bullet import Bullet

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


def update_screen(ai_settings, screen, cat, covid, bullets):
    """Обновляет изображения на экране и отображает новый экран"""
    # при каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    # все пули позади кота и ковидов
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    cat.blitme()
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
