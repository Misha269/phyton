import sqlite3
import hashlib

connection = sqlite3.connect("db.sl3", timeout=15)
cur = connection.cursor()

users = [("misha", "1234", "misha@gmail.com"),("andrey", "5678", "andrey@gmail.com"), ("alex", "2222", "alex@gmail.com")]


for login, password, email in users:
    h_pass = hashlib.sha256(password.encode("utf-8")).hexdigest()

    cur.execute("INSERT INTO users (login, password, email) VALUES ('{login}', '{h_pass}', '{email}')")
connection.commit()

connection.close()
