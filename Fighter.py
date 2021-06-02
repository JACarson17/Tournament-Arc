import random
import numpy as np
import os.path
import Battle


savePath = "C:/Users/dabea/Documents/Code/Python/Tournament Arc"

class fighter:
	def __init__(self,name,atk,dfn,spd,mntl):
		self.name = name
		self.atk = atk
		self.dfn = dfn
		self.health = dfn + 5
		self.spd = spd
		self.mntl = mntl
		self.agro = atk - mntl
		self.statTot = self.atk + self.dfn + self.spd + self.mntl
		self.ogStats = [self.name, self.atk, self.dfn, self.spd, self.health, self.mntl, self.agro]
		self.action = None
		self.alive = True
		self.roundsLost = 0
		self.participation = 0
		self.wins = 0
		self.wr = 0
		self.current = False
		self.exp = 0

	def determineAction(self,opponent):
		self.reset()
		choice = np.random.choice(4,1,p=[self.atk/self.statTot, self.dfn/self.statTot, self.spd/self.statTot, self.mntl/self.statTot])
		if choice == 0:
			self.attack(opponent)
		elif choice == 1:
			self.block()
		elif choice == 2:
			self.evade()
		elif choice == 3:
			self.mental(opponent)

	def reset(self):
		self.name = self.ogStats[0]
		self.atk = self.ogStats[1]
		self.dfn = self.ogStats[2]
		self.spd = self.ogStats[3]
		self.action = None

	def attack(self,opponent):
		self.action = "attack"
		if self.current == True:
			Battle.log.append(self.name + " attacks " + opponent.name)
		power = random.randint(0,self.atk)
		defend = opponent.guard()
		if power > defend:
			if power == self.atk:
				if self.current == True:
					Battle.log.append("Critical hit!")
				damage = random.randint(1, power-defend)*2
			else:
				damage = random.randint(1, power-defend)
		else:
			damage = 0
		if damage > 0:
			opponent.takeDmg(damage)

	def mental(self,opponent):
		self.action = "mental"
		if self.current == True:
			Battle.log.append(self.name + " mentally attacks " + opponent.name)
		power = random.randint(0,self.mntl)
		resist = opponent.guard()
		if power > resist:
			if power == self.mntl:
				if self.current == True:
					Battle.log.append("Critical hit!")
				damage = random.randint(1,power-resist)*2
			else:
				damage = random.randint(1,power-resist)
		else:
			damage = 0
		if damage > 0:
			opponent.takeDmg(damage)

	def block(self):
		self.action = "block"
		if self.current == True:
			Battle.log.append(self.name + " blocks.")
		self.dfn = round(self.dfn * 1.5)

	def evade(self):
		if self.current == True:
			Battle.log.append(self.name + " begins evading.")
		self.dfn = round(self.spd * 1.5)
		self.action = "evade"

	def guard(self):
		defense = random.randint(0,self.dfn)
		return defense

	def mguard(self):
		resist	= random.randint(0,self.mntl)
		return resist

	def takeDmg(self, dmg):
		if self.action == "evade":
			self.health = self.health - round(dmg*1.5)
		else:
			self.health = self.health - dmg
		if self.health < 0:
			self.health = 0
		if self.current == True:
			Battle.log.append(self.name + " took " + str(dmg) + " damage. " + str(self.health) + " health remaining.")
		self.checkVitals()

	def checkVitals(self):
		if self.health <= 0:
			self.alive = False
			self.roundsLost = self.roundsLost + 1

	def roundReset(self):
		self.reset()
		self.action = None
		self.health = self.ogStats[4]
		self.alive = True

	def fightReset(self):
		self.roundReset()
		self.roundsLost = 0

	def updateWR(self):
		self.wins = self.wins + 1
		self.wr = self.wins / self.participation
		self.exp = self.exp + 1

	def updateStats(self):
		self.agro = self.atk - self.mntl
		self.statTot = self.atk + self.dfn + self.spd + self.mntl
		self.ogStats = [self.name, self.atk, self.dfn, self.spd, self.health, self.mntl, self.agro]
