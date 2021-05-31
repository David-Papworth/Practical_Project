from application import app, db
from application.models import Pick
from flask import render_template, request, redirect, url_for
import random

@app.route('/')
@app.route('/home')
def home():
    picks = Pick.query.limit(5)
    output = ""
    return render_template("index.html", title="Home", picks = picks)

@app.route('/operator')
def operator():
    operator_list = ['Sledge', 'Thatcher', 'Ash', 'Thermite', 'Montagne', 'Twitch', 'Blitz', 'Fuze', 'Glaz']
    op = random.choice(operator_list)
    if op in ['Ash', 'Sledge']:
        dif = 0
    elif op in ['Thatcher', 'Thermite', 'Twitch', 'Blitz']:
        dif = 10 
    elif op in ['Montagne', 'Fuze', 'Glaz']:
        dif = 20 
    new_pick = Pick(operator=op, diffulity=dif)
    db.session.add(new_pick)
    db.session.commit()
    return redirect(url_for('strat'))

@app.route('/strat')
def strat():
    strat_list = ['Primary Only', 'Secondary Only', 'Snail Mode', 'Train', 'Rush']
    strat_pick = random.choice(strat_list)
    pick = Pick.query.filter_by(id=id).first()
    if strat_pick in ['Primary Only', 'Rush']:
        dif = 0
    elif strat_pick in ['Secondary Only', 'Train']:
        dif = 20 
    elif strat_pick in ['Snail Mode']:
        dif = 40
    pick.strat = strat_pick
    pick.diffulity_strat = dif
    return redirect(url_for('points'))

@app.route('/points')
def points():
    lower_points = 0
    higher_points = 50
    lower_points += pick.diffulity
    higher_points += pick.diffulity
    lower_points += pick.diffulity_strat
    higher_points += pick.diffulity_strat
    return redirect(url_for('home'))