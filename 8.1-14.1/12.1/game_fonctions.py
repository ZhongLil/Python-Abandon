import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, stats, play_button, ship, bullets):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)

def check_play_button(stats, play_button, mouse_x, mouse_y):
    # 在用户单机Play按钮时开始游戏
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

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


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    # 释放已出屏幕的子弹所占用的资源
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    # print(len(bullets))


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # 检查是否有子弹击中敌方单位
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除现有子弹并生成敌方单位
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建新元素加入到bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, stats,  ship, aliens, bullets, play_button):

    # 每次循环输出一帧画面
    screen.fill(ai_settings.bg_color)

    # 在飞船和怪物后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)

    # 如果游戏处于非活动状态绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 输出画面
    pygame.display.flip()


def create_fleet(ai_settings, screen, ship, aliens):
    # 创建敌人群, 并计算最大容量(在无重叠情况下)
    # 默认间距为素材宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    # for alien_number in range(number_aliens_x):
    #     create_alien(ai_settings, screen, aliens, alien_number)
    # alien_width = alien.rect.width
    # available_space_x = ai_settings.screen_width - 2 * alien_width
    # number_aliens_x = int(available_space_x / (2 * alien_width))
    # # 创建一行敌人
    # for alien_number in range(number_aliens_x):
    #     # 创建一个敌人并将其添加到集合
    #     alien = Alien(ai_settings, screen)
    #     alien.x = alien_width + 2 * alien_width * alien_number
    #     alien.rect.x = alien.x
    #     aliens.add(alien)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建当前行敌人
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    # 检查是否有敌人处于屏幕边缘
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def get_number_aliens_x(ai_settings, alien_width):
    # 计算屏幕最大敌人容量
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    # 计算屏幕容量
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -
                         ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows


def check_fleet_edges(ai_settings, aliens):
    # 当敌人到达边缘时停止外移
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    # 将其向下移动
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):

    if stats.ships_left > 0:
        # 响应飞船被敌人撞毁
        stats.ships_left -= 1

        # 清空地方列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 进行初始化
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)

    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    # 检查是否有单位到达屏幕底部
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break