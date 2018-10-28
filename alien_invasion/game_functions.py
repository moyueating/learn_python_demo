import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_screen(settings, screen, ship, bullets):
	# 每次循环时都重绘屏幕
	screen.fill(settings.bg_color)
	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(bullets):
	bullets.update()
	# 删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(settings, screen, ship, bullets):
	# 创建子弹并添加到精灵编组中
	if len(bullets) < settings.bullet_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)
		
