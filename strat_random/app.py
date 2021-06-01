from flask import Flask, jsonify
import random 

app = Flask(__name__)

@app.route('/strat')
def strat():
    strat_list = ['Primary Only', 'Secondary Only', 'Snail Mode', 'Train', 'Rush']
    strat_pick = random.choice(strat_list)
    if strat_pick in ['Primary Only', 'Rush']:
        dif = 0
    elif strat_pick in ['Secondary Only', 'Train']:
        dif = 20 
    elif strat_pick in ['Snail Mode']:
        dif = 40
    return jsonify("strat":strat_pick, "difficulty":dif)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)