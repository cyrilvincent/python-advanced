import csv

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    res = [(float(row["loyer"]) / float(row["surface"]), float(row["loyer"]) ** 0.5) for row in reader]
    max = 0
    for data0, data1 in res:
        if data0 > max:
            max = data0


print(max)

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    surfaces = []
    loyers = []
    for row in reader:
        surfaces.append(float(row["surface"]))
        loyers.append(float(row["loyer"]))
    for loyer, surface in zip(loyers, surfaces):
        print(loyer / surface)


print(max)

