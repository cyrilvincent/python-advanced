import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mesures/mesures.csv")
#plt.plot(df["T"], df["VM"])
#plt.show()

df = pd.read_csv("house/house.csv")


# Calculer la moyenne des surfaces et des loyers
# Calculer l'ecart type ..
# Calculer la regression linéaire et afficher la droite
# Bonus : filtrer les surfaces > 200 et recalculer la regression

import numpy as np
import scipy.stats
print(f'Moyenne loyers: {np.mean(df["loyer"])}')
print(f'Ecart type loyers: {np.std(df["loyer"])}')
print(f'Moyenne loyer/m²: {np.mean(df["loyer"] / df["surface"])}')
print(f'Medianne loyer/m²: {np.median(df["loyer"] / df["surface"])}')
print(f'Ecart type loyer/m²: {np.std(df["loyer"] / df["surface"])}')

t = scipy.stats.linregress(df["surface"], df["loyer"])
print(f'Linregress: {t}')

plt.subplot(211)
plt.scatter(df["surface"], df["loyer"])
plt.plot(np.arange(450), np.arange(450) * t[0] + t[1])

df = df[df.surface < 200]
t = scipy.stats.linregress(df["surface"], df["loyer"])
print(f'Linregress: {t}')
plt.subplot(212)
plt.scatter(df["surface"], df["loyer"])
plt.plot(np.arange(200), np.arange(200) * t[0] + t[1])
plt.show()
