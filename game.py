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
BLACK = (0,0,0)
mouse = [0,0]

class Pix():
	def __init__(self, pos):
		self.x, self.y = pos
		self.old = False
		self.new = False

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
		#self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.screen = pygame.display.set_mode((800,200))
		self.width, self.height = self.screen.get_size()
		self.interesting = dict()
		self.temp = dict()
		###########################
		##initializing game stuff##
		###########################
		self.background = pygame.Surface((self.width, self.height)).convert()
		self.background.fill((0,0,0))
		self.pixArray = None 
	def mod(self, num, base):
		return num%base

	def neighbors(self, pos):
		x, y = pos
		#find a nice way to determine how many o the surrounding squares are 1. that is all.
		#Return from that the number. Other method can use it.
		#print([a for a in range(x-1,x+2) for b in range(y-1,y+2) if (a,b) in self.interesting and self.interesting[(a,b)] is True])
		temp = sum(1 for a in range(x-1,x+2) for b in range(y-1,y+2) if (a,b) in self.interesting and self.interesting[(a,b)] is True)
		if self.interesting[pos]:
			return temp - 1
		else: return temp

	def drawThing(self, pos):
		x, y = pos
		x1 = (x+2)%self.width
		y1 = (y+1)%self.height
		self.turnOnSquare((x,y))
		self.turnOnSquare((x1,y))
		self.turnOnSquare((x,y1))
		self.turnOnSquare((x1+1,y1))
	
	def turnOnSquare(self, pos):
		x, y = pos
		self.pixArray[x%self.width][y%self.height] = WHITE
		self.temp.update(((i%self.width,j%self.height),False) for i in range(x-1, x+2) for j in range(y-1,y+2) if not ((i,j) in self.temp or (i,j) in self.interesting))
		self.temp[pos] = True

	def turnOffSquare(self, pos):
		x,y = pos
		self.pixArray[x%self.width][y%self.height] = BLACK
		self.temp[pos] = False
 
	def update(self):
		self.pixArray = pygame.PixelArray(self.background)
		remove = set()
		print(len(self.interesting))
		if self.mouseclick:
			self.drawThing(pygame.mouse.get_pos())
		else:
			for pos, turnedOn in self.interesting.iteritems():
				if turnedOn:
					if self.neighbors(pos) < 2:
						self.turnOffSquare(pos)
					elif self.neighbors(pos) > 3:
						self.turnOffSquare(pos)
				else:
					if(self.neighbors(pos) == 3):
						self.turnOnSquare(pos)
					elif(self.neighbors(pos) == 0):
						remove.add(pos)
			self.interesting.update(self.temp)
			self.temp = dict()
			for r in remove:
				self.interesting.pop(r)
		del self.pixArray

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
