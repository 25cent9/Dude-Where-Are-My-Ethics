from app import app
from flask import render_template, request, session, redirect, jsonify
from json import dumps
from app.utils import read_prompts, gather_images, parse_image_location, find_moral_results
from random import choice, randint

app.secret_key = 'dude-where-are-my-ethics'
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 
            'July', 'August', 'September', 'October', 'November', 'December']
MORAL_STATES = ['MG', 'N', "MB"]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['moral_state'] = choice(MORAL_STATES)
        session['prompt_number'] = 0
        session['moral_score'] = 0
        session['end'] = False
        return redirect('/game')
    return render_template('login.html')

    
@app.route('/game', methods=['GET', 'POST'])
def game(start = False):
    if session["prompt_number"] == 15:
        session["prompt_number"] = 0
        session["end"] = True
        _moral_score, _moral_state, _result_image = find_moral_results(session["moral_score"])
        session["moral_score"] = 0
        return render_template('results.html', moral_score=_moral_score,
            moral_state=_moral_state, result_image=_result_image)
    elif session["prompt_number"] < 15:
        session['prompt_number'] += 1
    current_month = session['prompt_number']
    prompts = read_prompts(current_month)
    images = gather_images(current_month)
    actions = prompts[1:]
    if request.method == 'POST':
        elements = []
        for value in request.form:
            elements.append(value)
        response = parse_image_location(elements[0])
        session['moral_score'] += int(response)
        return render_template('game.html', month=MONTHS[current_month%len(MONTHS)-1], 
            prompt_number=session["prompt_number"], current_prompt=prompts[0], actions=actions, prompt_images=images, score=session['moral_score'])
    return render_template('game.html', month=MONTHS[current_month%len(MONTHS)-1], 
        prompt_number=session["prompt_number"], current_prompt=prompts[0], actions=actions, prompt_images=images, score=session['moral_score'])