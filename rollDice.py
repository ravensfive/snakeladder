import random

def funcRollDice() :
    global DiceValue
    DiceValue = str(random.randint(1,6))
    return DiceValue