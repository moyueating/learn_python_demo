import pygame
from pygame.sprite import Group
from settings import Settings
from button import Button
from game_status import GameStatus
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	all_settings = Settings()
	# set_mode返回的是一个Surface对象
	screen = pygame.display.set_mode((all_settings.screen_width, all_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建一个用于存储游戏统计信息的实例
	status = GameStatus(all_settings)

	# 创建一艘飞船
	ship = Ship(all_settings,screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	# 创建外星人群
	aliens = Group()
	gf.create_fleet(all_settings, screen, ship, aliens)

	# 创建Play按钮
	play_button = Button(all_settings, screen, "Play")

	# 开始游戏的主循环
	while True:
		gf.check_events(all_settings, screen, status, play_button, ship, aliens, bullets)
		
		if status.game_active:
			ship.update()
			gf.update_bullets(all_settings, screen, ship, aliens, bullets)
			gf.update_aliens(all_settings, status, play_button, screen, ship, aliens, bullets)

		gf.update_screen(all_settings, screen, status, ship, aliens, bullets, play_button)


run_game()
