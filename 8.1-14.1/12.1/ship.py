import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # 初始化飞船, 设置飞船初始位置

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像, 获取外接矩阵
        self.image = pygame.image.load(
            # "F:\project\python\Python-Abandon\8.1-14.1\\12.1\images\handgun.bmp")
            ".\images\handgun.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 初始化飞船位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # 在指定位置初始化飞船
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # 更新rect对象
        self.rect.centerx = self.center

    def center_ship(self):
        # 初始化位置
        self.center = self.screen_rect.centerx