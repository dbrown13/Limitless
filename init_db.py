# This is used to create the database and tables along with the two sql files

import sqlite3

connection = sqlite3.connect('userDB.db')

with open('userSchema.sql') as f:
    connection.executescript(f.read())

with open('goalSchema.sql') as f:
    connection.executescript(f.read())

with open('activitySchema.sql') as f:
    connection.executescript(f.read())
    
# CAUTION!!!  Leave this commented out or you will lose all the MET data
#with open('metSchema.sql') as f:
#    connection.executescript(f.read())
    
connection.close()