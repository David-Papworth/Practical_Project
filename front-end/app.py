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
    op = requests.get('http://project_random_operator:5000/operator')
    st = requests.get('http://project_random_strat:5000/strat')
    ops = op.json()["difficulty"]
    stra = st.json()["difficulty"]
    points = requests.post('http://project_points:5000/points', json={"difficulty":ops, "difficulty_strat":stra})
    last_picks = Pick.query.order_by(desc("id")).limit(5).all()
    db.session.add(
        Pick(
            operator = op.json()["operator"],
            difficulty = op.json()["difficulty"],
            strat = st.json()["strat"],
            difficulty_strat = st.json()["difficulty"],
            points_per_kill = int(points.text)
        )
    )
    db.session.commit()
    return render_template("index.html", title="Home", last_picks=last_picks, op=op, st=st, points=points)

if __name__ == "__main__": app.run(debug=True, host='0.0.0.0')