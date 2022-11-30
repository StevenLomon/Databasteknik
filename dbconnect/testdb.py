import mysql.connector

namn = input("Skriv namn på nya Shippern: ")
telefon = input("Skriv nummer till nya Shippern: ")

#Släng in dbeaver-tabellen:
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="6fGMA/AHC8@A-UH",
  database="northwind"
)

mycursor = mydb.cursor() 
mycursor.execute(f"INSERT INTO northwind.shippers (CompanyName, Phone) VALUES('{namn}', '{telefon}');")
mydb.commit()