from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import random

from BackEnd import createPlayerDict
 
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html', variable='Wank')

@app.route('/PlayGame', methods=['POST'])
def do_admin_login():
    return render_template('Game.html', variable=createPlayerDict(int(request.form['numPlayers'])) )


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)


