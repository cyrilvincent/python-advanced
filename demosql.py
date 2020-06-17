import sqlite3

with sqlite3.connect("data/media/books.db3") as connect:
    cursor = connect.execute("select id,title,price from book")
    # for row in cursor:
    #     print(row[2] * 1.2)
    prices = [row[2] for row in cursor]
    print(sum(prices) / len(prices))