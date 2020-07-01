import matplotlib.pyplot as plt

import csv
with open("data/covid-france.txt") as f:
    reader = list(csv.DictReader(f))
    x = [int(row["ix"]) for row in reader]
    nbcas = [int(row["NbCas"]) for row in reader]
    dcs = [int(row["DC"]) for row in reader]
    plt.plot(x, nbcas)
    plt.plot(x, dcs)
    plt.show()

    # Le nb de cas total
    # Le nb de cas moyen par jour
    # le nb dc total
    # le nb de dc moyen par jour
    # le taux de létalité = nbdctotal / nbcastotal
    # Filtrer pour [ix > 45] et tout recalculer

