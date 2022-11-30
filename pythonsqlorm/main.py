from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:6fGMA/AHC8!A-UH@localhost/demo'
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    players = db.relationship('Player', backref='team', lazy=True)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    jersey = db.Column(db.Integer, unique=False, nullable=False)
    team_id=db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

with app.app_context():
    while True:
        db.create_all()
        print("1. Skapa team")
        print("2. Uppdatera team")
        print("3. Lista teams")
        print("4. Skapa player")
        print("5. Lista players")
        print("6. Uppdatera player")
        print("7. Sök player")
        
        i = int(input("Ange val: "))
        if i == 1:
            o = Team()
            o.city = input("Ange city: ")
            o.namn = input("Ange namn: ")
            db.session.add(o)
            db.session.commit()
        elif i == 2:
            for m in Team.query.all():
                print(f"{m.id} {m.namn} {m.city}")
            sel = int(input("Vilket teamid vill du uppdatera? "))
            b = Team.query.filter_by(id=sel).first()
            b.namn = input("Ange nytt namn:")
            b.city = input("Ange nytt city:")
            db.session.commit()
        elif i == 3:
            for m in Team.query.all():
                print(f"{m.id} {m.namn} {m.city}")

        elif i == 4:
            b = Player()
            b.namn = input("Ange namn: ")
            b.jersey = int(input("Ange jersey: "))
            b.year = int(input("Ange birthyear: "))
            for m in Team.query.all():
                print(f"{m.id} {m.namn} {m.city}")
            sel = int(input("Vilket teamid hör denna till"))
            b.team_id = sel
            db.session.add(b)
            db.session.commit()
        elif i == 5:
            for m in Player.query.all():
                print(m.namn)
        elif i == 6:
            for m in Player.query.all():
                print(f"{m.id} {m.namn}")
            sel = int(input("Vilken vill du uppdatera:"))
            b = Player.query.filter_by(id=sel).first()
            b.namn = input("Ange nytt namn:")
            db.session.commit()
        elif i == 7:
            search = input("Sök efter")
            print("Sökresultat")
            for m in Player.query.filter(Player.namn.contains(search)).all():
                print(f"{m.id} {m.namn}")
            print("Slut sök")