import sqlite3

connection = sqlite3.connect('userDB.db')

with open('userSchema.sql') as f:
    connection.executescript(f.read())
    
connection.close()