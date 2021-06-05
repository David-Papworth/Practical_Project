from flask import Flask, jsonify
import random 

app = Flask(__name__)

@app.route('/strat')
def strat():
    strat_list = ['Primary Only', 'Secondary Only', 'Snail Mode', 'Train', 'Rush', '1 minute plant', 'last minute rush', 'knife only']
    strat_pick = random.choice(strat_list)
    if strat_pick in ['Primary Only', 'Rush']:
        dif = 0
    elif strat_pick in ['Secondary Only', 'Train', '1 minute plant', 'last minute rush']:
        dif = 20 
    elif strat_pick in ['Snail Mode', 'knife only']:
        dif = 40
    return jsonify({"strat":strat_pick, "difficulty":dif})

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)