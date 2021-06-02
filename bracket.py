import random
import numpy as np
import Battle
import WriteFighters

class Bracket():
	def __init__(self, size,elim,pc):
		self.size = size
		self.elim = elim
		self.victor = None
		self.player = pc

	def make(self,flist):		
		bouts = [[] for i in range(int(len(flist)/2))]
		j = 0
		for i in flist:
			if len(bouts[j]) < 2:
				bouts[j].append(i)
			else:
				j = j+1
				bouts[j].append(i)
		self.round(bouts) #a 2d array of all first round fights, each index is a sub array of 2 fighters

	def round(self,rounds):
		winners = []
		for i in rounds:
			if self.player in i:
				winners.append(Battle.determineSpeed(i,True))
			else:
				winners.append(Battle.determineSpeed(i,False))
		if len(winners) > 1:
			self.make(winners)
		else:
			Battle.log.append(winners[0].name + " has won the tournament!")

def main(size,elim,pc):
	Battle.log = []
	b = Bracket(size,elim,pc)
	entrants = WriteFighters.amtFighters(size) #entrants is an array of fighter objects
	entrants.append(pc)
	b.make(entrants)
	file = open('BracketLog','w')
	for i in Battle.log:
		file.write(i+ '\n' )
	file.close()
