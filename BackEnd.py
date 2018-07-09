#import random package
import random, json

# setup json
def setupJson() :
    global playerdata
    playerdata = {}
    playerdata['players'] = []
    print ("JSON Setup")

# add player to the json, called with parameters
def addplayertoJson(ID,Name,lastScore,lastRoll,nextPlay,didPlay,hasWon,numGoes) :
    playerdata['players'].append({    
    'ID': ID ,
    'Name': Name,
    'lastScore': lastScore,
    'lastRoll': lastRoll,
    'Score': "0",
    'nextPlay': nextPlay,
    'didPlay': didPlay,
    'hasWon': hasWon,
    'numGoes': numGoes

    })

# setup game
def setupGame() :

    global ladders, snakes, gameSize

    # store variable to control setup
    gameReady = False
    print (gameReady)

    # loop through until ready
    while gameReady == False :
        #gameSize = input("What is the maximum score, must be a multiple of 10!")
        #gameSize = int(gameSize)
        gameSize = 100
        #if gameSize / 10 == int(gameSize/10) :
        factor = int(gameSize / 10)
        gameReady = True
        print("Game initiated, at size", gameSize)
        #else :
        #   gameSize = input("What is the maximum score, must be a multiple of 10!")
        print("Randomising ladders and snakes")
        ladders = []
        snakes = []
        l=0
        s=0

        for l in range(1,factor) :
            ladders.append(random.randint(1,90))
        
        for s in range(1,factor) :
            snakes.append(random.randint(10,99))

        print("Ladders are at postions ", ladders)
        print("Snakes are at positions ", snakes)

        # call to setup json
        setupJson()
        print("JSON Setup")

        return None

# how many players are player, user input, must be a number between 2 and 5
def setupPlayers():
    global numPlayers
    numPlayers=0
    while True:
        try:
            print("How many players are in the game?")
            numPlayers = int(input())
            return numPlayers
        except:
            print("Must be a number")

# create player dictionary, setup number of players and initial 0 value
def createPlayerDict(numPlayers):
            i = 0
            for i in range(1,numPlayers+1) :
                if i == 1 :
                    nextPlay = True
                else :
                    nextPlay = False
                    
                playerKey = input("Input the players name?")

                if playerKey != "" :
                    addplayertoJson(i,playerKey,0,0,nextPlay,False,False,0)
                else :
                    playerKey = "Player" + str(i)
                    addplayertoJson(i,playerKey,0,0,nextPlay,False,False,0)
                    print("No player entered, entry recorded as Player", i)
                # write out data to json file
            #with open('player.json', 'w') as outfile:  
            #       json.dump(playerdata, outfile) 

# setup the game
#setupGame()

# setup the players
#createPlayerDict(setupPlayers())

def playTurn() :

    playingPlayerID = 0

    # load json
    #with open('player.json') as json_file :  
    #    playerdata = json.load(json_file)
        
    for p in playerdata['players']:    

        if p['nextPlay'] == True :
  
            diceRoll = random.randint(1,6)
            p['lastRoll'] = diceRoll
            p['lastScore'] = p['Score']
            p['Score'] = str(int(p['Score']) + diceRoll)
            p['numGoes'] = p['numGoes'] + 1
            p['nextPlay'] = False
            p['didPlay'] = True

            # set next player
            playingPlayerID = int(p['ID'])

            if int(p['Score']) >= gameSize :
                p['hasWon'] = True

    # set next player
    if playingPlayerID == len(playerdata['players']) :
        playerdata['players'][0]['nextPlay'] = True        
    else :
        playerdata['players'][playingPlayerID]['nextPlay'] = True

    print(playerdata)
    
    # did they land on a snake or a ladder
    # did they win

def playGame() :
    
    # ***** Si, you need to replicate something like this for the front end
    winner = ""

    while winner == "" :
        # this simulates your button press
        input('Press enter to roll the dice')
        # this calls the generic play turn function
        playTurn()
        # this loops through the player json and tests if there has been a winner, I think you will
        # need to expand this to also extract the following information :
        # all player current scores, who's turn is it next, who just played, has anyone won and who
        # also typing this up, we will also need to add a last score to the json, so you can provide the result back
        # ****done this 18/06/2018 - added last score, last roll and num of goes**** 
        for p in playerdata['players'] :   
            if p['hasWon'] == True :
                winner = p['Name']
                print(winner)
    return("The winner is " + winner)    
    #return winner       
                

    with open('player.json', 'w') as outfile:  
        json.dump(playerdata, outfile) 



#playGame()

    # open json file
    #with open('player.json') as json_file:  
     #   playerdata = json.load(json_file)
if __name__ == '__main__':

    playGame()
    playTurn()
    setupGame()   
    setupPlayers()
    createPlayerDict(setupPlayers)

