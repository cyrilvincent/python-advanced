import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/mesures/mesures.csv")
plt.subplot(211)
plt.plot(df.vm)
plt.subplot(212)
plt.plot(np.abs(df.vm - df.vt))
plt.show()

noise = 1
df_errors = df[np.abs(df.vm - df.vt) > noise]
print(df_errors)
