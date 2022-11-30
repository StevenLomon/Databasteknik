from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from functions import getDatetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:6fGMA/AHC8!A-UH@localhost/demo'
db = SQLAlchemy(app)

class Hall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Namn = db.Column(db.String(50), unique=False, nullable=False)
    GatuAdress = db.Column(db.String(50), unique=False, nullable=False)
    Stad = db.Column(db.String(50), unique=False, nullable=False)
    Postnr = db.Column(db.String(5), unique=False, nullable=False)
    Banor = db.relationship('Bana', backref='hall', lazy=True)

class Bana(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nummer = db.Column(db.Integer, unique=False, nullable=False)
    Hallid = 
    Banor = db.relationship('Bana', backref='hall', lazy=True)