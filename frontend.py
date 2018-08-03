from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, make_response
import os
import random
import BackEnd
 
app = Flask(__name__)

#App.Route takes you to a specific area.  For example ('/') is the initial page
#GameStart page - Give options to Start Game or End Game.
#If Start Game is selected then the Set Up Game function is called and URL Redirects to the Game Set up Page
#If End Game is selected then the user has the option to begin or end the game for certain
@app.route('/', methods = ['POST', 'GET'])
def GameStart():
    if request.method == 'GET':
        return render_template('Page1GameStart.html')
    elif request.method == 'POST':
        if request.form.get('Start Game') == 'Start Game':
            print('Game Started')
            BackEnd.setupGame()
            return redirect(url_for('GameSetUp'))
        elif request.form.get('End Game') == 'End Game':
            return redirect(url_for('gameExit'))

# Called from the GameStart function when a user selects End Game
# The user is then presented with a choice to end the game or go back and start again
@app.route('/gameExit', methods = ['POST', 'GET'])
def gameExit():
    if request.method == 'POST':
        print (request.method)
        if request.form.get('Begin Game') == 'Begin Game':
            return redirect(url_for('GameStart'))
        elif request.form.get('End Game') == 'End Game':
            return "That's a real shame"
    else:
        return render_template('Page5GameOver.html')


@app.route('/GameSetUp', methods = ['POST', 'GET'])
def GameSetUp():
    if request.method == 'POST':
        if request.form.get('Add Player') == 'Add Player':
            return 'I need to write some code to set up a template with an input box and then loop through'
        elif request.form.get('Start Game') == 'Start Game':
            #TO-DO Validate the responses have been completed correctly
            numPlayers = request.form['noOfPlayers']
            player1 = request.form['Player One']
            player2 = request.form['Player Two']
            #TO-DO Create the required number of input boxes based on what numPlayers is
            BackEnd.createPlayers(player1, 1, True)
            BackEnd.createPlayers(player2, 2, False)
            return redirect(url_for('gameProgress'))
    else:
        return render_template('Page2GameSetUp.html')

    
@app.route('/GameProgress', methods = ['POST', 'GET'])
def gameProgress():
    if request.method == 'GET':
        return render_template('Page3GameProgress.html')
    elif request.method == 'POST':
        playerName, playerPreviousScore, playerScore, hasWon = BackEnd.playTurn()
        #return PlayerName
        if hasWon == True:
            return redirect(url_for('gameOver'))
        else:
            return render_template('Page3GameProgress.html', playerName=playerName, 
            playerScore=playerScore, playerPreviousScore=playerPreviousScore, hasWon=hasWon)
  
@app.route('/gameOver')
def gameOver():
    winningPlayer = BackEnd.isWinner()
    print(winningPlayer)
    return render_template('Page4GameOver.html', winningPlayer=winningPlayer)
    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)

# 1) Open Title Page - Snakes and Ladders - With a Button to Play Game
# 1a) Hitting the Play Game button loads the next page (/SetUpGame)
# 2) Second Page - Contains details on how many tiles, how many players and the players names
# 2a) Sets up the JSON file with these details
# 3) Third Page - The Game Page - This will have the grid, and move the counters.  Image of a Dice
# to click which looks into the JSON file, retrieves the details and presents them
# 4) Game over page.  Well done to the winner and Button for Play again? - If clcked, loops back to 
# Open Title Page
