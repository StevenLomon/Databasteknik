from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from functions import getDatetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:6fGMA/AHC8!A-UH@localhost/demo'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    birthdate = db.Column(db.Date, unique=False, nullable=False)
    label = db.Column(db.String(50), unique=False, nullable=False)
    albums = db.relationship('Album', backref='artist', lazy=True)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    releasedate = db.Column(db.Date, unique=False, nullable=False)
    sales = db.Column(db.Integer, unique=False, nullable=False)
    artist_id=db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    songs = db.relationship('Song', backref='album', lazy=True)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    length = db.Column(db.Integer, unique=False, nullable=False)
    album_id=db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        while True:
            #db.create_all()
            upgrade()
            print("1. Skapa artist")
            print("2. Skapa album")
            print("3. Skapa låt")

            i = int(input("Ange val: "))
            if i == 1:
                b = Artist()
                b.name = input("Ange namn: ")
                b.birthdate = getDatetime("sv", "Ange födelsedatum: ")
                b.label = input("Ange label: ")
                db.session.add(b)
                db.session.commit()
            elif i == 2:
                b = Album()
                b.name = input("Ange namn: ")
                b.releasedate = getDatetime("sv", "Ange releasedatum: ")
                for m in Artist.query.all():
                    print(f"{m.id} {m.name}")
                sel = int(input("Vilken artist hör detta album till? "))
                b.artist_id = sel
                db.session.add(b)
                db.session.commit()
            elif i == 3:
                b = Song()
                b.name = input("Ange namn: ")
                b.length = int(input("Ange längd i seuknder: "))
                for m in Album.query.all():
                    print(f"{m.id} {m.name}")
                sel = int(input("Vilket album hör denna sång till? "))
                b.album_id = sel
                db.session.add(b)
                db.session.commit()






