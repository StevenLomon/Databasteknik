from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from functions import getDatetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:6fGMA/AHC8!A-UH@localhost/bengan'
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
    Hall_id=db.Column(db.Integer, db.ForeignKey('hall.id'), nullable=False)
    Bokningar = db.relationship('Bokning', backref='bana', lazy=True)

class Medlem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Namn = db.Column(db.String(50), unique=False, nullable=False)
    GatuAdress = db.Column(db.String(50), unique=False, nullable=False)
    Stad = db.Column(db.String(50), unique=False, nullable=False)
    Postnr = db.Column(db.String(5), unique=False, nullable=False)
    Medlemsnummer = db.Column(db.String(15), unique=False, nullable=False)
    Serier = db.relationship('Serie', backref='medlem', lazy=True)
    Bokningar = db.relationship('Bokning', backref='medlem', lazy=True)

class Bokning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DateAndTime = db.Column(db.Date, unique=False, nullable=False)
    Bana_id=db.Column(db.Integer, db.ForeignKey('bana.id'), nullable=False)
    BokadAvMedlem_id=db.Column(db.Integer, db.ForeignKey('medlem.id'), nullable=False)

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    SerieNr = db.Column(db.String(15), unique=False, nullable=False)
    Omg1 = db.Column(db.Integer, unique=False, nullable=False)
    Omg2 = db.Column(db.Integer, unique=False, nullable=False)
    Omg3 = db.Column(db.Integer, unique=False, nullable=False)
    Omg4 = db.Column(db.Integer, unique=False, nullable=False)
    Omg5 = db.Column(db.Integer, unique=False, nullable=False)
    Omg6 = db.Column(db.Integer, unique=False, nullable=False)
    Omg7 = db.Column(db.Integer, unique=False, nullable=False)
    Omg8 = db.Column(db.Integer, unique=False, nullable=False)
    Omg9 = db.Column(db.Integer, unique=False, nullable=False)
    Omg10 = db.Column(db.Integer, unique=False, nullable=False)
    Slutpoäng = db.Column(db.Integer, unique=False, nullable=False)
    Medlems_id=db.Column(db.Integer, db.ForeignKey('medlem.id'), nullable=False)        
    Boknings_id=db.Column(db.Integer, db.ForeignKey('bokning.id'), nullable=False)

with app.app_context():
    while True:
        db.create_all()
        