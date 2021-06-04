from Fighter import fighter
import pickle
import numpy as np
import random

Punchy = fighter("Punchy",10,5,5,5)
Speedy = fighter("Speedy",4,3,15,5)
Smarty = fighter("Smarty",5,5,5,10)
Fendy = fighter("Fendy",5,10,5,5)
Even = fighter("Even Steven",7,7,7,7)
Rando = fighter("Mr.Randopolis",12,8,5,1)
Brain = fighter("Mega Brain",3,3,3,24)
Omniman = fighter("Good Guy",16,16,16,16)
filler = fighter("Filler Man",1,1,1,1)

fighterList = [Punchy,Speedy,Smarty,Fendy,Even,Rando,Brain,Omniman]
customFighters = []

def save(f):
	file = open('CustomFighters','rb')
	customs = pickle.load(file)
	for i in customs:
		if i.name == f.name:
			customs.remove(i)
	customs.insert(0,f)
	file.close()
	return(customs)

def amtFighters(num):
	file = open('FighterList', 'rb')
	fighters = pickle.load(file)
	tourney = []
	while len(tourney) < num-1:
		add = fighters.pop(random.randint(0,len(fighters)-1))
		tourney.append(add)
	for i in tourney:
		fighters.append(i)
	return tourney

def rewriteFighters():
	file = open('FighterList','wb')
	pickle.dump(fighterList, file)
	file.close()

def rewriteCustoms():
	file = open('CustomFighters','wb')
	pickle.dump(customFighters,file)
	file.close()

if __name__ == '__main__':
	rewriteFighters()
	rewriteCustoms()