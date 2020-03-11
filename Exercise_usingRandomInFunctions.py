
import random

def func_GetRandom():       #function to generate random number
    randVar = random.randint(0,1000)
    return randVar
    
x = func_GetRandom()        #generates an initial value for the random number when code is first run


def startGame(randomNumber):
    print('The game has started. The random value is:',randomNumber)
    level1(randomNumber)
    
def level1(randomNumber):
    print('The game has progressed to level 1. The random value is',randomNumber)
    level2(randomNumber)

def level2(randomNumber):
    print('The game has progressed to level 2. The random value is',randomNumber)
    restartGame = input('Restart game? Y/N')
    if restartGame.upper() == 'Y':
        gameRestart()

def gameRestart():    #generates a new random number when the game restarts
    x = func_GetRandom()
    print('The game has restarted. The random value is',x)
    startGame(x)
    

startGame(x)





    



    

    

    





