from flask import Flask, request
import random 

app = Flask(__name__)

@app.route('/points')
def points():
    difficulty = request.data["difficulty"]
    difficulty_strat = request.data["difficulty_strat"]
    lower_points = 0
    higher_points = 50
    lower_points += difficulty
    higher_points += difficulty
    lower_points += difficulty_strat
    higher_points += difficulty_strat
    return random.randrange(lower_points, higher_points)