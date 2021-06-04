log = []

def determineSpeed(fs,has):
	f1 = fs[0]
	f2 = fs[1]
	if has == True:
		f1.current,f2.current = True, True
	else:
		f1.current,f2.current = False, False
	if f1.spd > f2.spd:
		desp = round(f1.spd/f2.spd)
		if desp < 2:
			desp = 2
		if has == True:
			winner = battle(f1,f2,desp,has)
		else:
			winner = npcBattle(f1,f2,desp)
	elif f2.spd > f1.spd:
		desp = round(f2.spd/f1.spd)
		if desp < 2:
			desp = 2
		if has == True:
			winner = battle(f2,f1,desp,has)
		else:
			winner = npcBattle(f2,f1,desp)
	elif f1.spd == f2.spd:
		if has == True:
			winner = battle(f1,f2,2,has)
		else:
			winner = npcBattle(f1,f2,2)
	return(winner)

def battle(faster, slower, floor,has):
	faster.participation = faster.participation	+1
	slower.participation = slower.participation	+1
	rnd = 1
	while faster.roundsLost != 2 and slower.roundsLost != 2:
		log.append("\nROUND " + str(rnd) + "\n")
		turn = 0
		while faster.alive == True and slower.alive == True:
			if turn % floor == floor - 1:
				slower.determineAction(faster)
			else:
				faster.determineAction(slower)
			turn = turn + 1
		faster.roundReset()
		slower.roundReset()
		rnd = rnd+1
	if faster.roundsLost != 2:
		log.append(faster.name + " wins!")
		faster.updateWR()
		faster.fightReset()
		slower.fightReset()
		return(faster)
	elif slower.roundsLost != 2:
		log.append(slower.name + " wins!")
		slower.updateWR()
		faster.fightReset()
		slower.fightReset()
		return(slower)


def npcBattle(faster,slower,floor):
	faster.participation = faster.participation	+1
	slower.participation = slower.participation	+1
	rnd = 1
	while faster.roundsLost != 2 and slower.roundsLost != 2:
		turn = 0
		while faster.alive == True and slower.alive == True:
			if turn % floor == floor - 1:
				slower.determineAction(faster)
			else:
				faster.determineAction(slower)
			turn = turn + 1
		faster.roundReset()
		slower.roundReset()
		rnd = rnd+1
	if faster.roundsLost != 2:
		faster.updateWR()
		faster.fightReset()
		slower.fightReset()
		return(faster)
	elif slower.roundsLost != 2:
		slower.updateWR()
		faster.fightReset()
		slower.fightReset()
		return(slower)