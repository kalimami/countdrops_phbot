from phBot import *
import QtBind

gui = QtBind.init(__name__,'CountDrops')

metaby = QtBind.createLabel(gui,'by Kardamot // Hellixir',11,267)
lCIZGI = QtBind.createLabel(gui,'_____________________',11,18)
lTITAN = QtBind.createLabel(gui,'TITAN DROPS',40,10)
lLMP = QtBind.createLabel(gui,'Lucky Magic Powder',11,40)
lSTRScroll = QtBind.createLabel(gui,'STR 5 Increase Scroll',11,55)
lINTScroll = QtBind.createLabel(gui,'INT 5 Increase Scroll',11,70)
lHPIceFlakes = QtBind.createLabel(gui,'Very Cold Ice Flakes',11,85)
lMPIceFlakes = QtBind.createLabel(gui,'Cold Ice Flakes',11,100)
lDualIceFlakes = QtBind.createLabel(gui,'Frozen Ice Flakes',11,115)
lHPScroll = QtBind.createLabel(gui,'500 HP Increase Scroll',11,130)
lMPScroll = QtBind.createLabel(gui,'500 MP Increase Scroll',11,145)
lHitScroll = QtBind.createLabel(gui,'Hit Scroll',11,160)
lDodgingScroll = QtBind.createLabel(gui,'Dodging Scroll',11,175)
lTriggerScroll = QtBind.createLabel(gui,'Trigger Scroll',11,190)
lsceva = QtBind.createLabel(gui,'Scroll of Evasion',11,205)
lscacc = QtBind.createLabel(gui,'Scroll of Accuracy',11,220)
qLMP = QtBind.createLabel(gui,'0',130,40)
qSTRScroll = QtBind.createLabel(gui,'0',130,55)
qINTScroll = QtBind.createLabel(gui,'0',130,70)
qHPIceFlakes = QtBind.createLabel(gui,'0',130,85)
qMPIceFlakes = QtBind.createLabel(gui,'0',130,100)
qDualIceFlakes = QtBind.createLabel(gui,'0',130,115)
qHPScroll = QtBind.createLabel(gui,'0',130,130)
qMPScroll = QtBind.createLabel(gui,'0',130,145)
qHitScroll = QtBind.createLabel(gui,'0',130,160)
qDodgingScroll = QtBind.createLabel(gui,'0',130,175)
qTriggerScroll = QtBind.createLabel(gui,'0',130,190)
qsceva = QtBind.createLabel(gui,'0',130,205)
qscacc = QtBind.createLabel(gui,'0',130,220)

lCIZGI = QtBind.createLabel(gui,'_____________________',164,18)
lAttStones = QtBind.createLabel(gui,'ATTRIBUTE STONES',180,10)
lCourage = QtBind.createLabel(gui,'Courage',164,40)
lPhilosophy = QtBind.createLabel(gui,'Philosophy',164,55)
lFocus = QtBind.createLabel(gui,'Focus',164,70)
lChallenge = QtBind.createLabel(gui,'Challenge',164,85)
lAgility = QtBind.createLabel(gui,'Agility',164,100)
lWarriors = QtBind.createLabel(gui,'Warriors',164,115)
lMeditation = QtBind.createLabel(gui,'Meditation',164,130)
lFlesh = QtBind.createLabel(gui,'Flesh',164,145)
lMind = QtBind.createLabel(gui,'Mind',164,160)
lDodging = QtBind.createLabel(gui,'Dodging',164,175)
lLife = QtBind.createLabel(gui,'Life',164,190)
lSpirit = QtBind.createLabel(gui,'Spirit',164,205)
lTraining = QtBind.createLabel(gui,'Training',164,220)
lPrayer = QtBind.createLabel(gui,'Prayer',164,235)
qcourage = QtBind.createLabel(gui,'0',283,40)
qphilosophy = QtBind.createLabel(gui,'0',283,55)
qfocus = QtBind.createLabel(gui,'0',283,70)
qchallenge = QtBind.createLabel(gui,'0',283,85)
qagility = QtBind.createLabel(gui,'0',283,100)
qwarriors = QtBind.createLabel(gui,'0',283,115)
qmeditation = QtBind.createLabel(gui,'0',283,130)
qflesh = QtBind.createLabel(gui,'0',283,145)
qmind = QtBind.createLabel(gui,'0',283,160)
qdodging = QtBind.createLabel(gui,'0',283,175)
qlife = QtBind.createLabel(gui,'0',283,190)
qspirit = QtBind.createLabel(gui,'0',283,205)
qtraining = QtBind.createLabel(gui,'0',283,220)
qprayer = QtBind.createLabel(gui,'0',283,235)

lCIZGI = QtBind.createLabel(gui,'_____________________',317,18)
lMagStones = QtBind.createLabel(gui,'MAGIC STONES',344,10)
lSTR = QtBind.createLabel(gui,'Str',317,40)
lINT = QtBind.createLabel(gui,'Int',317,55)
lMaster = QtBind.createLabel(gui,'Master',317,70)
lStrikes = QtBind.createLabel(gui,'Strikes',317,85)
lDiscipline = QtBind.createLabel(gui,'Discipline',317,100)
lPenetration = QtBind.createLabel(gui,'Penetration',317,115)
lDodging2 = QtBind.createLabel(gui,'Dodging',317,130)
lStamina = QtBind.createLabel(gui,'Stamina',317,145)
lMagic = QtBind.createLabel(gui,'Magic',317,160)
lFogs = QtBind.createLabel(gui,'Fogs',317,175)
lAir = QtBind.createLabel(gui,'Air',317,190)
lFire = QtBind.createLabel(gui,'Fire',317,205)
lImmunity = QtBind.createLabel(gui,'Immunity',317,220)
lRevival = QtBind.createLabel(gui,'Revival',317,235)
lLuck = QtBind.createLabel(gui,'Luck',317,250)
lSteady = QtBind.createLabel(gui,'Steady',317,265)
qstr = QtBind.createLabel(gui,'0',436,40)
qint = QtBind.createLabel(gui,'0',436,55)
qmaster = QtBind.createLabel(gui,'0',436,70)
qstrikes = QtBind.createLabel(gui,'0',436,85)
qdiscipline = QtBind.createLabel(gui,'0',436,100)
qpenetration = QtBind.createLabel(gui,'0',436,115)
qdodging2 = QtBind.createLabel(gui,'0',436,130)
qstamina = QtBind.createLabel(gui,'0',436,145)
qmagic = QtBind.createLabel(gui,'0',436,160)
qfogs = QtBind.createLabel(gui,'0',436,175)
qair = QtBind.createLabel(gui,'0',436,190)
qfire = QtBind.createLabel(gui,'0',436,205)
qimmunity = QtBind.createLabel(gui,'0',436,220)
qrevival = QtBind.createLabel(gui,'0',436,235)
qluck = QtBind.createLabel(gui,'0',436,250)
qsteady = QtBind.createLabel(gui,'0',436,265)

lCIZGI = QtBind.createLabel(gui,'_____________________',565,120)
lElixirs = QtBind.createLabel(gui,'ELIXIRS',610,116)
lWeapon = QtBind.createLabel(gui,'Weapon',565,137)
lProtector = QtBind.createLabel(gui,'Protector',565,152)
lAccessory = QtBind.createLabel(gui,'Accessory',565,167)
lShield = QtBind.createLabel(gui,'Shield',565,182)
qweapon = QtBind.createLabel(gui,'0',684,137)
qprotector = QtBind.createLabel(gui,'0',684,152)
qaccessory = QtBind.createLabel(gui,'0',684,167)
qshield = QtBind.createLabel(gui,'0',684,182)

lCIZGI = QtBind.createLabel(gui,'_____________________',565,204)
lCoins = QtBind.createLabel(gui,'COINS',610,200)
lGoldC = QtBind.createLabel(gui,'Gold Coin',565,220)
lSilverC = QtBind.createLabel(gui,'Silver Coin',565,235)
lCopperC = QtBind.createLabel(gui,'Copper Coin',565,251)
lIronC = QtBind.createLabel(gui,'Iron Coin',565,268)
qgold = QtBind.createLabel(gui,'0',684,220)
qsilver = QtBind.createLabel(gui,'0',684,235)
qcopper = QtBind.createLabel(gui,'0',684,251)
qiron = QtBind.createLabel(gui,'0',684,268)

lLIST = QtBind.createList(gui,150,40,1,207)
lLIST2 = QtBind.createList(gui,303,40,1,220)
lLIST3 = QtBind.createList(gui,455,40,1,240)
lLIST4 = QtBind.createList(gui,540,135,1,155)
lLIST5 = QtBind.createList(gui,720,135,1,155)
lBUTTONBG = QtBind.createList(gui,540,15,180,88)
lNEREYAZI = QtBind.createLabel(gui,'Where do you want to look?',565,8)
btnStorage = QtBind.createButton(gui,'btnStorage_clicked',"  Look at Storage  ",584,52)
btnGuildStorage = QtBind.createButton(gui,'btnGuildStorage_clicked',"  Look at Guild Storage  ",572,75)
btnInventory = QtBind.createButton(gui,'btnInventory_clicked',"  Look at Inventory  ",579,29)
leDegree = QtBind.createLineEdit(gui,"11",470,150,19,19)
lDegree = QtBind.createLabel(gui,'Degree',494,153)


def btnStorage_clicked():
	countIn = 'Storage'
	countItems(countIn)

def btnGuildStorage_clicked():
	countIn = 'GuildStorage'
	countItems(countIn)

def btnInventory_clicked():
	countIn = 'Inventory'
	countItems(countIn)


def countItems(countIn):
	LMP = 0
	STRScroll = 0
	INTScroll = 0
	HPIceFlakes = 0
	MPIceFlakes = 0
	DualIceFlakes = 0
	HPScroll = 0
	MPScroll = 0
	HitScroll = 0
	DodgingScroll = 0
	TriggerScroll = 0
	sceva = 0
	scacc = 0
	courage = 0
	philosophy = 0
	focus = 0
	challenge = 0
	agility = 0
	warriors = 0
	meditation = 0
	flesh = 0
	mind = 0
	pdodging = 0
	life = 0
	spirit = 0
	training = 0
	prayer = 0
	Str = 0
	Int = 0
	master = 0
	strikes = 0
	discipline = 0
	penetration = 0
	gdodging = 0
	stamina = 0
	magic = 0
	fogs = 0
	air = 0
	fire = 0
	immunity = 0
	revival = 0
	luck = 0
	steady = 0
	weapon = 0
	protector = 0
	accessory = 0
	shield = 0
	gold = 0
	silver = 0
	copper = 0
	iron = 0
	items = []
	if countIn == 'Storage':
		items = get_storage()['items']
	elif countIn == 'GuildStorage':
		items = get_guild_storage()['items']
	elif countIn == 'Inventory':
		items = get_inventory()['items']
	degree = str(QtBind.text(gui,leDegree))
	if items != []:
		for item in items:
			if item != None and degree in item['name'] and 'tablet' not in item['name'] and 'stone' in item['name']:
				if "courage" in item['name']:
					courage += item['quantity']
				elif "philosophy" in item['name']:
					philosophy += item['quantity']
				elif "focus" in item['name']:
					focus += item['quantity']
				elif "challenge" in item['name']:
					challenge += item['quantity']
				elif "agility" in item['name']:
					agility += item['quantity']
				elif "warriors" in item['name']:
					warriors += item['quantity']
				elif "meditation" in item['name']:
					meditation += item['quantity']
				elif "flesh" in item['name']:
					flesh += item['quantity']
				elif "mind" in item['name']:
					mind += item['quantity']
				elif "Attribute stone of dodging" in item['name']:
					pdodging += item['quantity']
				elif "life" in item['name']:
					life += item['quantity']
				elif "spirit" in item['name']:
					spirit += item['quantity']
				elif "training" in item['name']:
					training += item['quantity']
				elif "prayer" in item['name']:
					prayer += item['quantity']				
				elif "Str" in item['name']:
					Str += item['quantity']
				elif "Int" in item['name']:
					Int += item['quantity']
				elif "master" in item['name']:
					master += item['quantity']
				elif "strikes" in item['name']:
					strikes += item['quantity']
				elif "discipline" in item['name']:
					discipline += item['quantity']
				elif "penetration" in item['name']:
					penetration += item['quantity']
				elif "Magic stone of dodging" in item['name']:
					gdodging += item['quantity']
				elif "stamina" in item['name']:
					stamina += item['quantity']
				elif "magic" in item['name']:
					magic += item['quantity']
				elif "fogs" in item['name']:
					fogs += item['quantity']
				elif "air" in item['name']:
					air += item['quantity']
				elif "immunity" in item['name']:
					immunity += item['quantity']
				elif "revival" in item['name']:
					revival += item['quantity']
				elif "fire" in item['name']:
					fire += item['quantity']
				elif "steady" in item['name']:
					steady += item['quantity']
				elif "luck" in item['name']:
					luck += item['quantity']				
			if item != None and "Magic" in item['name'] and "Powder" in item['name']:
				LMP += item['quantity']
			if item != None and "Strength" in item['name'] and "Scroll" in item['name']:
				STRScroll += item['quantity']
			if item != None and "Intelligence" in item['name'] and "Scroll" in item['name']:
				INTScroll += item['quantity']
			if item != None and "Very Cold" in item['name'] and "Flakes" in item['name']:
				HPIceFlakes += item['quantity']
			if item != None and "Cold" in item['name'] and "Very" not in item['name']:
				MPIceFlakes += item['quantity']
			if item != None and "Frozen" in item['name'] and "Flakes" in item['name']:
				DualIceFlakes += item['quantity']
			if item != None and "HP" in item['name'] and "Scroll" in item['name']:
				HPScroll += item['quantity']
			if item != None and "MP" in item['name'] and "Scroll" in item['name']:
				MPScroll += item['quantity']
			if item != None and "Hit" in item['name'] and "Scroll" in item['name']:
				HitScroll += item['quantity']
			if item != None and "Dodging" in item['name'] and "Scroll" in item['name']:
				DodgingScroll += item['quantity']
			if item != None and "Trigger" in item['name'] and "Scroll" in item['name']:
				TriggerScroll += item['quantity']
			if item != None and "Scroll" in item['name'] and "Evasion" in item['name']:
				sceva += item['quantity']
			if item != None and "Scroll" in item['name'] and "Accuracy" in item['name']:
				scacc += item['quantity']
			if item != None and "Intensifing" in item['name'] and "(weapon)" in item['name']:
				weapon += item['quantity']
			if item != None and "Intensifing" in item['name'] and "(protector)" in item['name']:
				protector += item['quantity']
			if item != None and "Intensifing" in item['name'] and "(accessory)" in item['name']:
				accessory += item['quantity']
			if item != None and "Intensifing" in item['name'] and "(Shield)" in item['name']:
				shield += item['quantity']
			if item != None and "Coin" in item['name'] and "Gold" in item['name']:
				gold += item['quantity']
			if item != None and "Coin" in item['name'] and "Silver" in item['name']:
				silver += item['quantity']
			if item != None and "Coin" in item['name'] and "Copper" in item['name']:
				copper += item['quantity']
			if item != None and "Coin" in item['name'] and "Iron" in item['name']:
				iron += item['quantity']
	QtBind.setText(gui,qLMP,str(LMP))
	QtBind.setText(gui,qSTRScroll,str(STRScroll))
	QtBind.setText(gui,qINTScroll,str(INTScroll))
	QtBind.setText(gui,qHPIceFlakes,str(HPIceFlakes))
	QtBind.setText(gui,qMPIceFlakes,str(MPIceFlakes))
	QtBind.setText(gui,qDualIceFlakes,str(DualIceFlakes))
	QtBind.setText(gui,qHPScroll,str(HPScroll))
	QtBind.setText(gui,qMPScroll,str(MPScroll))
	QtBind.setText(gui,qHitScroll,str(HitScroll))
	QtBind.setText(gui,qDodgingScroll,str(DodgingScroll))
	QtBind.setText(gui,qTriggerScroll,str(TriggerScroll))
	QtBind.setText(gui,qsceva,str(sceva))	
	QtBind.setText(gui,qscacc,str(scacc))	
	QtBind.setText(gui,qcourage,str(courage))
	QtBind.setText(gui,qphilosophy,str(philosophy))
	QtBind.setText(gui,qfocus,str(focus))
	QtBind.setText(gui,qchallenge,str(challenge))
	QtBind.setText(gui,qagility,str(agility))
	QtBind.setText(gui,qwarriors,str(warriors))
	QtBind.setText(gui,qmeditation,str(meditation))
	QtBind.setText(gui,qflesh,str(flesh))
	QtBind.setText(gui,qmind,str(mind))
	QtBind.setText(gui,qdodging,str(pdodging))
	QtBind.setText(gui,qlife,str(life))
	QtBind.setText(gui,qspirit,str(spirit))
	QtBind.setText(gui,qtraining,str(training))
	QtBind.setText(gui,qprayer,str(prayer))
	QtBind.setText(gui,qstr,str(Str))
	QtBind.setText(gui,qint,str(Int))
	QtBind.setText(gui,qmaster,str(master))
	QtBind.setText(gui,qstrikes,str(strikes))
	QtBind.setText(gui,qdiscipline,str(discipline))
	QtBind.setText(gui,qpenetration,str(penetration))
	QtBind.setText(gui,qdodging2,str(gdodging))
	QtBind.setText(gui,qstamina,str(stamina))
	QtBind.setText(gui,qmagic,str(magic))
	QtBind.setText(gui,qfire,str(fire))
	QtBind.setText(gui,qair,str(air))
	QtBind.setText(gui,qfogs,str(fogs))
	QtBind.setText(gui,qrevival,str(revival))
	QtBind.setText(gui,qimmunity,str(immunity))
	QtBind.setText(gui,qluck,str(luck))
	QtBind.setText(gui,qsteady,str(steady))
	QtBind.setText(gui,qweapon,str(weapon))
	QtBind.setText(gui,qprotector,str(protector))
	QtBind.setText(gui,qaccessory,str(accessory))
	QtBind.setText(gui,qshield,str(shield))
	QtBind.setText(gui,qgold,str(gold))
	QtBind.setText(gui,qsilver,str(silver))
	QtBind.setText(gui,qcopper,str(copper))
	QtBind.setText(gui,qiron,str(iron))
	
log('Plugins: [CountDrops v1.2] successfully loaded')
