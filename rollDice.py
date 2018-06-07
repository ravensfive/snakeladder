import random

def funcRollDice() :
    global DiceValue
    DiceValue = str(random.randint(1,6))
    return DiceValue


#     def home():
#     if not session.get('logged_in'):
#         return render_template('login.html', variable='Cock')
#     else:
#         return render_template('Game.html', variable=funcRollDice() )

    
# @app.route('/login', methods=['POST'])
# def do_admin_login():
#     if request.form['numPlayers'] == '1':
#         session['logged_in'] = True
#     else:
#         flash('wrong password!')
#     return home()