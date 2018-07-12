from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, make_response
import os
import random
import BackEnd
 
app = Flask(__name__)

#App.Route takes you to a specific area.  For example ('/') is the initial page
#GameStart page 
@app.route('/', methods = ['POST', 'GET'])
def GameStart():
    print(request.method)
    if request.method == 'GET':
        return render_template('Page1GameStart.html')
    #return "Hello Bert"
    elif request.method == 'POST':#
        if request.form.get('Start Game') == 'Start Game':
            print('Game Started')
            BackEnd.setupGame()
            return redirect(url_for('GameSetUp'))
        else:
            
            BackEnd.playTurn()
            return BackEnd.playGame()
            #return 'Complete'
            
            # Set up a End Game Template with Options to start again
        #return render_template('Page2GameSetUp.html')
        
        #return str(random.randint(1,10))

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
        print(request.form['noOfPlayers'])
        NumPlayers = request.form['noOfPlayers']
        #BackEnd.createPlayerDict(int(NumPlayers))
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
        BackEnd.playTurn()
        return render_template('Page3GameProgress.html')
  
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
