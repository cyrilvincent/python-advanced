import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/mesures/mesures.csv")
plt.plot(df.vm)
plt.show()

# vt = volt theorique
noise = 1
# Afficher la courbe |vt - vm|
# Filtrer les incidents |vt - vm| > noise et les afficher
