"""
Player moves from room to room
Sometimes encounters enemies
Sometimes encounters ppl who want to trade
Objective: Collect 10 coins

-player
-rooms
-other characters

-player inventory



***

10 rooms
1 contains exit
Player must find exit


1) Create room object
2) Create player object
3) Assign exit to a room 
 
***



10 rooms
5 coins
Move from room to room
Some rooms contain a coin
No room contains >1 coin
-Building layout


***


"""
# ***	THE BELOW IS JUST A TEST TO DEMONSTRATE MOVING BETWEEN 3 ROOMS ***

playerLocation = 0


dictRoom0C = {
			'northOpen':True,
			'southOpen':False,
			'eastOpen':False,
			'westOpen':False,
		}
			
			
dictRoom1C = {
			'northOpen':True,
			'southOpen':True,
			'eastOpen':False,
			'westOpen':False,
		}		

dictRoom2C = {
			'northOpen':False,
			'southOpen':True,
			'eastOpen':False,
			'westOpen':False,
		}		


rooms = [dictRoom0C,dictRoom1C,dictRoom2C]


import random

def getEntry():
	entry = random.randint(0,2) #used to assign an integer to the variable 'exit'. This will later be used to select the room containing the exit. 
	return entry
	
#playerLocation = getEntry()
playerLocation = rooms[getEntry()]

print(playerLocation) #think this will print the dictionary for the given room. 

print('You start in room ' + str(playerLocation) + '.')


def tryToMove():
		
	playerMove = input("Which way do you want to go? Enter 'n','s','e' or 'w'. ")
										
	#check if playerMove is an unlocked door: 

	if playerMove.title() == 'N':
		playerMove = 'northOpen' 		#reassign playerMove as dictionary key. (may eliminate this)
	elif playerMove.title() == 'S':
		playerMove = 'southOpen'
	elif playerMove.title() == 'E':
		playerMove = 'eastOpen'
	elif playerMove.title() == 'W':
		playerMove = 'westOpen'
	else:
		print('Enter a letter, dingbeetle.')
		tryToMove()
	
	
	return playerMove
	
nonFuncPlayerMove = tryToMove()

if playerLocation[nonFuncPlayerMove] == True:
	print('You move ' +nonFuncPlayerMove.replace('Open','') + '.')
	"""
	Search playerLocation (a dictionary name, eg dict01C) within the list Rooms
	Return the int location of the matching dictionary within list Rooms
	"""
	numberedLocation = rooms.index(playerLocation) #?? apparently using dictionary names to store info is a bad idea?? What's the alternative? 
	
elif playerLocation[nonFuncPlayerMove] == False:
	print('You cannot move ' + nonFuncPlayerMove.replace('Open','') + '.')
	nonFuncPlayerMove = tryToMove()







		
	

			




# class Room(object):
	# def __init__(self,Ndoor,Edoor,Wdoor,Sdoor):
		
		# self.Ndoor = Ndoor  #semicolon may be needed here (at end of each line)
		# self.Edoor = Edoor
		# self.Wdoor = Wdoor
		# self.Sdoor = Sdoor
		




