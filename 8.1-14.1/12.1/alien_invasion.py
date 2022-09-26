import imp
import sys
import pygame
from settings import Settings
from ship import Ship
import game_fonctions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化pygame
    # 初始化屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建开始按钮
    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)

    # 创建敌人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 游戏主循环
    while True:

        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            # bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
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

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()