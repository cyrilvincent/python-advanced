import csv
with open("data/media/books.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(float(row["price"]) * 1.2)