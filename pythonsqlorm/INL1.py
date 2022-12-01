from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from functions import getDatetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:6fGMA/AHC8!A-UH@localhost/auctionsite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    name = db.Column(db.String(50), unique=False, nullable=False)
    adress = db.Column(db.String(50), unique=False, nullable=False)
    postalcode = db.Column(db.String(5), unique=False, nullable=False)
    city = db.Column(db.String(50), unique=False, nullable=False)
    logins = db.relationship('Login', backref='User', lazy=True)
    ads = db.relationship('Ad', backref='User', lazy=True)
    bids = db.relationship('Bid', backref='User', lazy=True)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, unique=False, nullable=False)
    ip_adress = db.Column(db.String(15), unique=False, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    description = db.Column(db.String(150), unique=False, nullable=False)
    startprice = db.Column(db.Integer, unique=False, nullable=False)
    timestamp_start = db.Column(db.DateTime, unique=False, nullable=False)
    timestamp_end = db.Column(db.DateTime, unique=False, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    images = db.relationship('Image', backref='Ad', lazy=True)
    bids = db.relationship('Bid', backref='Ad', lazy=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50), unique=False, nullable=False)
    is_default = db.Column(db.Boolean, unique=False, nullable=False)
    ad_id=db.Column(db.Integer, db.ForeignKey('ad.id'), nullable=False)

class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, unique=False, nullable=False)
    timestamp = db.Column(db.DateTime, unique=False, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ad_id=db.Column(db.Integer, db.ForeignKey('ad.id'), nullable=False)

with app.app_context():
    while True:
        db.create_all()

