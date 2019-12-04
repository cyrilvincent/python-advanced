import csv
import matplotlib.pyplot as plt

with open("house/house.csv") as f:
    reader = csv.DictReader(f)
    res = (float(row["loyer"]) / float(row["surface"]) for row in reader)

with open("house/house.csv") as f:
    reader = list(csv.DictReader(f))
    loyers = [float(row["loyer"]) for row in reader]
    surfaces = [float(row["surface"]) for row in reader]

    plt.scatter(surfaces, loyers)
    plt.savefig("diagram.png")
    plt.show()
