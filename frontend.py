from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import random
#from BackEnd import createPlayerDict
 
app = Flask(__name__)

#App.Route takes you to a specific area.  For example ('/') is the initial page
@app.route('/')
def GameStart():
    return render_template('Page1GameStart.html')

@app.route('/GameSetUp',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("Page2GameSetUp.html")


#Post Method selected which creates PlayGame area
#@app.route('/GameSetUp')
#def GameSetUp():


    #return render_template('Page2GameSetUp.html')
    #return render_template('Game.html', variable=createPlayerDict(int(request.form['numPlayers'])) )
    #return render_template('Game.html', variable='Cock')
    
@app.route('/GameProgress')
def gameProgress():
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
