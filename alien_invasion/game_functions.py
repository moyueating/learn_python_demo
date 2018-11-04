import sys
import json
import pygame
from time import sleep
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

def check_events(settings, screen, status, sb, play_button, ship, aliens, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(settings, screen, status, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(settings, screen, status, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	# 点击开始游戏
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not status.game_active:
		# 重置游戏设置
		settings.initialize_dynamic_settings()
		# 隐藏光标
		pygame.mouse.set_visible(False)
		status.reset_status()
		sb.prep_life()
		sb.prep_score()
		status.game_active = True
		aliens.empty()
		bullets.empty()
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()

def update_screen(settings, screen, status, sb, ship, aliens, bullets, play_button):
	# 每次循环时都重绘屏幕
	screen.fill(settings.bg_color)
	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	sb.show_score()
	if not status.game_active:
		play_button.draw_button()
	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(settings, screen, status, sb,ship, aliens, bullets):
	bullets.update()
	# 删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(settings, screen, status, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(settings, screen, status, sb, ship, aliens, bullets):
	# 检查时候有子弹击中外星人，并删除相互碰撞的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			status.score += settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(status, sb)

	if len(aliens) == 0:
		# 删除现有所有子弹，并创建新的外星人群
		bullets.empty()
		# 加速游戏
		settings.increase_speed()
		create_fleet(settings, screen, ship, aliens)

def check_high_score(status, sb):
	if status.score > status.high_score:
		status.high_score = status.score
		sb.prep_high_score()

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

def check_alien_bottom(settings, status, sb, play_button, screen, ship, aliens, bullets):
	screen_rect = screen.get_rect()
	for alien in aliens:
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(settings, status, sb, play_button, screen, ship, aliens, bullets)
			break

def update_aliens(settings, status, sb, play_button, screen, ship, aliens, bullets):
	check_fleet_edges(settings, aliens)
	aliens.update()

	# 飞船和外星人相撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(settings, status, sb,  play_button, screen, ship, aliens, bullets)
	
	# 检查外星人是否达到屏幕底部
	check_alien_bottom(settings, status, sb, play_button, screen, ship, aliens, bullets)

def save_high_score(settings, status):
	with open(settings.high_score_file, 'w') as file:
		json.dump(status.high_score, file)

def ship_hit(settings, status, sb, play_button, screen, ship, aliens, bullets):
	# 飞船生命减一
	status.ships_left -= 1
	sb.prep_life()
	if status.ships_left > 0:
		# 清空子弹和外星人
		aliens.empty()
		bullets.empty()
		# 新建外星人
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()
		# 暂停
		sleep(0.5)
	else:
		status.game_active = False
		pygame.mouse.set_visible(True)
		save_high_score(settings, status)