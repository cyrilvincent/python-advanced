import matplotlib.pyplot as plt
import numpy as np
import csv
with open("data/covid-france.txt") as f:
    reader = list(csv.DictReader(f))
    x = np.array([int(row["ix"]) for row in reader])
    nbcas = np.array([int(row["NbCas"]) for row in reader])
    dcs = np.array([int(row["DC"]) for row in reader])
    plt.plot(x, nbcas)
    plt.plot(x, dcs)
    plt.show()

    # Le nb de cas total
    # Le nb de cas moyen par jour
    # le nb dc total
    # le nb de dc moyen par jour
    # le taux de létalité = nbdctotal / nbcastotal
    # Filtrer pour [ix > 45] et tout recalculer
    nbcastotal = sum(nbcas)
    nbcasmoyen = np.mean(nbcas)
    nbdctotal = sum(dcs)
    nbdcmoyen = np.mean(dcs)
    print(nbcastotal, nbcasmoyen)
    print(nbdctotal, nbdcmoyen)
    print(nbdctotal / nbcastotal)
    nbcas = nbcas[x > 44]
    dcs = dcs[x > 44]
    nbcastotal = sum(nbcas)
    nbcasmoyen = np.mean(nbcas)
    nbdctotal = sum(dcs)
    nbdcmoyen = np.mean(dcs)
    print(nbcastotal, nbcasmoyen)
    print(nbdctotal, nbdcmoyen)
    print(nbdctotal / nbcastotal)

import pandas as pd

dataframe = pd.read_csv("data/covid-france.txt")
ix = dataframe["ix"]
nbcas = dataframe.NbCas
dcs = dataframe.DC
print(nbcas)
