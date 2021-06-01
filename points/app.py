from flask import Flask, request
import random 

app = Flask(__name__)

@app.route('/points')
def points():
    difficulty = request.data[]
    lower_points = 0
    higher_points = 50
    lower_points += pick.difficulty
    higher_points += pick.difficulty
    lower_points += pick.difficulty_strat
    higher_points += pick.difficulty_strat
    return random.randrange(lower_points, higher_points)