import imp
import sys
import pygame
from settings import Settings
from ship import Ship
import game_fonctions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    # 初始化pygame
    # 初始化屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # bg_color = (230, 230, 230)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien = Alien(ai_settings, screen)

    # 游戏主循环
    while True:

        # 监听键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # bullets.update()
        gf.update_bullets(bullets)

 
        # # 释放已出屏幕的子弹资源
        # for bullet in bullets.copy() :
        #     if bullet.rect.bottom < 0:
        #         bullets.remove(bullet)
        # print(len(bullets))

        # # 修改背景颜色
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()

        # # 让最近绘制的屏幕可见
        # pygame.display.flip()

        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()