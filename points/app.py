from flask import Flask, request
import random 

app = Flask(__name__)

@app.route('/points', methods=['POST'])
def points():
    difficulty = request.json["difficulty"]
    difficulty_strat = request.json["difficulty_strat"]
    lower_points = 0
    higher_points = 50
    lower_points += difficulty
    higher_points += difficulty
    lower_points += difficulty_strat
    higher_points += difficulty_strat
    return str(random.randrange(lower_points, higher_points))

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000)