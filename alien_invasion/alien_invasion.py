import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init()
    all_settings = Settings()
    screen = pygame.display.set_mode((all_settings.screen_width, all_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(all_settings,screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(all_settings, screen, ship)


run_game()
