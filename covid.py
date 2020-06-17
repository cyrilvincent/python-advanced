import csv
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("data/covid-france.txt")
print(dataframe)
# with open("data/covid-france.txt") as f:
#     reader = list(csv.DictReader(f))
#     x = [int(row["ix"]) for row in reader]
#     ynbcas = [int(row["NbCas"]) for row in reader]
#     ydc = [int(row["DC"]) for row in reader]

plt.yscale("log")
plt.scatter(dataframe["ix"], dataframe.NbCas)
plt.bar(dataframe["ix"], dataframe.DC)
plt.show()


# transformer les listes python en x = np.array(list)
# nbcas et dc = moyenne, min, max
# x = x[x > 40]
# y = y[x > 40] recalculer moyenne, min max au delà du 40ème jour
# tauxletalites = dc / nbcas par jour, moyenne
import numpy as np
# x = np.array(x)
# ynbcas = np.array(ynbcas)
# ydc = np.array(ydc)
print("NbCas", np.mean(dataframe.NbCas), np.min(dataframe.NbCas), np.max(dataframe.NbCas), np.std(dataframe.NbCas))
print("DC", np.mean(dataframe.DC), np.min(dataframe.DC), np.max(dataframe.DC), np.std(dataframe.DC))
dataframe.NbCas = dataframe.NbCas[dataframe["ix"] > 40]
dataframe.DC = dataframe.DC[dataframe["ix"] > 40]
print("NbCas", np.mean(dataframe.NbCas), np.min(dataframe.NbCas), np.max(dataframe.NbCas), np.std(dataframe.NbCas))
print("DC", np.mean(dataframe.DC), np.min(dataframe.DC), np.max(dataframe.DC), np.std(dataframe.DC))
letalities = dataframe.DC / dataframe.NbCas
print(letalities)
print(np.mean(letalities))
dataframe.to_excel("data/covid.xlsx")
