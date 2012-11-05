###################
##Importing Stuff##
###################
import pygame
import sys, os
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Pix():
	def __init__(alive):
		self.alive = alive

class Game():
	#############################
	##initializing pygame stuff##
	#############################
	width = 1000
	height = 600
	brush = 4
	
	def __init__(self):
		pygame.init()
		self.timer = pygame.time.Clock()
		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.width, self.height = self.screen.get_size()
		self.interesting = set()
		###########################
		##initializing game stuff##
		###########################
		self.background = pygame.Surface((self.width, self.height)).convert()
		self.background.fill((0,0,0))
		pygame.Surface.blit(self.background, self.screen, (0,0))
		self.pixArray = pygame.PixelArray(self.background)

	def neighbors(self, tup):
		x, y, on = tup
		if on:
			pass
		else	
			pass

	def update(self):
		pixArray = pygame.PixelArray(self.background)
		for yo in self.interesting:
			
		del pixArray

	def draw(self):
		self.screen.blit(self.background, (0,0))
		pygame.display.flip()

	def mainLoop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					pass
				elif event.type == pygame.MOUSEMOTION:
					pass
				elif event.type == pygame.MOUSEBUTTONUP:
					pass
			self.update()
			self.draw()
			self.timer.tick(60)

if __name__ == '__main__':
	game = Game()
	game.mainLoop()
