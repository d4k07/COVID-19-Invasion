import sys
import pygame


def check_events():
    # обрабатывает нажатия клавиш и мышки
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
