
import random

def func_GetRandom():       #function to generate random number
    randVar = random.randint(0,1000)
    return randVar
    
x = func_GetRandom()        #generates an initial value for the random number when code is first run

def level1(randVar):
    print('The game has progressed to level 1. The random value is',randVar)
    level2(randVar)

def level2(randVar):
    print('The game has progressed to level 2. The random value is',randVar)
    restartGame = input('Restart game? Y/N')
    if restartGame.upper() == 'Y':
        gameRestart()
        
def startGame(randVar):
    print('The game has started. The random value is:',randVar)
    level1(randVar)
   
def gameRestart():    #generates a new random number when the game restarts
    x = func_GetRandom()
    print('The game has restarted. The random value is',x)
    startGame(x)
    

startGame(x)





    



    

    

    





