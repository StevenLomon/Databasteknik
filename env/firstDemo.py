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