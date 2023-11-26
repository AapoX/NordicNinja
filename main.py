import pygame, sys, asyncio
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI



class Game:
	def __init__(self):

		# game attributes
		self.max_level = 0
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0
		
		# audio 
		self.level_bg_music = pygame.mixer.Sound('audio/level_music.wav')
		self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.wav')

		# overworld creation
		self.overworld = Overworld(0,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)

		# user interface 
		self.ui = UI(screen)


	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_overworld,self.change_coins,self.change_health)
		self.status = 'level'
		self.overworld_bg_music.stop()
		self.level_bg_music.play(loops = -1)

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)
		self.level_bg_music.stop()

	def change_coins(self,amount):
		self.coins += amount

	def change_health(self,amount):
		self.cur_health += amount

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0,self.max_level,screen,self.create_level)
			self.status = 'overworld'
			self.level_bg_music.stop()
			self.overworld_bg_music.play(loops = -1)

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			self.ui.show_health(self.cur_health,self.max_health)
			self.ui.show_coins(self.coins)
			self.check_game_over()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()
font = pygame.font.SysFont('comicsansms', 30)
start_ticks = pygame.time.get_ticks()
timer_active = True



async def main():
    
	current_time = 0
	button_press_time = 0
    
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		if timer_active:
			current_ticks = pygame.time.get_ticks()
			elapsed_ticks = current_ticks - start_ticks
			elapsed_seconds = elapsed_ticks // 1000
			elapsed_minutes = elapsed_seconds // 60
			elapsed_seconds %= 60
  
		screen.fill('grey')
		game.run()
		timer_text = f"{elapsed_minutes}:{elapsed_seconds}"
		timer_surface = font.render(timer_text, True, (255, 255, 255))
		padding = 10
		timer_x = max(screen.get_width() - timer_surface.get_width() -padding, 0)
		screen.blit(timer_surface, (timer_x, 0))


		pygame.display.update()
		clock.tick(60)
		await asyncio.sleep(0)
  
asyncio.run(main())