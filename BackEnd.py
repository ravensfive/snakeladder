#import random package
import random, json

# setup json
def setupJson() :
    global playerdata
    playerdata = {}
    playerdata['players'] = []

# add player to the json, called with parameters
def addplayertoJson(ID,Name,nextPlay,didPlay) :
    playerdata['players'].append({    
    'ID': ID ,
    'Name': Name,
    'Score': "0",
    'nextPlay': nextPlay,
    'didPlay': didPlay
    })

# setup game
def setupGame() :

    global ladders, snakes, gameSize

    # store variable to control setup
    gameReady = False

    # loop through until ready
    while gameReady == False :
        gameSize = input("What is the maximum score, must be a multiple of 10!")
        gameSize = int(gameSize)
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
                playerKey = input("Input the players name?",)
                if playerKey != "" :
                    addplayertoJson(i,playerKey,nextPlay,False)
                else :
                    playerKey = "Player" + str(i)
                    addplayertoJson(i,playerKey,nextPlay,False)
                    print("No player entered, entry recorded as Player", i)
                # write out data to json file
            with open('player.json', 'w') as outfile:  
                   json.dump(playerdata, outfile) 

# setup the game
setupGame()

# setup the players
createPlayerDict(setupPlayers())


def playTurn() :

    # load json
    with open('player.json') as json_file :  
        playerdata = json.load(json_file)
        
    for p in playerdata['players']:
        
        print(p['ID'],p['Name'],p['Score'], p['nextPlay'])

        if p['nextPlay'] == True :
            diceRoll = random.randint(1,6)
            print(str(diceRoll))
            p['Score'] = str(int(p['Score']) + diceRoll)
            p['nextPlay'] = False
            p['didPlay'] = True
         
            print(p['ID'],p['Name'],p['Score'], p['nextPlay'])    

    print(playerdata)
    
    with open('player.json', 'w') as outfile:  
        json.dump(playerdata, outfile) 

    # did they land on a snake or a ladder
    # did they win
    # return json

playTurn()

# play the game function
def playGame() :
    global winner

# set winner default
    winner = 0

    # open json file
    with open('player.json') as json_file:  
        playerdata = json.load(json_file)

    # loop through to player json file until you hit winner
    while winner == 0 :
        
        # loop through player json file
        for p in playerdata['players']:
            #InputString = k + "'s turn, your current score is " + str(playerDict[k]) + ". Press enter to roll the dice!"
            #input(InputString)
            # roll the dice
            #rollDice()
            # update player score
            #p['Score'] = int(p['Score']) + DiceValue
            # feedback score to player
            #print(p['Name'], ", you rolled a ", str(DiceValue), " and your new score is ", int(p['Score']))

            # test if the position landed is a ladder
            for a in ladders :
                if a == int(p['Score']) : 
                    p['Score'] = int(p['Score']) + random.randint(10,20)
                    print(p['Name'], ", congratulations, you landed on a ladder moving forward to ", int(p['Score']) )

            # test if the position landed on is a snake
            for b in snakes :
                if b == int(p['Score']) : 
                    p['Score'] = int(p['Score']) - random.randint(10,20)
                    print(p['Name'], "how unfortunate, you landed on a snake moving back to ", int(p['Score']) )

            print(playerdata)

            # test if the current players score is over 100
            if  int(p['Score']) >= gameSize :
                winner = p['Name']

    print(winner, "wins the game")

    with open('player.json', 'w') as outfile:  
        json.dump(playerdata, outfile) 



# start game
#playGame()

