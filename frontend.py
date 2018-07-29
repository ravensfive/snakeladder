from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, make_response
import os
import random
import BackEnd
 
app = Flask(__name__)

#App.Route takes you to a specific area.  For example ('/') is the initial page
#GameStart page - Give options to Start Game or End Game.
#If Start Game is selected then the Set Up Game function is called and URL Redirects to the Game Set up Page
#If End Game is selected then a new template to be called
@app.route('/', methods = ['POST', 'GET'])
def GameStart():
    print(request.method)
    if request.method == 'GET':
        return render_template('Page1GameStart.html')
    elif request.method == 'POST':
        if request.form.get('Start Game') == 'Start Game':
            print('Game Started')
            BackEnd.setupGame()
            return redirect(url_for('GameSetUp'))
        elif request.form.get('End Game') == 'End Game':
             #TO-DO - Create a screen if End Game has been selected
             # Set up a End Game Template with Options to start again
            return "Finished"

@app.route('/GameSetUp', methods = ['POST', 'GET'])
def GameSetUp():
    #return render_template('Page2GameSetUp.html')
    #str(random.randint(1,10))
    #if requeest.method == 'GET':   
        #return "John" 
     #   return render_template('Page2GameSetUp.html')
    #else:
     #   return str(random.randint(1,10))

    #return str(random.randint(1,10))

    if request.method == 'POST':
        #TO-DO Establish what button has been selected and process based on if
        #TO-DO Validate the responses have been completed correctly
        numPlayers = request.form['noOfPlayers']
        print(numPlayers)
        #TO-DO Create the required number of input boxes based on what numPlayers is
        #TO-DO Create players dynamically based on what's been input
        BackEnd.createPlayers('Simon', 1, True)
        BackEnd.createPlayers('Steve', 2, False)
        return redirect(url_for('gameProgress'))
    else:
        return render_template('Page2GameSetUp.html')
      #BackEnd.createPlayerDict(2)
      #result = request.form
      #return render_template("Page2GameSetUp.html")


#Post Method selected which creates PlayGame area
#@app.route('/GameSetUp')
#def GameSetUp():


    #return render_template('Page2GameSetUp.html')
    #return render_template('Game.html', variable=createPlayerDict(int(request.form['numPlayers'])) )
    #return render_template('Game.html', variable='Cock')
    
@app.route('/GameProgress', methods = ['POST', 'GET'])
def gameProgress():
    if request.method == 'GET':
        return render_template('Page3GameProgress.html')
    elif request.method == 'POST':
        playerName = BackEnd.playTurn()
        print(playerName)
        #return PlayerName
        return render_template('Page3GameProgress.html', playerName=playerName)
  
@app.route('/GameOver')
def gameOver():
    return render_template('Page4GameOver.html')
    
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
