from flask import Flask, jsonify
import random 

app = Flask(__name__)

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
    return jsonify{"operator": op, "difficulty":dif}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)