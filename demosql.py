import sqlite3

db = sqlite3.connect("mesures/mesures.db3")
c = db.cursor()
c.execute("select * from mesure")
for row in c:
    print(row[4])