import sqlite3 as db

with db.connect("data/media/books.db3") as conn:
    generator = conn.cursor()
    generator.execute("select id,title,price from book")
    for row in generator:
        print(row[1])