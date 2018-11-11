from app import app
from flask import render_template, request, session, redirect, jsonify
from app.models import Player
from json import dumps

from random import choice

app.secret_key = 'dude-where-are-my-ethics'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        moral_states = ['MG', 'N', "MB"]
        new_player = Player(request.form['username'], moral_state=choice(moral_states))
        session['username'] = new_player.username
        session['moral_state'] = new_player.moral_state
        return redirect('/game')
    return render_template('login.html')

    
@app.route('/game', methods=['GET', 'POST'])
def game():
    print(session)
    if request.method == 'POST':
        print("Button has been pressed")
        return render_template('game.html', my_string=session['username'],
            my_list=['The', 'quick', 'brown', 'fox'], moral_state=session["moral_state"])


    return render_template('game.html', my_string=session['username'],
            my_list=['The', 'quick', 'brown', 'fox'], moral_state=session["moral_state"])
