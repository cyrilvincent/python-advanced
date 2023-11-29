import pandas as pd
import numpy as np
import config.config as config

print(config.version)

# Charger par pandas un house.csv avec le path
# service.load("data/house/house.csv") déduit qu'il faut utiliser read_csv par l'extension

# service.mean("surface") => 65.1
# service.str("surface")
# Tester unittest

# Avec qtdesigner créer une mainwindow avec menu
# Créer l'attribut qui instancie HouseService + load
# File / Open => Ouvrir une filedialog pour choisir le fichier
# Créer une combo avec les valeurs "surface", loyer (dataframe.columns)
# Créer un bouton Ok => slot Affiche la moyenne de la colonne spécifiée

class HouseService:

    def __init__(self):
        self.dataframe = None

    def extension(self, path: str) -> str:
        index = path.rindex(".")
        extension = path[index + 1:]
        return extension

    def load(self, path: str):
        extension = self.extension(path)
        if extension == "csv":
            self.dataframe = pd.read_csv(path)
        elif extension == "xlsx":
            self.dataframe = pd.read_excel(path)
        else:
            raise ValueError(f"Bad extension {extension}")

    def mean(self, column: str):
        return np.mean(self.dataframe[column])

    def median(self, column: str):
        return np.median(self.dataframe[column])
