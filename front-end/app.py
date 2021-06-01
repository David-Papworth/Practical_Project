from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class Pick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operator = db.Column(db.String(120), nullable=False)
    difficulty = db.Column(db.String(120), nullable=False)
    strat = db.Column(db.String(120), nullable=False)
    difficulty_strat = db.Column(db.String(120), nullable=False)
    points_per_kill = db.Column(db.Integer, nullable=False)

@app.route('/')
@app.route('/home')
def home():
    op = requests.get('http://operator_random_api:5000/get_operator')
    st = requests.get('http://strat_random_api:5000/get_strat')
    points = requests.post('http://points_api:5000/get_noise', data={difficulty:op.json.get["difficulty"], difficulty_strat:st.json.get["difficulty"]})
    last_picks = Pick.query.order_by(desc("id")).limit(5).all()
    db.session.add(
        Animals(
            operator = op.json.get["operator"],
            difficulty = op.json.get["difficulty"],
            strat = st.json.get["strat"],
            difficulty_strat = st.json.get["difficulty"],
            points_per_kill = points.text
        )
    )
    db.session.commit()
    return render_template("index.html", title="Home", last_five_animals=last_five_animals)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')