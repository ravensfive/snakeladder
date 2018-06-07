#import random package
import random

gameReady = False

#while gameReady == False :
gameSize = input("What is the maximum score, must be a multiple of 10!")
gameSize = int(gameSize)
    #if gameSize / 10 == int(gameSize/10) :
ladderFactor = 10
snakeFactor =  10
gameReady = True
       # print("Game initiated, at size", gameSize)
    #else :
     #   gameSize = input("What is the maximum score, must be a multiple of 10!")

# dice roll, returns a value between 1 and 6
def rollDice() :
    global DiceValue
    DiceValue = random.randint(1,6)

# how many players are player, user input, must be a number between 2 and 5
def setupPlayers():
    global numPlayers
    numPlayers=0
    while True:
        try:
            print("How many players are in the game?")
            numPlayers = int(input())
            if numPlayers > 4 or numPlayers < 2:
                print("Must be a number greater than 1 and less than 5")
            else:
                return numPlayers
        except:
            print("Must be a number")

# create player dictionary, setup number of players and initial 0 value
def createPlayerDict(numPlayers):
    global playerDict
    if numPlayers > 4 or numPlayers < 2:
            return "Must be a number greater than 1 and less than 5"
    else:
            playerDict = {}
            i = 0
            for i in range(1,numPlayers+1) :
                playerKey = input("Input the players name?",)
                if playerKey != "" :
                    playerDict[playerKey] = 0
                else :
                    playerKey = "Player" + str(i)
                    playerDict[playerKey] = 0
                    print("No player entered, entry recorded as Player", i)
    return str(playerDict)

# setup game and instantiate player dictionary
createPlayerDict(setupPlayers())

# play the game function
def playGame() :
    global winner
    ladders = []
    snakes = []
    l = 0
    s = 0

    for l in range(1,random.randint(5,10)+1) :
        ladders.append(random.randint(1,90))
    #ladders = {5,15,25,35,45,55,65,75,85,95}
    for s in range(1,random.randint(5,10)+1) :
        snakes.append(random.randint(10,99))
       
    #snakes = {10,20,30,40,50,60,70,80,90}

    print("Ladders are at postions ", ladders)
    print("Snakes are at positions ", snakes)

# set winner default
    winner = 0

    # loop through to player dictionary until you hit winner
    while winner == 0 :
        
        # loop through player dictionary
        for k in playerDict :
            #InputString = k + "'s turn, your current score is " + str(playerDict[k]) + ". Press enter to roll the dice!"
            #input(InputString)
            # roll the dice
            rollDice()
            # update player score
            playerDict[k] = playerDict[k] + DiceValue
            # feedback score to player
            print(k, ", you rolled a ", str(DiceValue), " and your new score is ", playerDict[k])

            # test if the position landed is a ladder
            for a in ladders :
                if a == playerDict[k] : 
                    playerDict[k] = playerDict[k] + random.randint(10,20)
                    print(k, ", congratulations, you landed on a ladder moving forward to ", playerDict[k] )

            # test if the position landed on is a snake
            for b in snakes :
                if b == playerDict[k] : 
                    playerDict[k] = playerDict[k] - random.randint(10,20)
                    print(k, "how unfortunate, you landed on a snake moving back to ", playerDict[k] )

            print(playerDict)

            # test if the current players score is over 100
            if  playerDict[k] >= gameSize :
                winner = [k]

    print(winner, "wins the game")

# start game
playGame()

