import sqlite3

database = sqlite3.connect('../pokemon-db.sqlite')

# prepare a cursor object
cursorObject = database.cursor()

print("Okay Dokey!")