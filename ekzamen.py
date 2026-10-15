import sqlite3
import hashlib

connection = sqlite3.connect ("db. s13", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE users(dohod TEXT Vutrat TEXT suma TEXT")
connection.commit()

dohod = int(input("Походи : "))
vutratu = int(input ("Витрати: "))
suma = int((dohod-vutratu))
h = hashlib.sha256()
h_vutratu = h.hexdigest()
cur.execute(f"INSERT INTO users (dohod, vutratu, suma) VALUES ('{dohod}', '{vutratu}', '{suma}'")
connection.commit()

connection.close()