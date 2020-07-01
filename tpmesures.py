# Charger data/mesures/mesures.csv avec pandas
# Afficher les courbes VM et AM
# Et afficher les erreurs |VM - VT|
# Calculer le VM moyen = 0 min = -240 et max = +240
# Chercher les erreurs |VM - VT| > bruit = 1v
# Chercher les erreurs |AM - AT| > bruit = 1v
# Faire la même chose pour db3 : select t,at,vt,am,vm from mesure
# Bonus : idem avec xlsx

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3 as db

dataframe = pd.read_csv("data/mesures/mesures.csv")
plt.subplot(211)
plt.title = "Mesures"
plt.plot(dataframe["T"], dataframe.VM, label="VM")
plt.plot(dataframe["T"], dataframe.AM, label="AM")
plt.legend()
plt.subplot(212)
plt.title = "Erreurs"
plt.plot(dataframe["T"], np.abs(dataframe.VM - dataframe.VT), label="VM-VT")
plt.plot(dataframe["T"], np.abs(dataframe.AM - dataframe.AT), label="AM-AT")
plt.legend()
plt.show()

print(np.min(dataframe.VM), np.max(dataframe.VM), np.mean(dataframe.VM))
noise = 1
Verrors = dataframe[np.abs(dataframe.VM - dataframe.VT) > noise]
print(Verrors)
Aerrors = dataframe[np.abs(dataframe.AM - dataframe.AT) > noise]
print(Aerrors)

with db.connect("data/mesures/mesures.db3") as conn:
    dataframe = pd.read_sql("select t,at,vt,am,vm from mesure",conn)
plt.subplot(211)
plt.title = "Mesures"
plt.plot(dataframe["t"], dataframe.vm, label="VM")
plt.plot(dataframe["t"], dataframe.am, label="AM")
plt.legend()
plt.subplot(212)
plt.title = "Erreurs"
plt.plot(dataframe["t"], np.abs(dataframe.vm - dataframe.vt), label="VM-VT")
plt.plot(dataframe["t"], np.abs(dataframe.am - dataframe["at"]), label="AM-AT")
plt.legend()
plt.show()

print(np.min(dataframe.vm), np.max(dataframe.vm), np.mean(dataframe.vm))
noise = 1
Verrors = dataframe[np.abs(dataframe.vm - dataframe.vt) > noise]
print(Verrors)
Aerrors = dataframe[np.abs(dataframe.am - dataframe["at"]) > noise]
print(Aerrors)