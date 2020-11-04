import csv
import matplotlib.pyplot as plt

with open("data/house/house.csv") as f:
    reader = list(csv.DictReader(f))
    loyers = [float(row["loyer"]) for row in reader]
    surfaces = [float(row["surface"]) for row in reader]

plt.scatter(surfaces, loyers)
plt.show()