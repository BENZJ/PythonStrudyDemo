#coding=utf-8
import pygame
from Settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	pygame.init()
#	screen = pygame.display.set_mode((1200, 800))
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	ship = Ship(ai_settings,screen)

	pygame.display.set_caption("Alien Invasion")

	#创建一个用于存储子弹的编组
	bullets = Group()
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		'''
		#删除已消失的子弹
		for bullet in bullets.copy():
			if bullet.rect.bottom<=0:
				bullets.remove(bullet)
		#print(len(bullets))
		'''
		gf.update_bullets(bullets)

		gf.update_screen(ai_settings,screen,ship,bullets)

'''
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		pygame.display.flip()
'''
'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
'''
run_game()
