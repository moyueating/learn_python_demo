import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def update_screen(settings, screen, ship, aliens, bullets):
	# 每次循环时都重绘屏幕
	screen.fill(settings.bg_color)
	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
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

def get_number_rows(settings, ship_height, alien_height):
	# 计算高度方向的外星人宽度以及个数
	available_space_y = settings.screen_height - 3 * alien_height - ship_height
	numer_rows = int(available_space_y / (2 * alien_height))
	return numer_rows

def get_number_clomns(settings, alien_width):
	# 计算宽度方向的外星人宽度以及个数
	available_space_x = settings.screen_width - 2 * alien_width
	numbe_clomns = int(available_space_x / (2*alien_width))
	return numbe_clomns

def create_alien(settings, screen, aliens, clomn_number, row_number):
	alien = Alien(settings, screen)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	alien = Alien(settings, screen)
	alien.x = alien_width + 2 * alien_width * clomn_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
	alien = Alien(settings, screen)
	numbe_clomns = get_number_clomns(settings, alien.rect.width)
	row_number = get_number_rows(settings, ship.rect.height, alien.rect.height)

	for row_number in range(row_number):
		for clomn_number in range(numbe_clomns):
			create_alien(settings, screen, aliens, clomn_number, row_number)
		
def check_fleet_edges(settings, aliens):
	for alien in aliens:
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break

def change_fleet_direction(settings, aliens):
	for alien in aliens:
		alien.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1

def update_aliens(settings, aliens):
	check_fleet_edges(settings, aliens)
	aliens.update()

