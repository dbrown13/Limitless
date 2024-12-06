# This is used to create the database and tables along with the two sql files

import sqlite3

connection = sqlite3.connect('userDB.db')

#with open('userSchema.sql') as f:
#    connection.executescript(f.read())

#with open('goalSchema.sql') as f:
#    connection.executescript(f.read())

with open('activitySchema.sql') as f:
    connection.executescript(f.read())
    
connection.close()