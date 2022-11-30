from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from functions import getDatetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:6fGMA/AHC8!A-UH@localhost/demo'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    datehired = db.Column(db.Date, unique=False, nullable=False)

with app.app_context():
    while True:
        db.create_all()
        print("1. Skapa employee")
        print("2. Uppdatera employee")
        print("3. Sök efter employee")
        print("4. Lista employees")

        i = int(input("Ange val: "))
        if i == 1:
            b = Employee()
            b.name = input("Ange namn: ")
            b.age = int(input("Ange ålder: "))
            b.datehired = getDatetime("sv", "Ange anställningsdatum: ")
            db.session.add(b)
            db.session.commit()
        elif i == 2:
            for m in Employee.query.all():
                print(f"{m.id} {m.name} {m.age} {m.datehired}")
            sel = int(input("Vilken vill du uppdatera: "))
            b = Employee.query.filter_by(id=sel).first()
            sel = int(input("Vad ska uppdateras? (1. Namn, 2. Ålder, 3. Anställningsdatum:"))
            if sel == 1:
                b.name = input("Ange nytt namn: ")
            elif sel == 2:
                b.age = int(input("Ange ny ålder: "))
            elif sel == 3:
                b.yearhired = int(input("Ange nytt anställningsår: "))
            db.session.commit()
        elif i == 3:
            search = input("Sök efter: ")
            print("Sökresultat")
            for m in Employee.query.filter(Employee.name.contains(search)).all():
                print(f"{m.id} {m.name} {m.age} {m.datehired}")
            print("Slut på sök")
        elif i == 4:
            for m in Employee.query.all():
                print(f"{m.id} {m.name} {m.age} {m.datehired}")