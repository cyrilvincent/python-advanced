# Charger avec pandas mesures.csv
# Calculer la moyenne de VM => 0 le max = 240
# |VM - VT| > bruit, bruit = 1v
# Filtrer le dataframe pour obtenir les erreurs
# Bonus afficher à l'écran
# 15h45

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
dataframe = pd.read_csv("data/mesures/mesures.csv")
plt.plot(dataframe["T"], dataframe.VM)
errors = np.abs(dataframe.VM - dataframe.VT)
plt.plot(dataframe["T"], errors)
plt.show()
errors = dataframe[errors > 1]
print(errors)