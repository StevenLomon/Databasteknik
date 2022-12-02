from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from functions import getDatetime, getIntMenuInput
from datetime import datetime, timedelta
import time
import os

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
    type = db.Column(db.String(6), unique=False, nullable=False) #Boolean? 0 is enkel, 1 is dubbel. Enum?
    size = db.Column(db.Integer, unique=False, nullable=False)
    available = db.Column(db.Boolean, unique=False, nullable=False)
    eligible_extra_bed = db.Column(db.Boolean, unique=False, nullable=False)
    reservation_id=db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=True)
    roomstype = db.relationship("RoomType", back_populates="rooms")

class RoomType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(6), unique=False, nullable=False)
    rooms = db.relationship("Room", back_populates="roomstype")

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nr_of_nights = db.Column(db.Integer, unique=False, nullable=False)
    start_date = db.Column(db.Date, unique=False, nullable=False)
    end_date = db.Column(db.Date, unique=False, nullable=False)
    extra_bed = db.Column(db.Boolean, unique=False, nullable=False)
    #reservation_nr = db.Column(db.String(6), unique=False, nullable=False)
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
    print("GÖRAN'S HOTELL\n")
    print("1. Sök lediga rum")
    print("2. Ny bokning")
    print("3. Ändra bokning")
    print("4. Avboka rum")
    print("5. Admin")
    print("6. Avsluta")

def printAdminMenu():
    print("ADMIN MENY\n")
    print("1. Lägg till nytt rum")
    print("2. Ändra rum")
    print("3. Se kunder")
    print("4. Ändra kundinfo")
    print("5. Ta bort kund")
    print("6. Se fakturor")
    print("7. Gå tillbaka")

invoiceDueTime = 10
eligibleForExtraBed = 30
with app.app_context():
    while True:
        db.create_all()

        os.system('cls')
        printMenu()

        i = getIntMenuInput("Ange val: ", 1, 6)
        if i == 1:
            time.sleep(0.5)
            os.system('cls')
            print("LEDIGA RUM")
            for r in Room.query.all(): #TODO implement show only available
                print(f"{r.id} {r.type} {r.size}")
            b = input("\nTryck enter för att gå tillbaka")
        elif i == 2:
            time.sleep(0.5)
            os.system('cls')
            print("BOKAR RUM")
            c = Customer()
            c.name = input("Ange namn: ")
            c.adress = input("Ange adress: ")
            c.postalcode = input("Ange postnummer: ")
            c.city = input("Ange stad: ")
            db.session.add(c)
            db.session.commit()
            availableRooms = []
            for r in Room.query.all(): #TODO implement show only available
                print(f"{r.id} {r.type} {r.size}")
                availableRooms.append(r.id)
            room = getIntMenuInput("Ange rum: ", availableRooms[0], availableRooms[-1])
            #TODO ask for extra bed if dubbelrum is chosen
            r = Reservation()
            r.nr_of_nights = int(input("Hur många nätter? "))
            r.start_date = datetime.now()
            r.end_date = r.start_date + timedelta(days = r.nr_of_nights)
            r.customer_id = c.id
            r.room_id = room
            db.session.add(r)
            db.session.commit()
            print(r.id)
            inv = Invoice()
            inv.is_paid = False
            inv.customer_id = c.id
            inv.due_date = r.start_date + timedelta(days = invoiceDueTime)
            inv.url = input("Ange url: ")
            inv.reservation_id = r.id
            db.session.add(inv)
            db.session.commit()
            print("Rum bokat. Vi ser fram emot ditt besök!")
            time.sleep(2)
            os.system('cls')
        elif i == 3: #TODO Implement reservation number and check if no reservations
            reservations = []
            for r in Reservation.query.all():
                print(f"{r.id} {r.nr_of_nights} {r.start_date} {r.end_date}")
                reservations.append(r.id)
            sel = getIntMenuInput("Vilken bokning ska ändras?", reservations[0], reservations[-1])
        elif i == 4:
            pass
        elif i == 5:
            time.sleep(0.5)
            os.system('cls')
            while True:
                printAdminMenu()
                j = getIntMenuInput("Ange val: ", 1, 7)
                if j == 1:
                    r = Room()
                    r.available = True
                    r.type = input("Ange typ ('enkel' eller 'dubbel'): ")
                    r.size = int(input("Ange storlek: "))
                    if r.type.lower() == 'dubbel' and r.size >= eligibleForExtraBed:
                        r.eligible_extra_bed = True
                    else:
                        r.eligible_extra_bed = False
                    db.session.add(r)
                    db.session.commit()
                    print("Rum tillagt")
                    time.sleep(2)
                    os.system('cls')
                elif j == 4:
                        for c in Customer.query.all():
                            print(f"{c.id} {c.name}")
                        sel = int(input("Vem ska uppdatera? "))
                        c = Customer.query.filter_by(id=sel).first()
                        sel = int(input("Vad ska uppdateras? (1. Namn, 2. Adress, 3. Postnummer, 4. Stad): "))
                        if sel == 1:
                            c.name = input("Ange nytt namn: ")
                        elif sel == 2:
                            c.adress = input("Ange ny adress: ")
                        elif sel == 3:
                            c.postalcode = input("Ange nytt postnummer: ")
                        elif sel == 4:
                            c.city = input("Ange ny stad: ")
                        db.session.commit()
                        print("Kund ändrad")
                        time.sleep(2)
                        os.system('cls')
                elif j == 5:
                    #TODO check if customer has a reservation
                    #TODO delete customer if no reservation
                    #Följade kunder har för nuvarande ingen reservation och har inte gjort en reservation på de senaste 30 dagarna 
                    pass
                elif j == 7:
                    time.sleep(0.5)
                    os.system('cls')
                    break
        elif i == 6:
            print("Ha en fortsatt trevlig dag!")
            time.sleep(2)
            exit()