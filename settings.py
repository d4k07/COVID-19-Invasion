class Settings:
    """тут все настройки игры"""

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (250, 250, 250)

        # показатель скорости кота
        self.cat_speed_factor = 1.5

        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3