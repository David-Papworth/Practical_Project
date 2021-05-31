from application import db

class Pick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operator = db.Column(db.String(120), nullable=False)
    diffulity = db.Column(db.String(120), nullable=False)
    strat = db.Column(db.String(120), nullable=False)
    diffulity_strat = db.Column(db.String(120), nullable=False)
    points_per_kill = db.Column(db.Integer, nullable=False)