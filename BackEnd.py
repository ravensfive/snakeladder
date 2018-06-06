#import random package
import random

# dice roll, returns a value between 1 and 6
def rollDice() :
    global DiceValue
    DiceValue = random.randint(1,6)

# how many players are player, user input, must be a number between 2 and 5
def setupPlayers():
    players=0
    while True:
        try:
            print("How many players are in the game?")
            players = int(input())
            if players > 4 or players < 2:
                print("Must be a number greater than 1 and less than 5")
            else:
                return players
        except:
            print("Must be a number")

# create player dictionary, setup number of players and initial 0 value
def createPlayerDict(numPlayers):
    global playerDict
    playerDict = {}
    i = 0
    for i in range(1,numPlayers+1) :
        playerKey = str(i)
        playerDict[playerKey] = 0

# setup game and instantiate player dictionary
createPlayerDict(setupPlayers())


# play the game function
def playGame() :
  ladders = {5,15,25,35,45,55,65,75,85,95}
  snakes = {10,20,30,40,50,60,70,80,90}

# set winner default
  winner = 0

  # loop through to player dictionary until you hit winner
  while winner == 0 :
    
    # loop through player dictionary
    for k in playerDict :
        print("Player ", k,"'s turn, your current score is", playerDict[k])
        input("Press enter to roll the dice")
        # roll the dice
        rollDice()
        # update player score
        playerDict[k] = playerDict[k] + DiceValue
        # feedback score to player
        print("You rolled a ", str(DiceValue), " and your new score is ", playerDict[k])

        # test if the position landed is a ladder
        for a in ladders :
            if a == playerDict[k] : 
                playerDict[k] = playerDict[k] + 3
                print("Well done Cock, you landed on a ladder moving forward to ", playerDict[k] )

        # test if the position landed on is a snake
        for b in snakes :
            if b == playerDict[k] : 
                playerDict[k] = playerDict[k] - 3
                print("How unfortunate you cunt, you landed on a snake moving back to ", playerDict[k] )

        # test if the current players score is over 100
        if  playerDict[k] >= 100 :
            winner = [k]

    print("Player ", [k], "wins the game")

# start game
playGame()

