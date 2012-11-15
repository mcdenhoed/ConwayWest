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

sBrushDefault = '''\
OO
O.O
O'''
sBrushGun = '''\
........................O
......................O.O
............OO......OO............OO
...........O...O....OO............OO
OO........O.....O...OO
OO........O...O.OO....O.O
..........O.....O.......O
...........O...O
............OO'''
sBrushNewGun = '''\
.......................OO........................OO
.......................OO........................OO
.........................................OO
........................................O..O
.........................................OO

....................................OOO
....................................O.O
.........OO.........................OOO
.........OO.........................OO
........O..O.......................OOO
........O..O.OO....................O.O
........O....OO....................OOO
..........OO.OO
...............................OO
.....................OO.......O..O
.....................OO........OO
.................................................OO
.................................................OO

....OO..................O
OO....OOOO..........OO..OO.OOO
OO..OO.OOO..........OO....OOOO
....O...................OO'''
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
		if "--fullscreen" in sys.argv:
			self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		else:
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
		self.brushDefault = self.stringToBrush(sBrushDefault)
		self.brushGun = self.stringToBrush(sBrushGun)
		self.brushNewGun = self.stringToBrush(sBrushNewGun)
	def mod(self, num, base):
		return num%base

	def neighbors(self, pos):
		x, y = pos
		#find a nice way to determine how many o the surrounding squares are 1. that is all.
		#Return from that the number. Other method can use it.
		#print([a for a in range(x-1,x+2) for b in range(y-1,y+2) if (a,b) in self.interesting and self.interesting[(a,b)] is True])
		temp = sum(1 for a in range(x-1,x+2) for b in range(y-1,y+2) if (a%self.width, b%self.height) in self.interesting and self.interesting[a%self.width, b%self.height] is True)
		if self.interesting[pos]:
			return temp - 1
		else: return temp

	def stringToBrush(self, s):
		points = []
		lines = s.split('\n')
		for i in range(len(lines)):
			line = lines[i]
			for j in range(len(line)):
				if line[j] == 'O':
					points.append((j,i))
		return points

	def drawThing(self, pos, brush=None):
		if not brush: brush = self.brushDefault
		x, y = pos
		for (dx,dy) in brush:
			self.turnOnSquare((x+dx, y+dy))
	
	def turnOnSquare(self, pos):
		x, y = pos
		self.pixArray[x%self.width][y%self.height] = WHITE
		self.temp.update(((i%self.width,j%self.height),False) for i in range(x-1, x+2) for j in range(y-1,y+2) if not ((i%self.width,j%self.height) in self.temp or (i%self.width,j%self.height) in self.interesting))
		self.temp[pos] = True

	def turnOffSquare(self, pos):
		x,y = pos
		self.pixArray[x%self.width][y%self.height] = BLACK
		self.temp[pos] = False
 
	def update(self):
		self.pixArray = pygame.PixelArray(self.background)
		remove = set()
		if self.mouseclick:
			self.drawThing(pygame.mouse.get_pos())
		else:
			for pos, turnedOn in self.interesting.iteritems():
				neighbors = self.neighbors(pos)
				if turnedOn and neighbors not in [2,3]:
					self.turnOffSquare(pos)
				elif neighbors == 3:
					self.turnOnSquare(pos)
			self.interesting.update(self.temp)
			# update interesting set
			for pos, turnedOn in self.interesting.iteritems():
				neighbors = self.neighbors(pos)
				if not turnedOn and self.neighbors(pos) == 0:
					remove.add(pos)
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
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
