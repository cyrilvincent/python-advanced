import csv
with open("data/media/books.csv") as f:
    reader = csv.DictReader(f)

    # for row in reader:
    #     print(row["title"], float(row["price"]) * 1.2)
    prices = [float(row["price"]) for row in reader if "PYTHON" in row["title"].upper()]
    print(sum(prices) / len(prices))


