from turtle import Turtle


class GameStats():
    # log类

    def __init__(self, ai_settings) -> None:
        # 初始化统计信息
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        # 初始化数据
        self.ships_left = self.ai_settings.ship_limit