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

# declare ladder and snake array


# play the game function
def playGame() :
  #while  playerDict[player] < 100 :
  winner = 0
  while winner == 0 :
    for k in playerDict :
        print("Player ", k,"'s turn, your current score is", playerDict[k])
        input("Press enter to roll the dice")
        rollDice()
        playerDict[k] = playerDict[k] + DiceValue
        print("You rolled a ", str(DiceValue), " and your new score is ", playerDict[k])
        if  playerDict[k] >= 100 :
            winner = [k]
    print("Player ", [k], "wins the game")

# start game
playGame()

