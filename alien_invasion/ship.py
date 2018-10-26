import pygame

class Ship(object):
	"""一个存储游戏《外星人入侵》 的所有设置的类"""
	def __init__(self, settings,screen):
		self.screen = screen
		self.settings = settings
		# 加载飞船图像并获取起外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.center = float(self.screen_rect.centerx)

		# 移动标志
		self.moving_right = False
		self.moving_left = False

		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def update(self):
		if self.moving_right:
			self.center += self.settings.ship_speed_factor
		if self.moving_left:
			self.center -= self.settings.ship_speed_factor

		# 根据self.center更新rect对象
		self.rect.centerx = self.center

	def blitme(self):
		self.screen.blit(self.image, self.rect)
