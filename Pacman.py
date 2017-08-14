import pygame
from PIL import Image
from colors import *

class Pacman:

	def __init__(self, frame):
		self.frame = frame
		self.name = 'pacman.png'
		self.name_back = 'pacman-back.png'
		im = Image.open(self.name)
		self.width, self.height = im.size
		self.x = self.frame.get_prop()[0] - self.width/2
		self.y = self.frame.get_prop()[1] - self.height/2
		self.image = pygame.image.load('pacman.png')
		self.image_back = pygame.image.load('pacman-back.png')
		self.speed = 6
		self.direction = 0
		self.prev_dir = self.direction
		self.start_point = (self.x + self.width/2, self.y + self.height/2)
		self.border_point_start = self.start_point
		self.reach_border = True
		self.leave_border = False
		self.half_border = 0
		self.lines = []
		self.last_line = False

	def show(self):
		if self.direction == 2:
			return self.image
		elif self.direction == 4:
			return self.image_back
		return self.image

	def move(self, screen):
		# draw all lines

		for line in self.lines:
			pygame.draw.line(screen, red, line[0], line[1], 3)

		if self.prev_dir != self.direction or self.check_border_point():
			if self.last_line == False:
				self.lines.append((self.start_point, (self.x + self.width/2, self.y + self.height/2)))
				self.last_line = True

			self.start_point = (self.x + self.width/2, self.y + self.height/2)

		if self.prev_dir == self.direction and not self.check_border_point():
			pygame.draw.line(screen, red, self.start_point, (self.x + self.width/2, self.y + self.height/2), 3)
			self.last_line = False



		if self.check_border_point():
			if self.leave_border == False:
				self.border_point_start = self.start_point
			else:
				self.half_border = ( (self.border_point_start[0]
									+ (self.x + self.width/2))/2,
									 (self.border_point_start[1] 
									+ (self.y + self.height/2))/2 )
				self.reach_border = True
				self.flood_fill(self.half_border[0], self.half_border[1],screen)
		else:
			self.leave_border = True
			self.reach_border = False


		if self.direction == 1:
			self.y -= self.speed
			if self.y + self.height/2 < self.frame.get_prop()[1]:
				self.y = self.frame.get_prop()[1] - self.height/2
		elif self.direction == 2:
			self.x += self.speed
			if self.x + self.width/2 > self.frame.get_prop()[0] + self.frame.get_prop()[2]:
				self.x = self.frame.get_prop()[0] + self.frame.get_prop()[2] - self.width/2
		elif self.direction == 3:
			self.y += self.speed
			if self.y + self.height/2 > self.frame.get_prop()[1] + self.frame.get_prop()[3]:
				self.y = self.frame.get_prop()[1] + self.frame.get_prop()[3] - self.height/2
		elif self.direction == 4:
			self.x -= self.speed
			if self.x + self.width/2 < self.frame.get_prop()[0]:
				self.x = self.frame.get_prop()[0] - self.width/2
		else:
			pass

		self.prev_dir = self.direction

	def flood_fill(self, x, y, screen):
		x = int(x)
		y = int(y)
		screen.set_at((x, y), red)
		screen.fill(black)
		# draw Frame
		pygame.draw.rect(screen,
						 self.frame.get_color(),
						 self.frame.get_prop(),
						 self.frame.get_thickness())
		# Move the Hero
		# Draw line behind the Hero
		pygame.draw.circle(screen, green, (170,450), 5)
		# Draw the Hero
		screen.blit(self.show(),
						(self.get_x(),
						 self.get_y())
						)
		pygame.display.flip()
		if screen.get_at((x+1, y)) == (0,255,255,255):
			self.flood_fill(x+1,y, screen)
		if screen.get_at((x, y+1)) == (0,255,255,255):
			self.flood_fill(x,y+1, screen)
		if screen.get_at((x-1, y)) == (0,255,255,255):
			self.flood_fill(x-1,y, screen)
		if screen.get_at((x, y-1)) == (0,255,255,255):
			self.flood_fill(x,y-1, screen)
		
		return

	def check_border_point(self):
		left_border = self.frame.get_prop()[0] - self.width/2
		right_border = self.frame.get_prop()[0] + self.frame.get_prop()[2] - self.width/2
		up_border = self.frame.get_prop()[1] - self.height/2
		bottom_border = self.frame.get_prop()[1] + self.frame.get_prop()[3] - self.height/2
		if self.x == left_border or self.x == right_border or self.y == up_border or self.y == bottom_border:
			return True
		return False


	def get_x(self):
		return self.x
	def get_y(self):
		return self.y

	def set_direction(self, value):
		'''
		  1
		  |
		4-0-2
		  |
		  3
		'''
		self.direction = value
