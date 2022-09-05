import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    # 响应按键和鼠标事件
    for event in pygame.event.get():

        # if event.key == pygame.K_q:
        #     sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            # # 向右移
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = True
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹, 加入到矩阵Bullets中
        # print("check space")
        # print(ai_settings.bullet_width)
        # print(ai_settings.bullet_height)
        # print(ai_settings.bullet_color)
        # if len(bullets) < ai_settings.bullets_allowed:
        #     new_bullet = Bullet(ai_settings, screen, ship)
        #     bullets.add(new_bullet)
        fire_bullet(ai_settings, screen, ship, bullets)
    # 按键Q退出
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(bullets):

    # 释放已出屏幕的子弹所占用的资源
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    # print(len(bullets))


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建新元素加入到bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):

    # 每次循环输出一帧画面
    screen.fill(ai_settings.bg_color)

    # 在飞船和怪物后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)
        # 输出画面
    pygame.display.flip()


def create_fleet(ai_settings, screen, aliens):
    #    创建敌人群, 并计算最大容量(在无重叠情况下)
    # 默认间距为素材宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # 创建一行敌人
    for alien_number in range(number_aliens_x):
        # 创建一个敌人并将其添加到集合
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

