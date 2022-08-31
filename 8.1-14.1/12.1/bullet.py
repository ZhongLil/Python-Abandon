import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship) -> None:
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0, 0)处创建一个子弹矩阵, 在让其出现在正确位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # print(ship.rect.top)

        # 存储子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 更新子弹位置的小数值
        self.y -= self.speed_factor
        # 更新子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)