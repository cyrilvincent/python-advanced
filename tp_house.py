# Charger house.csv en pandas
# Créer la colonne loyer_per_m2
# np.mean = moyenne
# np.std = ecart type
# np.median = medianne
# Faire la fonction mean_std_median(surface) => Tuple[float, float, float*] => (moyenne, std, mediane)
# Bonus1 : rendre ce code OO
# Bonus2 : doc scipy.linregress : calculer la regression lineaire
# Bonus3 : afficher la regression lineaire
# Correction à 10h25

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as stats

matplotlib.use("Qt5Agg")

class HouseService:

    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.df = self.df[self.df.surface < 200]
        self.df = self.df[self.df.loyer < 20000]
        self.df["loyer_per_m2"] = self.df.loyer / self.df.surface

    def save_json(self, path):
        """
        Save JSON
        :param path: path to file
        :return: None
        """
        self.df.to_json(path)

    def show(self):
        plt.scatter(self.df.surface, self.df.loyer)
        slope, intersect = self.lineregress()
        y = self.df.surface * slope + intersect
        plt.plot(self.df.surface, y, "red")
        plt.show()

    def lineregress(self):
        slope, intersect, corr,  pvalue, err = stats.linregress(self.df.surface, self.df.loyer)
        return slope, intersect



