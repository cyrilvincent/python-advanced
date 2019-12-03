import csv

with open("house/house.csv") as f:
    reader = csv.DictReader(f)
    res = (float(row["loyer"]) / float(row["surface"]) for row in reader)
    

