import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9]
y = [0,1,2,3,4,5,6,7,8,9]

plt.bar(x,y) #plot scatter
plt.show()

import csv
with open("data/house/house.csv") as f:
    reader = list(csv.DictReader(f))
    loyers = [float(row["loyer"]) for row in reader]
    surfaces = [float(row["surface"]) for row in reader]
    plt.scatter(surfaces, loyers)
    plt.show()
