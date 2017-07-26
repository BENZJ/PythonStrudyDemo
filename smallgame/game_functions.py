#coding=utf-8
import sys
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
	#响应按键和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ai_settings,screen,ship,bullets)

def update_screen(ai_settings, screen , ship,bullets):
	"""更新屏幕上的图像,并且切换到新的屏幕"""
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()

def check_keydown_events(event,ai_settings,screen, ship, bullets):
	"""键盘按下的响应事件"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	if event.key == pygame.K_SPACE:
		#限制最大子弹数
		fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ai_settings,screen , ship, bullets):
	"""键盘松开的响应事件"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right=False
	if event.key == pygame.K_LEFT:
		ship.moving_left=False

def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0 :
			bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
