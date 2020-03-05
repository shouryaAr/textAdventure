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


The following links might help:


https://inventwithpython.com/blog/2014/12/11/making-a-text-adventure-game-with-the-cmd-and-textwrap-python-modules/

(This one looks particularly useful:)
https://www.quora.com/I-am-very-new-to-Python-and-I-want-to-create-a-text-adventure-game-in-Python-How-can-I-do-this





        
3 possible approaches here:

1) Retain 'for' loop, but figure out way to manage situations where dict values that don't match playerMove (eg playerMove is 's' in room 3, but loop gets stuck on 'n', since 'n' != 's').
2) Replace 'for' loop with 'if' or switch statement, search dict_doors for matching key, access value (??seems to make sense??)
3) Remove dictionary, use variables only, use 2) to search through variables somehow

checkDoor = [value for key, value in dict_door.items() if playerMove in key.lower()] #returns a list of values for dict_door where the key matches playerMove. 



#random room selection: Random number selected once, when the game starts. 


"""

import random
import sys

def getExit():
	exitNum = random.randint(2,3)
	return exitNum
	
def playerWins():
	print('You\'re out. Yay. Presumably you found the massive hole in the floor?')
	playAgain = input("Play Again? 'y' or 'n'")
	if playAgain == 'y':
		exitLoc = getExit()
		room1(exitLoc)
	if playAgain == 'n':
		print("Scared, huh? Obviously you hate puzzles with as many as 3 pieces. Let\'s see how you handle my fiendish two piece rubix cube...anyhow, see ya.")
		sys.exit()



	



              


############ ROOM DEFINITIONS BELOW ##########

def room1(exitLocation):
	roomNum = 1

	if exitLocation == roomNum: #checks if player has found exit
		playerWins()

	dict_doors = {       
			'n' : True,
			's' : False,
			'e' : False,
			'w' : False,
			}
			
	playerMove = input('You are in Room 1. Which way do you want to go? Enter n,s,w or e.')
	
	checkDoor = [value for key, value in dict_doors.items() if playerMove in key.lower()] #returns a list of values for dict_door where the key matches playerMove.
	
	if len(checkDoor) >= 1:
		checkDoor = checkDoor[0] #if the list assigned to checkDoor contains at least 1 entry, reassign checkDoor to a pure Boolean 
		
	print('You entered: ' + playerMove + '. The open status for this door is:' + str(checkDoor))

	if checkDoor == True:
		#print('The value is True.')
		if playerMove == 'n':
			print('You move into Room 2.')
			room2(exitLoc)
	elif checkDoor == False:
		#print('The value is False.')
		print('This door is locked.')
		room1(exitLoc)
	else:								#if the player did not enter n,s,w or e. In which case checkDoor should contain an empty list.  
		#print('The value of this variable is neither True nor False.')
		print('um, sense much? You need to enter n,s,w or e.')
		room1(exitLoc)
		

		
		
def room2(exitLocation):
	roomNum = 2

	if exitLocation == roomNum: #checks if player has found exit
		playerWins()

	dict_doors = {       
			'n' : True,
			's' : True,
			'e' : False,
			'w' : False,
			}

	playerMove = input('You are in Room 2. Which way do you want to go? Enter n,s,w or e.')
	
	checkDoor = [value for key, value in dict_doors.items() if playerMove in key.lower()] #returns a list of values for dict_door where the key matches playerMove.
	
	if len(checkDoor) >= 1:
		checkDoor = checkDoor[0] #if the list assigned to checkDoor contains at least 1 entry, reassign checkDoor to a pure Boolean 
		
	print('You entered: ' + playerMove + '. The open status for this door is:' + str(checkDoor))

	if checkDoor == True:
		#print('The value is True.')
		if playerMove == 'n':
			print('You move into Room 3.')
			room3(exitLoc)
		if playerMove == 's':
			print('You move into Room 1.')
			room1(exitLoc)
		
	elif checkDoor == False:
		#print('The value is False.')
		print('This door is locked.')
		room2(exitLoc)
	else:								#if the player did not enter n,s,w or e. In which case checkDoor should contain an empty list.  
		#print('The value of this variable is neither True nor False.')
		print('um, sense much? You need to enter n,s,w or e.')
		room2(exitLoc)




def room3(exitLocation):
	roomNum = 3
	
	if exitLocation == roomNum: #checks if player has found exit
		playerWins()
			

	dict_doors = {       
			'n' : False,
			's' : True,
			'e' : False,
			'w' : False,
			}
			

	playerMove = input('You are in Room 3. Which way do you want to go? Enter n,s,w or e.')
	
	checkDoor = [value for key, value in dict_doors.items() if playerMove in key.lower()] #returns a list of values for dict_door where the key matches playerMove.
	
	if len(checkDoor) >= 1:
		checkDoor = checkDoor[0] #if the list assigned to checkDoor contains at least 1 entry, reassign checkDoor to a pure Boolean (the first entry in the list) 
		
	print('You entered: ' + playerMove + '. The open status for this door is:' + str(checkDoor))

	if checkDoor == True:
		#print('The value is True.')
		if playerMove == 's':
			print('You move into Room 2.')
			room2(exitLoc)
	elif checkDoor == False:
		#print('The value is False.')
		print('This door is locked.')
		room3(exitLoc)
	else:								#if the player did not enter n,s,w or e. In which case checkDoor should contain an empty list.  
		#print('The value of this variable is neither True nor False.')
		print('um, sense much? You need to enter n,s,w or e.')
		room3(exitLoc)



##################
    
         
exitLoc = getExit()          

room1(exitLoc)   









        
                
