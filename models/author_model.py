from db import db

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    auth_name = db.Column(db.String(100), nullable=False)
    auth_age = db.Column(db.Date, nullable=False)
    auth_email = db.Column(db.String(100), unique=True)
    auth_phone = db.Column(db.String(10), nullable=False, unique=True)
    auth_address = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)