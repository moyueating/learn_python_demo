import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	all_settings = Settings()
	# set_mode返回的是一个Surface对象
	screen = pygame.display.set_mode((all_settings.screen_width, all_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建一艘飞船
	ship = Ship(all_settings,screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	# 创建外星人群
	aliens = Group()
	gf.create_fleet(all_settings, screen, ship, aliens)

	# 开始游戏的主循环
	while True:
		gf.check_events(all_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_aliens(all_settings, aliens)
		gf.update_screen(all_settings, screen, ship, aliens, bullets)


run_game()
