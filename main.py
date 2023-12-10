import pygame, sys, asyncio, pygame.locals as pglocals, mysql.connector
from settings import *
from level import Level
from overworld import Overworld
from ui import UI

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentokentat',
         user='root',
         password='rootpass123',
         autocommit=True
         )

sqlCursor = connection.cursor()

class Game:
	def __init__(self):

		# game attributes
		self.max_level = 0
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0
		self.player_name = None

		# audio
		self.level_bg_music = pygame.mixer.Sound('audio/level_music.wav')
		self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.wav')

		# overworld creation
		#self.overworld = Overworld(0, self.max_level, screen, self.create_level)
		#self.status = 'overworld'
		self.status = 'name'
		#self.overworld_bg_music.play(loops=-1)

		# user interface
		self.ui = UI(screen)

	def create_level(self, current_level):
		self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health, self.player_name)
		self.status = 'level'
		self.overworld_bg_music.stop()
		self.level_bg_music.play(loops=-1)

	def create_overworld(self, current_level, new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops=-1)
		self.level_bg_music.stop()

	def change_coins(self, amount):
		self.coins += amount

	def change_health(self, amount):
		self.cur_health += amount

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0, self.max_level, screen, self.create_level)
			self.status = 'overworld'
			self.level_bg_music.stop()
			self.overworld_bg_music.play(loops=-1)

	def get_player_name(self):
		input_box_width = 140
		input_box_height = 32

		input_box = pygame.Rect(
			(screen_width - input_box_width) // 2,
			(screen_height - input_box_height) // 2,
			input_box_width,
			input_box_height
		)

		color = pygame.Color('dodgerblue2')
		text = ''
		font = pygame.font.Font(None, 32)

		while not self.player_name:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						existing_name_query = "SELECT * FROM leaderboard WHERE player_name = %s"
						sqlCursor.execute(existing_name_query, (text, ))
						result = sqlCursor.fetchone()

						if not result:
							insert_name_query = "INSERT INTO leaderboard (player_name) VALUES (%s)"
							sqlCursor.execute(insert_name_query, (text,))
							connection.commit()
						else:
							get_max_level_query = "SELECT max_level FROM leaderboard WHERE player_name = %s"
							sqlCursor.execute(get_max_level_query, (result[1], ))
							max_level_value = sqlCursor.fetchone()
							self.max_level = max_level_value[0]
							print(f'max level is {self.max_level}')

						self.player_name = text

						self.overworld = Overworld(0, self.max_level, screen, self.create_level)
						self.status = 'overworld'
						self.overworld_bg_music.play(loops=-1)


					elif event.key == pygame.K_BACKSPACE:
						text = text[:-1]
					else:
						text += event.unicode

			screen.fill('grey')
			pygame.draw.rect(screen, color, input_box, 2)
			txt_surface = font.render(text, True, color)
			width = max(input_box_width, txt_surface.get_width() + 10)
			input_box.w = width
			screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
			pygame.display.flip()
			clock.tick(30)

	def run(self):
		if not self.player_name:
			self.get_player_name()

		elif self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			self.ui.show_health(self.cur_health, self.max_health)
			self.ui.show_coins(self.coins)
			self.check_game_over()


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
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

		screen.fill('grey')
		game.run()

		timer_text = f"{elapsed_seconds}s"
		timer_surface = font.render(timer_text, True, (255, 255, 255))
		padding = 10
		timer_x = max(screen.get_width() - timer_surface.get_width() - padding, 0)
		screen.blit(timer_surface, (timer_x, 0))

		pygame.display.update()
		clock.tick(60)
		await asyncio.sleep(0)


asyncio.run(main())