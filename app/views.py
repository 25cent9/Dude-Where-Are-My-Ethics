from app import app
from flask import render_template, request, session, redirect

from random import choice

app.secret_key = 'dude-where-are-my-ethics'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect('/game')
    return render_template('login.html')

    
@app.route('/game')
def game():
    moral_states = ['MG', 'N', "MB"]
    print(session)
    if 'state' in session:
        print("state is good")
    else:
        session['state'] = choice(moral_states)
    print(session)
    return render_template('game.html', my_string=session['username'],
            my_list=['The', 'quick', 'brown', 'fox'], moral_state=session['state'])
