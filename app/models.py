# app/models.py
from . import db  # Import the SQLAlchemy instance from your app package

class Player(db.Model):
    __tablename__ = 'players'  # Optional: specify a custom table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    team = db.Column(db.String(50), nullable=False)
    statistics = db.Column(db.JSON, nullable=True)  # If you want to store JSON data
    availability = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Player {self.name}>'
