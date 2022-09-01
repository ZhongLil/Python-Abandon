import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # 敌对单位类
    def __init__(self, ai_settings, screen) -> None:
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载敌对单位图像, 设置其 rect属性
        self.image = pygame.image.load(
            "F:\project\python\Python-Abandon\8.1-14.1\\12.1\images\\alien.bmp")
        self.rect = self.image.get_rect()

        # 敌对单位生成在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存敌对单位的精准坐标
        self.x = float(self.rect.x)

    def blitme(self):
        # 绘制敌对单位
        self.screen.blit(self.image, self.rect)
