from app import app
from flask import render_template, request, session, redirect, jsonify
from app.models import Player
from json import dumps

from random import choice

app.secret_key = 'dude-where-are-my-ethics'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        new_player = Player(request.form['username'])
        encoded = dumps(new_player)
        print(encoded)
        session['username'] = jsonify(new_player)
        return redirect('/game')
    return render_template('login.html')

    
@app.route('/game')
def game():
    moral_states = ['MG', 'N', "MB"]
    moral_state_values = [100, 75, 50, 25]
    print(session)
    return render_template('game.html', my_string="session['username']",
            my_list=['The', 'quick', 'brown', 'fox'], moral_state=choice(moral_states))
