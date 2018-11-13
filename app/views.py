from app import app
from flask import render_template, request, session, redirect, jsonify
from app.models import Player
from json import dumps
from app.utils import read_prompts
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
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print(session)
    if request.method == 'POST':
        print("Button has been pressed")
        return render_template('game.html', my_string=session['username'],
            my_list=['The', 'quick', 'brown', 'fox'], moral_state=session["moral_state"])
    current_month = choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    prompts = read_prompts(current_month)
    actions = prompts[1:]
    return render_template('game.html', month=months[current_month%len(months)-1],
            my_list=['The', 'quick', 'brown', 'fox'], moral_state=session["moral_state"], current_prompt=prompts[0], actions=actions)
