###################
##Importing Stuff##
###################
import pygame
import sys, os
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

mouse = [0,0]
class Pix():
	def __init__(self, pos):
		self.x, self.y = pos
		self.old = False
		self.new = False
		self.pixArray = None
class Game():
	#############################
	##initializing pygame stuff##
	#############################
	width = 1000
	height = 600
	brush = 4
	
	def __init__(self):
		pygame.init()
		self.mouseclick = False
		self.timer = pygame.time.Clock()
		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.width, self.height = self.screen.get_size()
		self.interesting = set()
		###########################
		##initializing game stuff##
		###########################
		self.background = pygame.Surface((self.width, self.height)).convert()
		self.background.fill((0,0,0))

	def mod(self, num, base):
		return num%base

	def neighbors(self, pos):
		#find a nice way to determine how many o the surrounding squares are 1. that is all.
		#Return from that the number. Other method can use it.
		pass
	def drawThing(self, pos):
		x, y = pos
		x1 = (x+1)%self.width
		y1 = (y+1)%self.height
		self.pixArray[x][y] = WHITE
		self.pixArray[x1][y] = WHITE
		self.pixArray[x][y1] = WHITE
		self.pixArray[x1][y1] = WHITE
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				self.interesting.add(Pix(mod(i,self.width), mod(j, self.height)))

	def update(self):
		self.pixArray = pygame.PixelArray(self.background)
		if self.mouseclick:
			drawThing(pygame.mouse.get_pos())
		else:
			for pix in self.interesting:
				pix.old = pix.new
				if pix.old:
					
				else:
					pass
		del self.PixArray

	def draw(self):
		self.screen.blit(self.background, (0,0))
		pygame.display.flip()

	def mainLoop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.mouseclick = True
					mouse = pygame.mouse.get_pos()
					pass
				elif event.type == pygame.MOUSEMOTION:
					mouse = pygame.mouse.get_pos()
					pass
				elif event.type == pygame.MOUSEBUTTONUP:
					self.mouseclick = False
			self.update()
			self.draw()
			self.timer.tick(60)

if __name__ == '__main__':
	game = Game()
	game.mainLoop()
