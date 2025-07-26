from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class PracticeSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    instrument = db.Column(db.String(50))
    minutes = db.Column(db.Integer)
    notes = db.Column(db.String(200))
    date = db.Column(db.Date, default=datetime.utcnow)
