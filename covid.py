import csv
import matplotlib.pyplot as plt

with open("data/covid-france.txt") as f:
    reader = list(csv.DictReader(f))
    x = [int(row["ix"]) for row in reader]
    ynbcas = [int(row["NbCas"]) for row in reader]
    ydc = [int(row["DC"]) for row in reader]

plt.yscale("log")
plt.scatter(x, ynbcas)
plt.bar(x, ydc)
plt.show()

# transformer les listes python en x = np.array(list)
# nbcas et dc = moyenne, min, max
# x = x[x > 40]
# y = y[x > 40] recalculer moyenne, min max au delà du 40ème jour
# tauxletalites = dc / nbcas par jour, moyenne