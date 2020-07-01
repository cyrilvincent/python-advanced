import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("data/covid-france.txt")
ix = dataframe["ix"]
nbcas = dataframe.NbCas
dcs = dataframe.DC
plt.plot(ix, nbcas)
plt.plot(ix, dcs)

import sklearn.linear_model as lm
import sklearn.pipeline as pipe
import sklearn.preprocessing as pp

model = pipe.make_pipeline(pp.PolynomialFeatures(4), lm.Ridge())
model.fit(ix.values.reshape(-1,1), dataframe.NbCas)
plt.plot(ix, model.predict(ix.values.reshape(-1,1)))
plt.show()



