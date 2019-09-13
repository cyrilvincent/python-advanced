import csv
import matplotlib.pyplot as plt
import scipy.stats

with open("house/house.csv") as f:
    reader = list(csv.DictReader(f))

surfaces = [float(row["surface"]) for row in reader if float(row["surface"])< 250]
loyers = [float(row["loyer"]) for row in reader if float(row["surface"])< 250]

slope, intercept, _,_,_ = scipy.stats.linregress(surfaces, loyers)

plt.plot(range(250), [slope * x + intercept for x in range(250)])

plt.scatter(surfaces, loyers)
plt.show()