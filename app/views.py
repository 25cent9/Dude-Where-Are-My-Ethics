from app import app
from flask import render_template, request, session, redirect, jsonify
from app.models import Player
from json import dumps
from app.utils import read_prompts, gather_images, parse_image_location
from random import choice, randint

app.secret_key = 'dude-where-are-my-ethics'
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 
            'July', 'August', 'September', 'October', 'November', 'December']

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        moral_states = ['MG', 'N', "MB"]
        new_player = Player(request.form['username'], moral_state=choice(moral_states))
        session['username'] = new_player.username
        session['moral_state'] = new_player.moral_state
        session['prompt_number'] = 1
        return redirect('/game')
    return render_template('login.html')

    
@app.route('/game', methods=['GET', 'POST'])
def game():
    print(session['prompt_number'])
    current_month = session['prompt_number']
    prompts = read_prompts(current_month)
    images = gather_images(current_month)
    actions = prompts[1:]
    if request.method == 'POST':
        elements = []
        for value in request.form:
            elements.append(value)
        response = parse_image_location(elements[0])
        if session["prompt_number"] == 15:
            session["prompt_number"] = 1
        elif session["prompt_number"] >= 1:
            session['prompt_number'] += 1
        current_month = session['prompt_number']
        prompts = read_prompts(current_month)
        images = gather_images(current_month)
        return render_template('game.html', month=MONTHS[current_month%len(MONTHS)], 
            prompt_number=session["prompt_number"], current_prompt=prompts[0], actions=actions, prompt_images=images)
    return render_template('game.html', month=MONTHS[0], 
        prompt_number=session["prompt_number"], current_prompt=prompts[0], actions=actions, prompt_images=images)