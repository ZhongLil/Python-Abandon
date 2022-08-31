class Settings():
    # 储存游戏类

    def __init__(self) -> None:

        # 初始化参数

        # 背景参数
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船参数
        self.ship_speed_factor = 1.5

        # 射击参数
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4
