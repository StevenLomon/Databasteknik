from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from functions import getDatetime, getIntMenuInput
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:6fGMA/AHC8!A-UH@localhost/hotelmanagement'
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    adress = db.Column(db.String(50), unique=False, nullable=False)
    postalcode = db.Column(db.String(5), unique=False, nullable=False)
    city = db.Column(db.String(50), unique=False, nullable=False)
    reservations = db.relationship('Reservation', backref='Customer', lazy=True)
    invoices = db.relationship('Invoice', backref='Customer', lazy=True)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Boolean, unique=False, nullable=False)
    size = db.Column(db.Integer, unique=False, nullable=False)
    eligigle_extra_bed = db.Column(db.Boolean, unique=False, nullable=False)
    reservation_id=db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nr_of_nights = db.Column(db.Integer, unique=False, nullable=False)
    start_date = db.Column(db.Date, unique=False, nullable=False)
    end_date = db.Column(db.Date, unique=False, nullable=False)
    customer_id=db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    room_id=db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_paid = db.Column(db.Boolean, unique=False, nullable=False)
    due_date = db.Column(db.Date, unique=False, nullable=False)
    url = db.Column(db.String(50), unique=False, nullable=False)
    customer_id=db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    reservation_id=db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)

def printMenu():
    print("Välkommen till Görans's hotell!\n")
    print("1. Sök lediga rum")
    print("2. Ny bokning")
    print("3. Ändra bokning")
    print("4. Avboka rum")
    print("5. Admin")
    print("6. Avsluta")

def printAdminMenu():
    print("1. Lägg till nytt rum")
    print("2. Ändra rum")
    print("3. Se kunder")
    print("4. Ändra kund")
    print("5. Ta bort kund")
    print("6. Se fakturor")
    print("7. Gå tillbaka")

def createNew():
    b = Employee()
    b.name = input("Ange namn: ")
    b.age = int(input("Ange ålder: "))
    b.datehired = getDatetime("sv", "Ange anställningsdatum: ")
    db.session.add(b)
    db.session.commit()

with app.app_context():
    while True:
        db.create_all()

        printMenu()

        i = getIntMenuInput("Ange val: ", 1, 6)
        if i == 1:
            pass
        elif i == 5:
            while True:
                print("ADMIN MENY\n")
                printAdminMenu()
                j = getIntMenuInput("Ange val: ", 1, 7)
                if j == 1:
                    pass
                elif j == 7:
                    break
        elif i == 6:
            print("Ha en fortsatt trevlig dag!")
            time.sleep(1)
            exit()