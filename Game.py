import pygame
from Pacman import *
from colors import *
from Frame import *
from Creature import *

class Game:

	def __init__(self, size):
		pygame.init()
		self.size = size
		self.screen = pygame.display.set_mode(size, 0, 32)
		self.color = black
		pygame.display.set_caption('PACMAN FOREVER YOUNG')
		self.run = True
		self.frame = Frame((50, 50, 1100, 800), cyan, 4)
		self.pacman = Pacman(self.frame)
		# game speed = number of operations per sec
		self.game_speed = 60
		self.lines = []

	def escape_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.run = False

	def main_loop(self):
		time = pygame.time.Clock()
		while self.run:
			# manage a speed of the game
			time.tick(self.game_speed)

			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_DOWN]:
				self.pacman.set_direction(3)
			elif keys_pressed[pygame.K_UP]:
				self.pacman.set_direction(1)
			if keys_pressed[pygame.K_RIGHT]:
				self.pacman.set_direction(2)
			elif keys_pressed[pygame.K_LEFT]:
				self.pacman.set_direction(4)
			if keys_pressed[pygame.K_SPACE]:
				self.pacman.set_direction(0)

			self.escape_loop()

			# Fill the background
			self.screen.fill(self.color)
			# draw Frame
			pygame.draw.rect(self.screen,
							 self.frame.get_color(),
							 self.frame.get_prop(),
							 self.frame.get_thickness())
			# Move the Hero
			self.pacman.move(self.screen)
			# Draw line behind the Hero
			pygame.draw.circle(self.screen, green, (170,450), 5)
			# Draw the Hero
			self.screen.blit(self.pacman.show(),
							(self.pacman.get_x(),
							 self.pacman.get_y())
							)
			pygame.display.flip()


if __name__ == '__main__':
	game = Game((1400,1000))
	game.main_loop()
