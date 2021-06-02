from tkinter import *
import Battle
import bracket
import pickle


root = Tk()
root.geometry("500x500")

currentFighter = None
options = Frame(root)
options.grid(row=0,column=0)
currentvar = StringVar()
currentvar.set("Your current fighter is: ")


def customFighter():
	options.grid_forget()
	creator = LabelFrame(root, text='Create a custom fighter')
	creator.grid(row=0,column=0)
	
	global statot,atk,dfn,spd,mntl
	statot = 26
	atk = 1
	dfn = 1
	spd = 1
	mntl = 1


	strvar,defvar,spdvar,mntlvar,statvar = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
	strvar.set("Str: "+str(atk))
	defvar.set("Def: "+str(dfn))
	spdvar.set("Spd: "+str(spd))
	mntlvar.set("Mntl: "+str(mntl))
	statvar.set("Stat Points Remaining: "+str(statot))

	def StrTickUp():
		global atk, statot
		if statot > 0:
			statot = statot-1
			atk = atk+1
			strvar.set("Str: "+str(atk))
			statvar.set("Stat Points Remaining: "+str(statot))

	def StrTickDn():
		global atk, statot
		if atk > 1:
			statot = statot+1
			atk = atk-1
			strvar.set("Str: "+str(atk))
			statvar.set("Stat Points Remaining: "+str(statot))

	def DfnTickUp():
		global dfn, statot
		if statot > 0:
			statot = statot-1
			dfn = dfn+1
			defvar.set("Def: "+str(dfn))
			statvar.set("Stat Points Remaining: "+str(statot))

	def DfnTickDn():
		global dfn, statot
		if dfn > 1:
			statot = statot+1
			dfn = dfn-1
			defvar.set("Def: "+str(dfn))
			statvar.set("Stat Points Remaining: "+str(statot))

	def SpdTickUp():
		global spd, statot
		if statot > 0:
			spd = spd+1
			statot = statot-1
			spdvar.set("Spd: "+str(spd))
			statvar.set("Stat Points Remaining: "+str(statot))

	def SpdTickDn():
		global spd, statot
		if spd > 1:
			statot = statot+1
			spd = spd-1
			spdvar.set("Spd: "+str(spd))
			statvar.set("Stat Points Remaining: "+str(statot))

	def MntlTickUp():
		global mntl, statot
		if statot > 0:
			statot = statot-1
			mntl = mntl+1
			mntlvar.set("Mntl: "+str(mntl))
			statvar.set("Stat Points Remaining: "+str(statot))

	def MntlTickDn():
		global mntl, statot
		if mntl > 1:
			mntl = mntl-1
			statot = statot+1
			mntlvar.set("Mntl: "+str(mntl))
			statvar.set("Stat Points Remaining: "+str(statot))

	def create():
		from Fighter import fighter
		import WriteFighters
		global atk, dfn, spd, mntl
		custom = fighter(name.get(),atk,dfn,spd,mntl)
		customs = WriteFighters.getCustoms(custom)
	
		file = open('CustomFighters','wb')
		pickle.dump(customs,file)
		file.close()
		creator.grid_forget()
		options.grid()	
		customB['state'] = 'normal'
		pickFighter['state'] = 'normal'
	
	def Back():
		creator.grid_forget()
		options.grid()
		
			

	label = Label(creator, text="Fighter Name:")
	name = Entry(creator, width=20)
	
	strengthU = Button(creator, text=" ^ ", command=StrTickUp)
	strengthL = Label(creator, textvariable=strvar)
	strengthD = Button(creator, text=" v ", command=StrTickDn)
	
	defenseU = Button(creator, text=" ^ ", command=DfnTickUp)
	defenseL = Label(creator, textvariable=defvar)
	defenseD = Button(creator, text=" v ", command=DfnTickDn)

	speedU = Button(creator, text=" ^ ", command=SpdTickUp)
	speedL = Label(creator, textvariable=spdvar)
	speedD = Button(creator, text=" v ", command=SpdTickDn)

	mentalU = Button(creator, text=" ^ ", command=MntlTickUp)
	mentalL = Label(creator, textvariable=mntlvar)
	mentalD = Button(creator, text=" v ", command=MntlTickDn)

	statL = Label(creator, textvariable=statvar)
	statL.grid(row=0, column=1)
	label.grid(row=1,column=0)
	name.grid(row=1,column=1)

	done = Button(creator, text="Done", command=create)

	strengthU.grid(row=2,column=0)
	strengthL.grid(row=3,column=0)
	strengthD.grid(row=4,column=0)
	defenseU.grid(row=2,column=1)
	defenseL.grid(row=3,column=1)
	defenseD.grid(row=4,column=1)
	speedU.grid(row=2,column=2)
	speedL.grid(row=3,column=2)
	speedD.grid(row=4,column=2)
	mentalU.grid(row=2,column=3)
	mentalL.grid(row=3,column=3)
	mentalD.grid(row=4,column=3)
	done.grid(row=1, column=2)

	back = Button(creator, text='Go Back', command=Back)
	back.grid(row=0, column=0)

def start():
	tournament = LabelFrame(root,text='Tournament In Progress')

	canvas = Canvas(tournament)
	canvas.pack(side=LEFT)

	scrollbar = Scrollbar(tournament,orient=VERTICAL,command=canvas.yview)
	scrollbar.pack(side=RIGHT, fill=Y)

	canvas.configure(yscrollcommand=scrollbar.set)
	canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion = canvas.bbox("all")))

	other = Frame(canvas)
	canvas.create_window((0,0),window=other,anchor="nw")

	bracket.main(8,1,currentFighter)
	options.grid_forget()	
	tournament.grid(row=0,column=0)
	file = open('BracketLog','r')
	for i in file:
		report = Label(other,text=i)
		report.pack()
	file.close()

	def lvlup():
		global currentFighter
		lvlvar,atkvar,dfnvar,spdvar,mntlvar = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
		tournament.destroy()
		won = currentFighter.exp
		lvlvar.set(currentFighter.name + ' won ' + str(won) + ' fights.\nPoints still left to distribute: ' + str(currentFighter.exp))
		level = LabelFrame(root,text='Level Up')
		level.grid(row=0,column=0)
		resources = Label(level,textvariable=lvlvar)
		resources.grid(row=0,column=0)

		minatk = currentFighter.atk
		mindfn = currentFighter.dfn
		minspd = currentFighter.spd
		minmntl = currentFighter.mntl

		atkvar.set('Str: ' + str(currentFighter.atk))
		dfnvar.set('Def: ' + str(currentFighter.dfn))
		spdvar.set('Spd: ' + str(currentFighter.spd))
		mntlvar.set('Mntl: '+str(currentFighter.mntl))

		def tickUp(var):
			if currentFighter.exp > 0:
				if var == atkvar:
					currentFighter.atk = currentFighter.atk + 1
					currentFighter.exp = currentFighter.exp - 1
					atkvar.set('Str: ' + str(currentFighter.atk))
					lvlvar.set(currentFighter.name + ' won ' + str(won) + ' fights.\nPoints still left to distribute: ' + str(currentFighter.exp))
				elif var == dfnvar:
					currentFighter.dfn = currentFighter.dfn + 1
					currentFighter.exp = currentFighter.exp - 1
					dfnvar.set('Def: ' + str(currentFighter.dfn))
					lvlvar.set(currentFighter.name + ' won ' + str(won) + ' fights.\nPoints still left to distribute: ' + str(currentFighter.exp))
				elif var == spdvar:
					currentFighter.spd = currentFighter.spd + 1
					currentFighter.exp = currentFighter.exp - 1
					spdvar.set('Spd: ' + str(currentFighter.spd))
					lvlvar.set(currentFighter.name + ' won ' + str(won) + ' fights.\nPoints still left to distribute: ' + str(currentFighter.exp))
				elif var == mntlvar:
					currentFighter.mntl = currentFighter.mntl + 1
					currentFighter.exp = currentFighter.exp - 1
					mntlvar.set('Mntl: '+str(currentFighter.mntl))
					lvlvar.set(currentFighter.name + ' won ' + str(won) + ' fights.\nPoints still left to distribute: ' + str(currentFighter.exp))

		def tickDn(var):
			if var == atkvar:
				if currentFighter.atk > minatk:
					currentFighter.atk = currentFighter.atk - 1
					currentFighter.exp = currentFighter.exp + 1
					atkvar.set('Str: ' + str(currentFighter.atk))
					lvlvar.set(currentFighter.name + ' won ' + str(won) + ' fights.\nPoints still left to distribute: ' + str(currentFighter.exp))
			elif var == dfnvar:
				if currentFighter.dfn > mindfn:
					currentFighter.dfn = currentFighter.dfn - 1
					currentFighter.exp = currentFighter.exp + 1
					dfnvar.set('Def: ' + str(currentFighter.dfn))
					lvlvar.set(currentFighter.name + ' won ' + str(won) + ' fights.\nPoints still left to distribute: ' + str(currentFighter.exp))
			elif var == spdvar:
				if currentFighter.spd > minspd:
					currentFighter.exp = currentFighter.exp + 1
					currentFighter.spd = currentFighter.spd - 1
					spdvar.set('Spd: ' + str(currentFighter.spd))
					lvlvar.set(currentFighter.name + ' won ' + str(won) + ' fights.\nPoints still left to distribute: ' + str(currentFighter.exp))
			elif var == mntlvar:
				if currentFighter.mntl > minmntl:
					currentFighter.mntl = currentFighter.mntl - 1
					currentFighter.exp = currentFighter.exp + 1
					mntlvar.set('Mntl: '+str(currentFighter.mntl))
					lvlvar.set(currentFighter.name + ' won ' + str(won) + ' fights.\nPoints still left to distribute: ' + str(currentFighter.exp))

		def save():
			if currentFighter.exp == 0:
				import WriteFighters
				customs = WriteFighters.save(currentFighter)
				file = open('CustomFighters','wb')
				pickle.dump(customs,file)
				file.close()
				level.grid_forget()
				options.grid()
				currentFighter.updateStats()


		strengthU = Button(level, text=" ^ ", command=lambda: tickUp(atkvar))
		strengthL = Label(level, textvariable=atkvar)
		strengthD = Button(level, text=" v ", command=lambda: tickDn(atkvar))
		
		defenseU = Button(level, text=" ^ ", command=lambda: tickUp(dfnvar))
		defenseL = Label(level, textvariable=dfnvar)
		defenseD = Button(level, text=" v ", command=lambda: tickDn(dfnvar))

		speedU = Button(level, text=" ^ ", command=lambda: tickUp(spdvar))
		speedL = Label(level, textvariable=spdvar)
		speedD = Button(level, text=" v ", command=lambda: tickDn(spdvar))

		mentalU = Button(level, text=" ^ ", command=lambda: tickUp(mntlvar))
		mentalL = Label(level, textvariable=mntlvar)
		mentalD = Button(level, text=" v ", command=lambda: tickDn(mntlvar))

		done = Button(level,text='Done',command=save)

		strengthU.grid(row=2,column=0)
		strengthL.grid(row=3,column=0)
		strengthD.grid(row=4,column=0)
		defenseU.grid(row=2,column=1)
		defenseL.grid(row=3,column=1)
		defenseD.grid(row=4,column=1)
		speedU.grid(row=2,column=2)
		speedL.grid(row=3,column=2)
		speedD.grid(row=4,column=2)
		mentalU.grid(row=2,column=3)
		mentalL.grid(row=3,column=3)
		mentalD.grid(row=4,column=3)
		done.grid(row=0,column=4)

	cont = Button(tournament,text='Continue',command=lvlup)
	cont.pack()


def change():
	customB['state'] = 'disabled'
	bracket8['state'] = 'disabled'
	pickFighter['state'] = 'disabled'

	def pick(f):
		global currentFighter
		currentFighter = f
		f.current = True
		currentvar.set("Your current fighter is: "+f.name)
		selection.grid_forget()
		file.close()
		customB['state'] = 'normal'
		bracket8['state'] = 'normal'
		pickFighter['state'] = 'normal'
	
	file = open('CustomFighters','rb')
	customs = pickle.load(file)
	if customs == []:
		currentvar.set('Please create a custom fighter to participate in tournaments')
		customB['state']='normal'
	else:
		selection = LabelFrame(options,text='Choose a fighter')
		selection.grid(row=2,columnspan=3)
		for i in customs:
			but = Button(selection,text=i.name,command=lambda: pick(i))
			but.pack()


customB = Button(options, text="Create Fighter", command=customFighter)
customB.grid(row=0,column=0)

bracket8 = Button(options, text='Enter an 8 fighter bracket',command=start)
bracket8.grid(row=0,column=1)

currentLabel = Label(options,textvariable=currentvar)
currentLabel.grid(row=1,columnspan=3)

pickFighter = Button(options,text='Change current Fighter',command=change)
pickFighter.grid(row=0,column=2)

if currentFighter == None:
	bracket8['state'] = 'disabled'

root = mainloop()